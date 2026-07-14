# Experiment Log

この台帳は append-only です。過去の結果を書き換えず、訂正は新しい実験
または注記として追記します。一度に変更する主要変数は一つにします。

## EXP-001: `<実験名>`

- Status: `Planned | Running | Concluded | Abandoned`
- Date: `YYYY-MM-DD`
- Owner: `<担当者>`
- Related hypothesis: `HYP-###`
- Related requirements: `REQ-###`

### Hypothesis

`<変更>` を行うと、`<条件>` において `<測定値>` が `<期待値>` になる。

### Method

- Baseline: `<比較対象と測定値>`
- Changed variable: `<今回だけ変更する項目>`
- Controlled conditions: `<固定するデータ、環境、手順>`
- Dataset or inputs: `<版、件数、生成方法、参照先>`
- Reproduction command: `<実行可能なコマンドまたは手順>`
- Success threshold: `<継続判断に使う閾値>`

### Result

- Observed value: `<実測値>`
- Evidence: `<ログ、レポート、スクリーンショットへのリンク>`
- Deviations: `<計画から変わった条件>`

### Conclusion

- Verdict: `Adopt | Iterate | Reject | Inconclusive`
- Learning: `<結果から支持できること。推測は区別する>`
- Next action: `<仕様、計画、ADR、次の EXP へのリンク>`
