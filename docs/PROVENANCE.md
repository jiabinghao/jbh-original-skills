# 来源、许可与创建方式

## 选题记录

- 采样日期：2026-10-04（Asia/Shanghai）。
- 聚合站：[SkillForge](https://skills.yangsir.net/)。
- 操作：在首页“热门 Skill”区域选择“安装量”，读取排序后的前十项。
- 数字：页面显示的约数；同一约数内的先后采用页面顺序，不推测精确差值。
- 范围：记录页面名称、作者、链接、安装量约数及抽象功能方向，不归档网站描述全文或原技能正文。
- 原仓库许可证：本批实现未复用原仓库材料，因此未以任何原仓库许可证授权本仓库；也未开展原仓库全部文件的许可审计。

| 页面顺序 | 参考技能 | 页面作者 | 显示安装量 | 本仓库独立实现 |
| --- | --- | --- | --- | --- |
| 1 | [find-skills](https://skills.yangsir.net/skill/find-skills) | @vercel-labs | 3.7M | [skill-scout](../skills/skill-scout/SKILL.md) |
| 2 | [grill-me](https://skills.yangsir.net/skill/sm3-grill-me) | @mattpocock | 1.3M | [plan-probe](../skills/plan-probe/SKILL.md) |
| 3 | [grill-with-docs](https://skills.yangsir.net/skill/gh-grill-with-docs) | @mattpocock | 1.1M | [context-check](../skills/context-check/SKILL.md) |
| 4 | [agent-browser](https://skills.yangsir.net/skill/agent-browser) | @vercel-labs | 1.0M | [browser-workflow](../skills/browser-workflow/SKILL.md) |
| 5 | [improve-codebase-architecture](https://skills.yangsir.net/skill/sm3-improve-codebase-architecture) | @mattpocock | 1.0M | [architecture-tune](../skills/architecture-tune/SKILL.md) |
| 6 | [tdd](https://skills.yangsir.net/skill/ssh2-tdd) | @mattpocock | 1.0M | [behavior-tests](../skills/behavior-tests/SKILL.md) |
| 7 | [frontend-design](https://skills.yangsir.net/skill/frontend-design-anthropic) | @anthropics | 950.1K | [interface-craft](../skills/interface-craft/SKILL.md) |
| 8 | [setup-matt-pocock-skills](https://skills.yangsir.net/skill/gh-setup-matt-pocock-skills) | @mattpocock | 932.4K | [project-baseline](../skills/project-baseline/SKILL.md) |
| 9 | [handoff](https://skills.yangsir.net/skill/gh-handoff) | @mattpocock | 910.5K | [work-handoff](../skills/work-handoff/SKILL.md) |
| 10 | [triage](https://skills.yangsir.net/skill/gh-triage) | @mattpocock | 880.8K | [issue-sort](../skills/issue-sort/SKILL.md) |

## 第二批选题记录：2026-10-05

重新打开用户提供的 [trending](https://skills.yangsir.net/trending) 和首页，按首页“安装量”排序核对已有参考项。trending 按增长量排序，其比较日期显示 2026-09-27 → 2026-10-05；不据此认定为严格的 24 小时数据。首页最近更新标记仍为 10-04。

排除上表十项后，剩余安装量最高的三项如下。这里“用得最多”采用聚合站总安装量这一可观察的代理指标，不能推断真实使用次数、活跃人数或技能质量。数字未独立审计；同主题的新指令不承诺等同于原技能。

| 总排名 | 剩余排名 | 参考技能 | 页面作者 | 显示安装量 | 本仓库独立实现 |
| --- | --- | --- | --- | --- | --- |
| 11 | 1 | [prototype](https://skills.yangsir.net/skill/gh-prototype) | @mattpocock | 877.5K | [prototype-lab](../skills/prototype-lab/SKILL.md) |
| 12 | 2 | [grilling](https://skills.yangsir.net/skill/gh-grilling) | @mattpocock | 825.6K | [decision-map](../skills/decision-map/SKILL.md) |
| 13 | 3 | [hyperframes-cli](https://skills.yangsir.net/skill/daily-hyperframes-cli) | @heygen-com | 779.5K | [video-build-flow](../skills/video-build-flow/SKILL.md) |

原型技能围绕实验问题和运行证据重新设计；决策技能围绕条件依赖与承诺顺序编写；视频技能围绕版本核对、时间采样和成片核验编写。未读取或复制这三项原技能的 SKILL.md 正文、脚本或模板，也未将原技能换名后发布。

视频技能的外部工具知识核对使用 [HyperFrames 官方 CLI 文档](https://github.com/heygen-com/hyperframes/blob/main/docs/developers/cli.mdx)、[官方项目](https://github.com/heygen-com/hyperframes)和 [HeyGen 环境说明](https://help.heygen.com/en/articles/15001510-hyperframes-x-heygen)。仅整理必要命令标识和运行前提，不打包第三方文档正文或软件。查阅时该工具采用 Apache-2.0；本仓库 MIT 许可不授予其代码或素材的权利。

## 已采用的独立实现方法

围绕任务目的从零编写中文指令，采用按功能描述的中性命名；指令、界面元数据、安装和校验脚本均在本次任务中生成。没有下载或引入所选技能的 SKILL.md、脚本、资产或模板。参考关系仅用于解释选题，不表示移植、兼容全部功能或原作者背书。

技能结构使用通行的 SKILL.md + YAML 元数据约定。MIT 许可使用标准许可文本；除此之外没有打包第三方实现。现有 skill-creator 用作制作指导和本地校验，其文件和校验器源码没有复制进此仓库。

## 许可与权利边界

本仓库及每个可单独安装的技能目录附带 MIT LICENSE，版权署名采用中性的“The skill authors”，适用范围限于维护者有权许可的内容。公开仓库及新名称不会自动消除第三方权利。

[WIPO 的版权说明](https://www.wipo.int/en/web/copyright/protection)区分思想、操作方法与具体表达：本项目选择功能主题并独立写作的原因在于避免复制受保护表达，而不是通过改名认领原作品。引用来源也不等于获得转载许可。

内容由 AI 辅助生成，未进行跨全网的相似性鉴定或取得律师意见。[美国版权局的 AI 输出说明](https://www.copyright.gov/newsnet/2025/1060.html)强调足够的人类创作表达对该法域的版权保护具有意义；不能据此推断其他法域，也不能保证这批内容具有专有版权或绝对不存在争议。

后续如引入外部素材、代码或文档，应记录准确版本、原始来源、许可证、保留通知的方式和是否修改。没有许可时不要把公开可见等同于可重新发布。对品牌标识、专利和平台使用条款应另行判断，MIT 不授予第三方权利。
