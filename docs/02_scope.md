# Scope Definition

## In Scope

| Capability or scenario | Intended evidence | Priority |
| --- | --- | --- |
| `<今回扱う機能または利用場面>` | `<デモ、テスト、計測値>` | `<Must、Should、Could>` |

## Out of Scope

| Excluded item | Reason | Revisit condition |
| --- | --- | --- |
| `<意図的に扱わない事項>` | `<今回除外する理由>` | `<再検討する条件>` |

Out of scope の項目は、暗黙に実装へ追加しません。必要になった場合は仕様を
更新し、人間の承認を得ます。

## Constraints

- Timebox: `<期間または終了条件>`
- Budget and people: `<利用可能な資源>`
- Required platforms: `<必須の環境、製品、規格>`
- Data restrictions: `<機密性、保持、利用許諾>`

## Assumptions

| ID | Assumption | Validation method | Owner |
| --- | --- | --- | --- |
| `ASM-001` | `<事実として未確認の前提>` | `<確認方法>` | `<担当>` |

前提が崩れた場合に要求やアーキテクチャが変わるなら、実装前に確認します。

## Non-Functional Boundaries

| Quality | Required boundary | Deferred work |
| --- | --- | --- |
| Security | `<認証、認可、データ境界>` | `<今回扱わない強化>` |
| Reliability | `<許容する失敗と回復>` | `<本番向け要件>` |
| Performance | `<検証に必要な閾値>` | `<大規模最適化>` |
| Accessibility | `<対象基準>` | `<除外があれば理由>` |

## Open Questions

- [ ] `<スコープを変え得る未解決事項>`

## Approval

- Status: `Draft | Approved | Superseded`
- Owner: `<意思決定者>`
- Reviewed on: `YYYY-MM-DD`
