# Release Checklist — Spam Email Detector

Before promoting a model to production, ALL conditions must be met:

## Model Quality
- Accuracy ≥ 0.85
- Precision ≥ 0.90
- Recall ≥ 0.85
- No regression > 2%

## Data Validation
- Data contract tests pass
- No schema violations
- No missing values

## Tests
- All pytest tests pass
- CI is green

## Evaluation
- metrics.json generated
- Meets thresholds in configs/thresholds.yaml

## Approval
- PR reviewed and approved
- Model version documented

## Deployment Safety
- Rollback plan ready
- Previous version available

## Final Decision
- [ ] APPROVED
- [ ] REJECTED
