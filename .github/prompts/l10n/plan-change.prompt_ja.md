---
name: 'Plan Change'
description: '承認済み機能仕様から、コード編集なしで要件トレース済み実装計画を作成します。'
argument-hint: '承認済み機能仕様のパスを指定してください。'
agent: 'Plan'
tools: ['read', 'search']
---

# 変更計画

元仕様が承認済みかつ Ready であることを確認し、
タスク、依存関係、対象ファイル、disproving checks（反証チェック）、ロールバック、リスク、完全な REQ/AC マッピングを含む最小の実装計画を作成してください。
未解決の振る舞いがある場合は停止してください。
