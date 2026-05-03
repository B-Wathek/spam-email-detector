# Monitoring Spec

## Service Health
- latency < 200ms
- error rate < 5%

## Data Drift
- spam ratio change
- text length distribution

## Model Quality Proxy
- prediction distribution

## Cost
- request rate

---

## Alerts

| Metric | Threshold | Action |
|--------|----------|--------|
| Latency | >300ms | investigate |
| Error rate | >5% | rollback |
| Drift | detected | retrain |
