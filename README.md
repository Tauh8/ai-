# 烛龙智元 · DragonAI Beamer 主题 · v3.2

高级感 · 简约。纯白纸面,红底白字只作块级强调,衬线汉字标题,等宽字标注,每页页脚正式微字标。16:9。

**设计目标:像写论文一样写幻灯片。** 结构命令 + 内容,版式全部由主题接管——文档里不出现任何 `\vskip` / `raisebox` / 手工 tabular 配置。上手请读《使用说明.md》并直接复制 `starter.tex` 开写;本文件是完整参考。v3.1/v3.2 把一整套课件实战经验(44 页 6 章授课课件 + 多轮评审返工)沉淀回主题:素材图组件、PPT 可编辑交付模式、目录密度自适应、折行悬挂,外加排版预算与排错速查。

## 文件

| 文件 | 说明 |
|---|---|
| `使用说明.md` | **从这里开始**:三步上手 + 每种页怎么写(面向作者) |
| `starter.tex` / `starter.pdf` | 模板骨架:复制改内容即可开写(PDF 为成品参照) |
| `beamerthemedragonai.sty` | 主题本体(选项 / 色彩 / 字体 / 部件 / 组件 / 版面 / 作者 API) |
| `demo.tex` / `demo.pdf` | 示例文稿,覆盖全部版式与全部组件,可当对照表用 |
| `check_figs.py` | 配图分辨率门禁(编译后跑一次,位图糊不糊用数字说话) |
| `logo-dragonai-full-cutout.png` | 标识(缺失时自动隐藏,不报错) |

## 编译

```bash
xelatex demo.tex
xelatex demo.tex   # 第二遍:目录、总页数、目录密度自适应都靠它
```

- 必须用 **XeLaTeX**(主题会在其他引擎下直接报错提示)。Overleaf:Menu → Compiler → XeLaTeX。
- `booktabs` 已由主题加载并预设表格行距,无需手动配置。

## 一份文稿的全部写法

```latex
\documentclass[aspectratio=169,11pt,t]{beamer}   % t:帧内容顶对齐(推荐)
\usetheme{dragonai}                    % 选项:warm / fakebold / logozone / ppt

\title{标题(可用 \\ 断行)}
\subtitle{副标题}
\author{报告人}\institute{单位}\date{日期}

\begin{document}
\DAcover                               % 封面
\DAtoc                                 % 目录(可 \DAtoc[大纲];行距随章节数自适应)
\DAsection[红底质感语句]{章节标题}      % 章节页,语句可省略
\begin{frame}{页标题}{页副标题} ... \end{frame}   % 正文照常写,副标题可省
\DAclosing                             % 结尾(可 \DAclosing[谢谢聆听])
\end{document}
```

## 选项

| 选项 | 效果 |
|---|---|
| `warm` | 暖纸纸面 `#FAF7F2`(默认纯白) |
| `fakebold` | 算法加粗,替代真实 Bold 字重(精简 Linux/CI 用) |
| `logozone` | 恢复内页右上「标识 + 竖线 + 字标」区(v3.0 起默认关闭,内页品牌由页脚微字标承担;标题宽度自动随之调整) |
| `ppt` | **PPT 转换友好模式**:红底强调整套降级为红色粗体文字、微字去字距、素材图去边框、固定纯白底。正文强调全部转为可直接编辑的文本对象(品牌图形类小件除外),见下文「PPT 可编辑交付」 |

## 版式清单(刻意克制)

1. **封面** — `\DAcover`(眉头行 + 龙标光学对齐 + 衬线大标题 + 元信息栏)
2. **目录** — `\DAtoc`(等宽红色序号 + 衬线条目 + 细线;≤4 章疏朗 / 5–6 章收紧 / ≥7 章紧凑,两遍编译后自动生效)
3. **章节页** — `\DAsection[语句]{标题}`(白底 + 大号红色序号 + 红底质感语句)
4. **要点页** — `itemize`(红菱形一级项 / 细横线二级项,间距已预设)
5. **双栏 + 图** — `columns` + `\DAfigbox` 素材图或 `\DAfigureph` 占位
6. **图行** — `DAfigrow` 环境 + `\DAfigbox`(单图即居中,多图 `\hfill` 均布)
7. **数据页** — `DAstatstack` 纵排数据块(左栏数字说话、右栏放证据图)
8. **定理 / 公式** — `block`(菱形 + 细线)、`alertblock`(红底标签标题)
9. **表格** — `DAtable` / `DAtable*` 环境(居中 / 字号 / 行距已预设,可选表注;分组总表用 `\DAtablegroup` + `\DAtableno`)
10. **结尾** — `\DAclosing`(红块谢谢 + 联系行)

## 内容小件(单命令,零版式代码)

星号的统一读法:**星号 = 更收敛的变体**——`\DAtagline*` 说明变灰、`\DAfigbox*` 图注压进图宽、`DAtable*` 字号行距更紧。

```latex
\DAhot{7 个}                           % 行内红底强调(色块不可断行,长句用 \\ 让它独占一行)
\DAtag{重点}                            % 等宽小标签(alertblock 标题同款)
\DAtagline{当日产出}{说明}               % 标签行:红 tag + 说明(块的轻量替代;
                                        %   说明折行自动悬挂缩进,续行与说明起点对齐)
\DAtagline*{备注}{说明}                 % 星号 = 说明文字弱化为灰
\DAstatbox{$-92\,\%$}{三行业平均提升}   % 红底数据块 + 说明(说明折行同样悬挂缩进)

\begin{DAstatstack}[17mm]               % 数据块纵排:块间距自动;可选参数 =
  \DAstatbox{10 天}{从零基础到可交付}    %   数字块统一宽度,说明列自动对齐
  \DAstatbox{6 题}{真实客户业务}         %   (窄栏里多块一律纵排,并排必挤压说明)
\end{DAstatstack}

\DAfigbox{20mm}{fig.png}{图注}          % 素材图:细边框 + 等宽小图注(盒子取自然宽度,
                                        %   图注不折行;图注明显宽于图会把整盒撑宽)
\DAfigbox*{20mm}{fig.png}{图注}         % 星号 = 图注折行并压进图宽(拿不准用星号版)
\begin{DAfigrow}                        % 图行:单图即居中;多图 \hfill 均布
  \DAfigbox{20mm}{a.png}{甲}\hfill
  \DAfigbox{20mm}{b.png}{乙}\hfill
  \DAfigbox{20mm}{c.png}{丙}
\end{DAfigrow}
\DAframed{\includegraphics[height=20mm]{fig.png}}  % 无图注素材的细线裱框(收任意内容;
                                        %   横幅长图等单图场景也可用 width 定尺寸)
\DAfigureph[52mm]{架构图占位}           % 图占位框(可再给宽度:[26mm][40mm],
                                        %   默认整行;进图行并排时要给宽)

\begin{DAtable}[表注]{@{}rlll@{}}        % 三线表(\small,适合 ≤6 行)
  \toprule … \midrule … \bottomrule
\end{DAtable}
\begin{DAtable*}{@{}rlll@{}}             % 紧凑三线表(10 行量级的整页总表;
  \DAtablegroup{第一阶段 · …} \\          %   分组总表:组标题行(可选参数=列数,默认 4)
  \DAtableno{01} & … \\                  %   红色等宽行号(补零两位)
\end{DAtable*}                           % 表注建议放页副标题,表身保持干净
```

选择建议:≤6 行用 `DAtable`,整页总表用 `DAtable*`;一页里「要点 + 尾部结论行」用 `\DAtagline`,比 block 省一半竖向空间;**图行内的素材图一律用高度控制展示尺寸**,多图并排时基线自然齐平(`\DAfigbox` 高度必填,是有意逼你先做竖向预算;`\DAfigureph` 给默认值,因为占位框反正要换掉)。图行里的 `\hfill` 是「图行分隔符」惯用法——不做成自动注胶,是为了保留 `\quad`/`\hspace` 手动控距的自由。

## PPT 可编辑交付(双驱动范式)

需要交「可以在 PowerPoint 里继续改」的版本时,不要拿放映版 PDF 硬转——PDF 规范里没有「字符底色」概念,红底白字必然转成「矩形 + 文字」两个错位对象;等宽微字的 LetterSpace 字距会被转换器拆成逐字碎片。正解是**共享正文 + 两个驱动**:

```latex
% 正文抽成 body.tex(只有 \DAsection / frame / 组件,零版式代码)

% ---- main.tex(放映版,设计不妥协) ----
\documentclass[aspectratio=169,11pt,t]{beamer}
\usetheme{dragonai}
\title{...}\author{...}\date{...}
\begin{document}\input{body}\end{document}

% ---- main-ppt.tex(转换版,只差一个选项) ----
\documentclass[aspectratio=169,11pt,t]{beamer}
\usetheme[ppt]{dragonai}
\title{...}\author{...}\date{...}
\begin{document}\input{body}\end{document}
```

`ppt` 选项做的事:行内强调 / 标签 / 数据块 / 章节语句 / 结尾横幅全部降级为**红色粗体文字**(转出即单个可编辑文本,需要高亮时在 PowerPoint 里用原生「文本突出显示」一键补回)、微字去 LetterSpace、素材图去边框、固定纯白底。**显式例外**(保持原样,转出为形状对象):`\DAchop` 红章与 `\DAlogoplate` 标识底板是品牌图形,降级成文字即毁;`\DAfigureph` 占位框留边框反而醒目,交付版里本就不该有它。正文强调降级后大多更省空间,但【标签】与章节语句会比色块版略宽——转换版是独立成品,照常跑两遍编译、查一眼 overfull。

**字体防「平庸」**:转出的 PPT 只带字体名不带字体文件,目标机没装就回退等线/宋体。主题字体栈(思源宋体 / 思源黑体 / JetBrains Mono / Inter)全部是 OFL/Apache 许可、可自由分发——交付时附上字体安装包,先装字体再打开,并在 PPT「保存选项」里勾「在文件中嵌入字体」。

## 配图:素材与分辨率门禁

课件配图三条纪律(全部来自真实返工):

1. **分辨率门禁**:编译后跑 `python3 check_figs.py 你的文档.tex`。文字/图表/UI 类位图 ≥16 px/mm,照片/画作类 ≥12 px/mm,矢量 PDF 免检,豁免必须注明理由。修复只有两条路——**换更高清的源,或缩小展示尺寸;严禁上采样凑数**(插值放大 = 伪造像素,投影仪上一眼糊)。
2. **找高清源的固定姿势**:历史照片走 Wikimedia API 拿原图(手猜 URL 必 404);论文图用原 PDF 以 300–600 dpi 直渲裁剪;网页/工具界面用无头浏览器原生放大自截(小 UI 用宽视口 + 页面 zoom,窄视口高 zoom 会触发换行);数据图按主题色板用 matplotlib 重制成矢量 PDF。
3. **版权**:公共领域照片 / 论文图 / 工具截图可转引并注明出处;他人自绘的图表**不直接裁用**,只列重绘清单照着重画。

## 排版预算与排错速查(实战沉淀)

**竖向预算**:16:9 / 11pt / `t` 模式下,一页内容区约 **55mm**;页副标题占 ~5.5mm。三条 itemize + 一个 block + 一个 exampleblock 就会溢出——尾行改用 `\DAtagline`(省一半);图行高度 = 图高 + 图注行数 × ~3.5mm,排前先算。

**横向基准**:正文有效宽度 = `\DAcontentwidth`(默认边距下 132mm)。columns 里算配图宽度用它,别按纸宽 160mm 估。

**排错流程**:`xelatex` 两遍 → `grep -iE "overfull|error"` log(underfull badness 10000 的 `[] []` 空盒是 beamer 模板固有噪音,忽略)→ `pdftoppm -png` 逐页目检。CJK 断词、行尾 1–3 字孤行只能靠目检,删字或 `\newline` 收行。

**表格 Overfull 恒定不随删字变**:别猜是哪格,`\showboxbreadth=200 \showboxdepth=8` dump 盒子看真凶——实测最宽单元格往往是 Inter 英文串,目测估宽严重偏低。

**细节坑位**:
- `⊃` 等数学符号 CJK 字体缺字形,必须写 `$\supset$`
- 等宽单元格里 `--` 不合字,直接写单连字符;正文/标题里 `--` 会正常合成 –(主题已开 Ligatures=TeX)
- 全角冒号/分号贴拉丁字符会被 xeCJK 压缩到贴字,后补 `\,` 细空
- `\DAhot` 色块不可断行:行中后置容易产生「里/条:」类孤字,长句用 `\\` 让色块整行独占
- `\DAfigbox` 普通版图注不折行,明显长于图宽会把整盒撑宽、破坏 `\hfill` 均布——紧凑图行用星号版
- 竖版特例:beamer 内部载了 geometry,`\usetheme` 后 `\geometry{paperwidth=210mm,paperheight=297mm}` 直接得 A4 竖版,单 `[plain]` frame 手排,部件全可复用

## 可覆盖的配置

```latex
\renewcommand{\DAbrandcn}{你的品牌}              % 全局中文字标 —— 换品牌只改这四行
\renewcommand{\DAbranden}{YOUR BRAND}             % 全局英文字标
\renewcommand{\DAchoptext}{品\\牌}                % 红章两行文字
\renewcommand{\DAlogofile}{your-logo.png}         % 标识文件(缺失自动隐藏)
\renewcommand{\DAfootbrand}{…}                    % 页脚字样(默认由品牌拼出)
\renewcommand{\DAcontact}{联系方式}               % 结尾页联系行
\renewcommand{\DAauthorlabel}{主讲}               % 封面元信息标签(另有
                                                  %   \DAinstitutelabel \DAdatelabel)

\setlength{\DAcovertopskip}{4.5mm}                % 封面页眉行下移量(默认 4.5mm)
\setlength{\DAcoverlogoheight}{13mm}              % 封面龙标高度(默认 13mm,
                                                  %   按高度自动与眉头行光学对齐)
```

封面未设 `\subtitle` / `\institute` 时,对应行与标签自动省略;自设 `\titlegraphic` 时按原样放置(仅做 2mm 基线微调)。

其余部件(`\DAbar` 红杠、`\DAdiamond` 菱形、`\DAeyebrow` 眉头、`\DAchop` 红章、`\DAtelemetry` 遥测刻度线、`\DAlogozone` 标识区、`\DAlogoplate` 标识底板)均可在自定页面中直接复用。**注意:`\DAtelemetry` 只配数据/仪表语境,普通版面一律用素细线 `\hrule`,拿刻度线当装饰是败笔。**

- 长标题自动换行(无标识区时占满整行);章节、页码序号自动补零(01‑99);全文无需手写 `\vskip`。

## 字体

需要以下字体(Google Fonts 免费,全部 OFL/Apache 许可可再分发);缺失时自动回退(Google 版 → CJK 版 → 系统字体),两个变体都缺也只是观感降级,不会中断编译:

- **Noto Serif SC** — 标题衬线(回退 Noto Serif CJK SC)
- **Noto Sans SC** — 正文(回退 Noto Sans CJK SC;等宽场景的汉字同源)
- **Inter** — 拉丁正文(缺失用系统无衬线)
- **JetBrains Mono** — 等宽标注(回退 Menlo)

无独立 Bold 字重的环境用 `\usetheme[fakebold]{dragonai}`。

## 品牌约束(请保持)

- 红底白字只作块级强调(序号 / 语句 / 数据块 / 标签行 / 谢谢块),不做整页大面积填充
- 不用 emoji、不用大圆角、不用渐变底、无阴影
- 衬线只给标题;正文永远无衬线

## v3.2 变更(自 v3.1)

- 页标题分隔线到正文零附加间距:正文起点上移约 3mm,整页重心不再偏下(呼吸位由列表/段落自身顶距提供)
- 新增 `starter.tex` 模板骨架与《使用说明.md》:复制骨架改内容即可开写
- `\DAfigureph` 增加第二个可选参数(宽度,默认整行):占位框可进 `DAfigrow` 并排

## v3.1 变更(自 v3.0)

- 新选项 `ppt`:PPT 转换友好模式,配合共享正文双驱动,一个选项之差得「放映版 + 可编辑转换版」双成品
- 素材图组件 `\DAfigbox` / `\DAfigbox*`、图行 `DAfigrow`、细线裱框 `\DAframed` 入主题(此前需在文档序言自定义)
- 数据块纵排环境 `DAstatstack`;`\DAtagline` / `\DAstatbox` 说明折行自动悬挂缩进(此前折行顶破左缘)
- 目录行距按章节总数自适应(≤4 疏朗 / 5–6 收紧 / ≥7 紧凑),多章文稿无需再手工覆写 `section in toc`
- 新长度 `\DAcontentwidth` = 正文有效宽度;新增配图分辨率门禁脚本 `check_figs.py`
- README 增补「PPT 可编辑交付」「配图门禁」「排版预算与排错速查」三节实战经验
