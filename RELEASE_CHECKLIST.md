# Release Checklist — Spam Email Detector

## Model Quality
- Accuracy ≥ 0.85
- Precision ≥ 0.90
- Recall ≥ 0.85
- No regression > 2%

## Data Validation
- Data contract tests pass
- No missing values
- Schema valid

## Tests
- All pytest tests pass
- CI is green

## Evaluation
- metrics.json generated
- Meets thresholds.yaml

## Deployment Safety
- Rollback plan ready
- Previous model available

## Approval
- PR reviewed

## Decision
- [ ] APPROVED
- [ ] REJECTED
