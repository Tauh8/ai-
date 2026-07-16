#!/usr/bin/env python3
r"""课件配图分辨率门禁(编译后必跑)。
用法: python3 check_figs.py 你的文档.tex [--assets 图片目录]

规则:
  1. 文字/图表/界面类位图:>=16 px/mm(约 400dpi,1080p 全屏投影有余量);
  2. 照片/画作类位图:>=12 px/mm(照片对软化容忍度高)——文件名加进 PHOTO_CLASS;
  3. 矢量 PDF 免检;豁免表 EXCEPTIONS 须写明理由;
  4. 修复手段只有两种:换更高清图源,或缩小展示尺寸 —— 禁止上采样凑数
     (插值放大 = 伪造像素,投影仪上一眼糊)。

识别的用法:\DAfigbox{Nmm}{file}{...} / \DAfigbox*{Nmm}{file}{...} /
\includegraphics[width=Nmm]{file} / \includegraphics[height=Nmm]{file};
自动跟随一层 \input{...} 正文、自动读 \graphicspath{{dir/}}。
"""
import os
import re
import sys

from PIL import Image

FLOOR_TEXT = 16.0   # 含文字/线条/UI 的图
FLOOR_PHOTO = 12.0  # 照片/绘画类
PHOTO_CLASS: set[str] = set()   # 例:{"portrait.jpg", "eniac.png"}
EXCEPTIONS: dict[str, str] = {}  # 例:{"lowres.png": "论文原图本身低清 —— 模糊即内容"}

VECTOR_EXT = (".pdf", ".eps", ".svg")


def strip_comments(text: str) -> str:
    # 剥掉 LaTeX 行内注释(未转义的 % 起):注释里的示例代码不应触发门禁
    return "\n".join(re.sub(r"(?<!\\)%.*", "", ln) for ln in text.splitlines())


def read_tex(path: str, base: str) -> str:
    text = strip_comments(open(path, encoding="utf-8").read())
    # 跟随一层 \input{...}(共享正文双驱动的常见结构)
    def inline(m: re.Match) -> str:
        name = m.group(1)
        if not name.endswith(".tex"):
            name += ".tex"
        sub = os.path.join(base, name)
        return strip_comments(open(sub, encoding="utf-8").read()) if os.path.exists(sub) else ""
    return re.sub(r"\\input\{([^}]+)\}", inline, text)


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    texpath = args[0]
    base = os.path.dirname(os.path.abspath(texpath))
    tex = read_tex(texpath, base)

    assets = None
    for i, a in enumerate(sys.argv):
        if a == "--assets" and i + 1 < len(sys.argv):
            assets = sys.argv[i + 1]
    if assets is None:
        m = re.search(r"\\graphicspath\{\{([^}]+)\}\}", tex)
        assets = os.path.join(base, m.group(1)) if m else base

    uses = [("h", g[0], g[1]) for g in
            re.findall(r"\\DAfigbox\*?\{([\d.]+)mm\}\{([^}]+)\}", tex)]
    uses += [(("w" if g[0] == "width" else "h"), g[1], g[2]) for g in
             re.findall(r"\\includegraphics\[(width|height)=([\d.]+)mm\]\{([^}]+)\}", tex)]

    fails, missing = [], []
    for mode, mm, fname in uses:
        if fname.lower().endswith(VECTOR_EXT):
            print(f"  vector    -    {fname}")
            continue
        if fname in EXCEPTIONS:
            print(f"  exempt    -    {fname}  ({EXCEPTIONS[fname]})")
            continue
        fpath = os.path.join(assets, fname)
        if not os.path.exists(fpath):
            missing.append(fname)
            print(f"  MISS      -    {fname}(找不到文件,--assets 指定图片目录)")
            continue
        im = Image.open(fpath)
        px = im.height if mode == "h" else im.width
        ppm = px / float(mm)
        floor = FLOOR_PHOTO if fname in PHOTO_CLASS else FLOOR_TEXT
        ok = ppm >= floor
        cls = "photo" if fname in PHOTO_CLASS else "text "
        print(f"  {'OK' if ok else 'FAIL':4s} {ppm:5.1f}/{floor:.0f} {cls} "
              f"{fname} ({im.width}x{im.height} @ {mm}mm{mode})")
        if not ok:
            fails.append(fname)

    if fails or missing:
        if fails:
            print(f"\n分辨率不达标 {len(fails)} 张: {', '.join(fails)}"
                  " —— 换高清源或缩小展示尺寸,禁止上采样")
        return 1
    print("\n全部达标")
    return 0


if __name__ == "__main__":
    sys.exit(main())
