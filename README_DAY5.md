# Day 5：Git 团队协作与全栈应用部署

这套课件基于 DragonFDE LaTeX Beamer 模板制作，共 109 个 PDF 页面、10 个章节。内容从 Git 本地模型和小团队开发流程开始，依次讲解冲突处理、主分支治理、服务器配置、宝塔部署、Docker / Compose、Node 前端、FastAPI 后端、Node 后端、域名、反向代理、SSL 与上线运维。

## 两种输出

- `main.tex`：放映版，保留模板的红底强调和完整视觉效果。
- `main-ppt.tex`：PPT 转换友好版，减少不利于 PDF 转 PPT 的复杂样式。

编译命令：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
latexmk -xelatex -interaction=nonstopmode -halt-on-error main-ppt.tex
```

需使用 XeLaTeX。当前版本在 macOS 上使用 `Heiti SC`、`Songti SC` 和 `Avenir Next`；如果换到 Linux 或 Windows，请在 `common.tex` 与 `beamerthemedragonai.sty` 中替换为当地已安装字体。

## 章节结构

1. 开场与今日交付
2. Git 核心模型与本地工作流
3. GitHub 团队协作工作流
4. 冲突处理、Review 与主分支治理
5. 服务器购买与部署架构
6. 通过宝塔部署全栈项目
7. Docker 基础与部署模型
8. Docker 部署 Node 前端与 FastAPI
9. 域名、反向代理与 SSL 证书
10. 运维、排错、回滚与课堂实战

服务器购买页位于 PDF 第 33 页（5.1）。

## 文件结构

```text
main.tex                 放映版入口
main-ppt.tex             PPT 转换友好版入口
common.tex               两个版本共享的字体、代码块和绘图配置
body.tex                 章节入口
sections/                10 个章节的正文
assets/official/         GitHub、宝塔、Let's Encrypt 官方素材
assets/generated/        为课件生成的教学示意图
beamerthemedragonai.sty  DragonAI Beamer 主题
check_figs.py            配图分辨率检查
```

## 配图与资料

课件中的界面截图来自 GitHub、宝塔和 Let's Encrypt 官方文档，技术内容优先参考 Git、GitHub、pnpm、uv、FastAPI、Docker、NGINX、Cloudflare、Let's Encrypt、MDN 与工信部公开资料。每个关键截图和规则页均在页脚标注来源，最后两页提供了集中参考链接。

本课件中的域名、IP、仓库名、密钥和密码均为教学示例。实际演示时应替换为自己的资源，并避免在投屏、录屏或 Git 历史中暴露 Secret。

## 质量检查

- 放映版与 PPT 转换友好版均已通过 XeLaTeX 编译。
- 两个版本均为 109 页、16:9。
- 编译日志无 Overfull 警告。
- `python3 check_figs.py main.tex` 检查结果为“全部达标”。
- 放映版已逐页渲染并完成接触表视觉检查。
