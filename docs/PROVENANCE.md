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
| 1 | [find-skills](https://skills.yangsir.net/skill/find-skills) | @vercel-labs | 3.7M | [jbh-skill-scout](../skills/jbh-skill-scout/SKILL.md) |
| 2 | [grill-me](https://skills.yangsir.net/skill/sm3-grill-me) | @mattpocock | 1.3M | [jbh-plan-probe](../skills/jbh-plan-probe/SKILL.md) |
| 3 | [grill-with-docs](https://skills.yangsir.net/skill/gh-grill-with-docs) | @mattpocock | 1.1M | [jbh-context-check](../skills/jbh-context-check/SKILL.md) |
| 4 | [agent-browser](https://skills.yangsir.net/skill/agent-browser) | @vercel-labs | 1.0M | [jbh-browser-workflow](../skills/jbh-browser-workflow/SKILL.md) |
| 5 | [improve-codebase-architecture](https://skills.yangsir.net/skill/sm3-improve-codebase-architecture) | @mattpocock | 1.0M | [jbh-architecture-tune](../skills/jbh-architecture-tune/SKILL.md) |
| 6 | [tdd](https://skills.yangsir.net/skill/ssh2-tdd) | @mattpocock | 1.0M | [jbh-behavior-tests](../skills/jbh-behavior-tests/SKILL.md) |
| 7 | [frontend-design](https://skills.yangsir.net/skill/frontend-design-anthropic) | @anthropics | 950.1K | [jbh-interface-craft](../skills/jbh-interface-craft/SKILL.md) |
| 8 | [setup-matt-pocock-skills](https://skills.yangsir.net/skill/gh-setup-matt-pocock-skills) | @mattpocock | 932.4K | [jbh-project-baseline](../skills/jbh-project-baseline/SKILL.md) |
| 9 | [handoff](https://skills.yangsir.net/skill/gh-handoff) | @mattpocock | 910.5K | [jbh-work-handoff](../skills/jbh-work-handoff/SKILL.md) |
| 10 | [triage](https://skills.yangsir.net/skill/gh-triage) | @mattpocock | 880.8K | [jbh-issue-sort](../skills/jbh-issue-sort/SKILL.md) |

## 已采用的独立实现方法

围绕任务目的从零编写中文指令，采用 JBH 命名；指令、界面元数据、安装和校验脚本均在本次任务中生成。没有下载或引入所选技能的 SKILL.md、脚本、资产或模板。参考关系仅用于解释选题，不表示移植、兼容全部功能或原作者背书。

技能结构使用通行的 SKILL.md + YAML 元数据约定。MIT 许可使用标准许可文本；除此之外没有打包第三方实现。现有 skill-creator 用作制作指导和本地校验，其文件和校验器源码没有复制进此仓库。

## 许可与权利边界

本仓库及每个可单独安装的技能目录附带 MIT LICENSE，许可人标为仓库维护者 jiabinghao，适用范围限于维护者有权许可的内容。公开仓库及新名称不会自动消除第三方权利。

[WIPO 的版权说明](https://www.wipo.int/en/web/copyright/protection)区分思想、操作方法与具体表达：本项目选择功能主题并独立写作的原因在于避免复制受保护表达，而不是通过改名认领原作品。引用来源也不等于获得转载许可。

内容由 AI 辅助生成，未进行跨全网的相似性鉴定或取得律师意见。[美国版权局的 AI 输出说明](https://www.copyright.gov/newsnet/2025/1060.html)强调足够的人类创作表达对该法域的版权保护具有意义；不能据此推断其他法域，也不能保证这批内容具有专有版权或绝对不存在争议。

后续如引入外部素材、代码或文档，应记录准确版本、原始来源、许可证、保留通知的方式和是否修改。没有许可时不要把公开可见等同于可重新发布。对品牌标识、专利和平台使用条款应另行判断，MIT 不授予第三方权利。
