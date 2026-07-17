# Implementation Plan: `<Feature Name>`

- Status: `Draft | Approved | Completed | Superseded`
- Owner: `<計画責任者>`
- Approver: `<承認者>`
- Approved on: `YYYY-MM-DD | Not approved`
- Source specification: `<../specs/feature-name.md>`
- Architecture and decisions: `<関連リンク>`

## Summary

`<承認済み仕様を満たすための最小アプローチと、採用理由>`

## Impact Analysis

| Area | Current behavior | Required change | Risk |
| --- | --- | --- | --- |
| `<module/interface/data>` | `<現状>` | `<変更後>` | `<low/medium/high and why>` |

## Implementation Tasks

### TASK-001: `<動詞で始める短い名前>`

- Requirements: `REQ-###`
- Acceptance criteria: `AC-###`
- Depends on: `None | TASK-###`
- Files: `<アプリケーションのソースコードは /src 配下。新規、更新、削除を区別>`
- Change: `<実装する振る舞いと境界>`
- Disproving check: `<変更直後に実行する最小テストまたはコマンド>`
- Done when: `<観察可能な完了条件>`

## Verification Strategy

| Acceptance criterion | Test level | Command or procedure | Expected evidence |
| --- | --- | --- | --- |
| `AC-###` | `<unit/integration/e2e/review>` | `<command or steps>` | `<test name、log、artifact>` |

## Migration and Rollback

- Migration: `<データ、設定、互換性への対応。不要なら None>`
- Rollback: `<安全に戻す方法と判断条件>`

## Risks and Open Questions

| Risk or question | Impact | Mitigation or owner |
| --- | --- | --- |
| `<内容>` | `<影響>` | `<対策または回答者>` |

## Requirement Mapping

| Requirement | Plan tasks | Acceptance criteria | Verification |
| --- | --- | --- | --- |
| `REQ-###` | `TASK-###` | `AC-###` | `<verification row or report link>` |

## Definition of Done

- [ ] すべての計画タスクが承認済み仕様へ対応している。
- [ ] アプリケーションのソースコードが `/src` 配下に配置されている。
- [ ] 各 `AC-###` に実行可能な検証方法がある。
- [ ] 対象チェックと必要な回帰テストが成功している。
- [ ] 変更ファイル、テスト、証跡が Requirement Mapping に反映されている。
- [ ] 残存リスクと未検証事項が明記されている。
- [ ] 必要な ADR または EXP が更新されている。
