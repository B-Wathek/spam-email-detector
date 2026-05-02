# Acceptance Criteria Table — Spam Email Detection AI Feature

This table defines measurable acceptance conditions for the system.  
Each scenario includes metric, threshold, tolerance, measurement method, and failure action.

---

| ID   | Scenario Type | Input Example                         | Metric              | Threshold        | Tolerance | Measurement Method     | Action on Fail                  |
|------|--------------|-------------------------------------|---------------------|------------------|----------|------------------------|---------------------------------|
| AC1  | Normal       | "Win a free iPhone now"             | Accuracy            | ≥ 0.90           | -0.02    | pytest + eval script   | Block release                  |
| AC2  | Normal       | "Meeting tomorrow at 10am"          | Precision (spam)    | ≥ 0.92           | -0.02    | evaluation report      | Block release                  |
| AC3  | Normal       | "Your invoice is attached"          | Recall (spam)       | ≥ 0.88           | -0.03    | eval dataset test      | Retrain model                 |
| AC4  | Edge         | Empty string ""                     | System stability    | No crash         | N/A      | unit test              | Fix preprocessing             |
| AC5  | Edge         | Very long email (10k words)         | Latency             | ≤ 200ms          | +50ms    | load benchmark (pytest)| Optimize vectorizer           |
| AC6  | Boundary     | confidence = 0.50                   | Output correctness  | "uncertain"      | ±0.05    | unit test              | Fix threshold logic           |
| AC7  | Negative     | null input                          | Error handling      | graceful fallback| N/A      | pytest exception test  | Add validation layer          |
| AC8  | Edge         | non-English text                    | Robustness          | ≥ 0.80 accuracy  | -0.05    | multilingual dataset   | Expand dataset                |
| AC9  | Load         | 100 requests/second                 | Throughput          | no failure       | N/A      | locust/load test       | Scale service                 |
| AC10 | Failure      | model missing                       | fallback behavior   | rule-based output| N/A      | CI simulation          | Implement fallback model      |

---

## Summary Rules

- All critical failures MUST block release
- Edge cases must not crash system
- Latency and accuracy are enforced in CI
- Fallback system must always activate on failure
