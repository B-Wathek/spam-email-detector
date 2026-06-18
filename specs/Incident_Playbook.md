# Incident Response Playbook

## Scenario 1: Prompt Injection / Adversarial Email
### Description
Attacker sends crafted email designed to bypass spam detection.

### Detection
- Sudden drop in precision
- Increase in false negatives

### Response
- Block suspicious patterns
- Update preprocessing rules
- Retrain model with adversarial examples

### Recovery
- Rollback to last stable model
- Monitor metrics closely

---

## Scenario 2: Data Poisoning
### Description
Malicious data is inserted into training dataset.

### Detection
- Unusual distribution shifts
- Unexpected model behavior

### Response
- Audit dataset sources
- Remove suspicious samples
- Validate dataset integrity

### Recovery
- Retrain model on clean dataset
- Add stricter data validation pipeline

---

## Scenario 3: System or Pipeline Failure
### Description
Training or inference pipeline crashes or produces invalid outputs.

### Detection
- CI pipeline failure
- Missing or corrupted outputs

### Response
- Inspect logs
- Fix broken preprocessing or code

### Recovery
- Re-run pipeline
- Restore last working version
