---
name: 'Verify Change'
description: '承認済みのすべての要件と受け入れ基準に対して実装を独立検証し、再現可能な証拠を作成します。'
argument-hint: '仕様、承認済み計画、リビジョン、環境を指定してください。'
agent: 'Verify'
tools: ['read', 'search', 'execute']
---

# 変更検証

完全な REQ/AC カバレッジマトリクスを構築し、文書化されたチェックを実行し、
指定された境界・失敗振る舞いを検証して、Pass、Pass with risk、Fail、または Blocked の判定を含む検証レポートを作成してください。
実装は編集しないでください。
