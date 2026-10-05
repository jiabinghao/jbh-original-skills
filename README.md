# Original Skills

面向中文任务与 Codex 使用习惯的 15 个独立编写的 AI Agent 技能。版本：2.2.0。

这些技能是任务指令包，帮助代理更准确地选择流程、使用工具与核验成果。它们不是 15 款独立应用，不自动提供浏览器驱动、搜索服务或开发运行环境。

## 技能目录

| 技能 | 用途 |
| --- | --- |
| [skill-scout](skills/skill-scout/SKILL.md) · 技能选型助手 | 根据任务与环境筛选适合的技能，核对依赖许可并说明推荐理由 |
| [plan-probe](skills/plan-probe/SKILL.md) · 方案压力测试 | 检查方案关键假设与验证成本，形成可执行且可判断的下一步 |
| [context-check](skills/context-check/SKILL.md) · 项目上下文核对 | 核对方案文档与代码中的业务规则，定位冲突并形成修订建议 |
| [browser-workflow](skills/browser-workflow/SKILL.md) · 浏览器任务执行 | 通过已有浏览器工具执行网页任务，逐步核验保存后的真实结果 |
| [architecture-tune](skills/architecture-tune/SKILL.md) · 架构局部改进 | 从实际维护困难定位耦合边界，完成最小重构并验证行为兼容 |
| [behavior-tests](skills/behavior-tests/SKILL.md) · 行为测试先行 | 围绕用户行为编写失败测试，完成实现并留下真实的回归验证记录 |
| [interface-craft](skills/interface-craft/SKILL.md) · 界面设计与实现 | 围绕用户任务实现响应式界面，覆盖完整交互状态并检查关键路径 |
| [project-baseline](skills/project-baseline/SKILL.md) · 项目协作基线 | 盘点仓库约定和检查入口，补齐能够支持后续协作的最小文档 |
| [work-handoff](skills/work-handoff/SKILL.md) · 工作续接说明 | 将当前目标、已完成工作与剩余依赖整理成可核实的任务交接材料 |
| [issue-sort](skills/issue-sort/SKILL.md) · 问题与需求分流 | 依据影响和证据整理错误报告与功能请求，给出优先级和就绪判断 |
| [prototype-lab](skills/prototype-lab/SKILL.md) · 原型验证 | 构建能回答关键未知的小型可运行原型，记录观测证据与继续条件 |
| [decision-map](skills/decision-map/SKILL.md) · 决策依赖审查 | 比较相互依赖的方案选择，梳理条件分支、撤回代价和承诺顺序 |
| [video-build-flow](skills/video-build-flow/SKILL.md) · 视频构建流程 | 通过现有 HyperFrames 工具预览、检查与渲染项目，核验视频规格和关键片段 |
| [react-perf-tune](skills/react-perf-tune/说明.md) · React 性能改进 | 定位 React 与 Next.js 的实际性能瓶颈，完成局部优化并比较相同场景的前后结果 |
| [learning-path](skills/learning-path/说明.md) · 学习路径与练习 | 围绕可展示的学习目标安排讲解与练习，根据实际作答调整难度并记录后续学习路径 |

每项技能的输入、输出、示例请求及能力边界见 [完整中文说明](docs/SKILLS.md)。

## 设计来源与原创边界

2026-10-04 在 [SkillForge 首页](https://skills.yangsir.net/)选择“安装量”排序，取页面显示的前十项作为**主题参考**。用户提供的 [trending 页面](https://skills.yangsir.net/trending)按增长量排序，不能当作总安装量榜；该页当天同时显示对比日期 2026-09-27 → 2026-10-04，因此本仓库不声称验证了其“24 小时”统计口径。

2026-10-05 再按首页总安装量排序，排除已参考的前十项，新增剩余前三个主题：prototype、grilling、hyperframes-cli，页面总排名分别为 11、12、13。采样时网站最近更新标记仍为 10-04；数字代表第三方安装量显示值，不是实际使用人数。原有十项保留首次采样记录，新增三项单独记录本次日期。

2026-10-05 将先前本地技能清单中的前五项按顺序发布到本仓库。本批参考主题对应保存的安装量快照第 14—18 位；沿用独立编写的名称、指令、元数据、中文说明和许可。记录的是先前采样事实，不代表重新验证了网站当前排名。

采用新的名称、中文表达和针对实际任务的执行规则，未引入所选技能的入口正文、代码、模板、图片或软件实现。浏览榜单时只将名称、作者、链接、约数与功能方向作为选题信息；这些引用不表示原作者参与或认可本项目。

详细映射见 [来源与许可记录](docs/PROVENANCE.md)。安装量是第三方页面的显示值，未独立验证，不能用于承诺效果。这里的实现也不保证与参考技能具有相同能力。

MIT 许可适用于本仓库可许可的内容。AI 辅助生成不等于取得了第三方权利，也不意味着能够保证绝对无侵权风险或在所有法域取得专有版权。未来引入外部资源时必须单独核对许可。

## 在 Codex 中安装

先克隆本仓库：

```powershell
git clone https://github.com/jiabinghao/jbh-original-skills.git original-skills
Set-Location original-skills
```

检查将写入的路径，再安装。脚本默认使用 CODEX_HOME 下的 skills 目录；未设置时使用用户目录中的 .codex/skills。

```powershell
.\scripts\install.ps1 -WhatIf
.\scripts\install.ps1
```

只安装一个技能：

```powershell
.\scripts\install.ps1 -Skill prototype-lab
```

指定其他技能目录：

```powershell
.\scripts\install.ps1 -Destination 'D:\my-agent\skills' -Skill plan-probe
```

脚本只复制技能目录，保留每个目录中的 LICENSE，默认遇到同名目录即停止，不覆盖已有技能。也可以手动复制所需目录。安装后重新打开或刷新 Codex 技能发现环境；实际加载方式取决于当前客户端。在新聊天中输入 `$work-handoff` 等名称即可显式调用，未禁用平台支持的自动选择。

其他遵循 SKILL.md 约定的代理可按其自身说明放置技能目录；本版本未验证所有平台的发现机制。

## 本地检查

检查工具只需要 Python 3.10+，没有第三方依赖：

```powershell
python .\scripts\validate.py
```

它检查目录、元数据、引用、每个技能的许可及安装包完整性。仓库同时配置 GitHub Actions 执行该检查。检查通过证明结构一致，不能替代真实任务验证，也不是法律鉴定。

## 个性化维护

修改目标技能的 SKILL.md 中具体决策规则；变更发现范围时同步更新 description、agents/openai.yaml、catalog.json 及中文说明。优先记录个人工作中可复用的实际需求，避免增加泛化口号或复制他人正文。

[LICENSE](LICENSE) · [验证范围](docs/VALIDATION.md)
