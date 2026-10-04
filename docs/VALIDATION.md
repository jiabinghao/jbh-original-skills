# 验证范围

本文件区分结构检查、工具运行和真实任务效果，不把其混为同一个“通过”。

## 可重复的检查

```powershell
python scripts/validate.py
python -m unittest discover -s tests -v
```

前者检查十个目录、入口文件、界面元数据、catalog.json、MIT 许可及本地文档引用；后者检查正确安装包、损坏引用的拒绝、安装预演无写入、单技能安装完整性和同名冲突时不覆盖且不产生部分安装。

这些检查只使用合成的临时目录，没有安装到真实 Codex 技能目录，也不访问生产服务。

## 技能行为检查

创建时对每项技能的发现范围、输入输出、工具前提、任务授权与完成证据作了人工式内容核对。SKILL.md 还使用当前环境的 skill-creator quick_validate.py 执行结构检查。该外部校验器不随包分发。

没有运行十项真实业务场景的独立代理评测，未声称获得准确率或效率提升指标。浏览器技能没有浏览器驱动；测试技能没有测试运行器；前端技能没有自带渲染环境。它们调用代理平台现有工具。

## 首次发布本地结果

2026-10-04 在 Windows、Python 3.12.6、PowerShell 7.6.5 下执行：

- 十个技能均通过当前环境 skill-creator 的 quick_validate.py。
- 本仓库 validate.py 通过，十个入口、元数据、许可及本地引用一致。
- unittest 的五项安装与打包检查全部通过，没有跳过项。

GitHub Actions 的结果以仓库 Actions 页面为准；本地通过不能替代远程运行结果。尚未验证 Windows PowerShell 5.1 或其他代理平台。
