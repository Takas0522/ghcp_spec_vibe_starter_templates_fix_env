# Verification Report: `<Feature Name>`

- Verdict: `Pass | Pass with risk | Fail | Blocked`
- Verified on: `YYYY-MM-DD`
- Verifier: `<実装担当とは異なる担当を推奨>`
- Specification: `<../specs/feature-name.md>`
- Implementation plan: `<../plans/feature-name.md>`
- Revision: `<commit SHA or working-tree description>`

## Environment

- Operating system: `<name and version>`
- Runtime and tools: `<versions>`
- Configuration: `<relevant non-secret settings>`
- Test data: `<fixture、dataset、seed、version>`

## Results

| Requirement | Criterion | Command or procedure | Result | Evidence |
| --- | --- | --- | --- | --- |
| `REQ-###` | `AC-###` | `<exact command or numbered steps>` | `<Pass、Fail、Blocked>` | `<test name、log、artifact path>` |

## Failures

### `<短い失敗名>`

- Severity: `Critical | High | Medium | Low`
- Related criteria: `AC-###`
- Reproduction: `<最小の入力、状態、手順>`
- Expected: `<仕様上の結果>`
- Actual: `<観察した結果>`
- Evidence: `<ログ、スクリーンショット、失敗テスト>`

## Unverified Items

| Item | Reason | Residual risk | Follow-up owner |
| --- | --- | --- | --- |
| `<REQ/AC or scenario>` | `<未検証の理由>` | `<影響>` | `<担当>` |

## Traceability Summary

- Requirements defined: `<count>`
- Requirements with plan tasks: `<count>`
- Acceptance criteria defined: `<count>`
- Criteria passed: `<count>`
- Criteria failed or blocked: `<count>`
- Criteria without evidence: `<count>`

## Verdict Rationale

`<Pass、risk、Fail、Blocked を選んだ根拠。未検証事項を含める>`

完了宣言には、実行コマンド、テスト名、結果、残存リスクが必要です。コード
レビューだけで実行可能な受入条件を Pass にしないでください。
