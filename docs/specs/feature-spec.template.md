# Feature Specification: `<Feature Name>`

- Status: `Draft | Approved | Superseded`
- Owner: `<仕様責任者>`
- Approver: `<承認者>`
- Approved on: `YYYY-MM-DD | Not approved`
- Related vision: [Product Vision](../01_vision.md)
- Related scope: [Scope Definition](../02_scope.md)

## Problem and Outcome

`<誰が、どの状況で、何に困っているか。この機能で観察したい成果>`

## User Scenarios

### Scenario 1: `<短い名前>`

- Given: `<開始状態と前提>`
- When: `<ユーザーまたはシステムの操作>`
- Then: `<外部から観察できる結果>`

## Requirements

### REQ-001: `<要求の短い名前>`

`<システムが提供する振る舞い。実装方法ではなく観察可能な能力を記述>`

- Priority: `Must | Should | Could`
- Source: `<ユーザーシナリオ、法令、制約、実験へのリンク>`
- Status: `Proposed | Accepted | Deprecated`

#### Acceptance Criteria

- `AC-001`: Given `<状態>`, when `<操作>`, then `<観察可能な結果>`.
- `AC-002`: Given `<境界または失敗条件>`, when `<操作>`, then `<結果>`.

## Edge and Failure Cases

| Case | Expected behavior | Related criteria |
| --- | --- | --- |
| `<空、上限、不正入力、依存障害など>` | `<外部から観察できる結果>` | `AC-###` |

## Non-Functional Requirements

| ID | Quality | Measurable boundary | Verification method |
| --- | --- | --- | --- |
| `REQ-002` | `<security/performance/etc.>` | `<条件と閾値>` | `<test、review、measurement>` |

## Dependencies

- `<外部サービス、データ、先行要求、ADR へのリンク>`

## Out of Scope

- `<意図的に実装しない振る舞いと理由>`

## Open Questions

- [ ] `[NEEDS CLARIFICATION] <回答により振る舞いが変わる質問>`

## Traceability

| Requirement | Acceptance criteria | Planned task | Verification evidence |
| --- | --- | --- | --- |
| `REQ-001` | `AC-001`, `AC-002` | `<plan link after approval>` | `<verification link after implementation>` |

## Approval Checklist

- [ ] 全要求がテスト可能である。
- [ ] すべての `AC-###` が要求に関連付いている。
- [ ] 境界、失敗、非機能要件が十分に定義されている。
- [ ] スコープを変え得る未解決事項がない。
- [ ] 人間の承認者が Status を `Approved` にした。
