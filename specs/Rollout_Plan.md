# Rollout Plan (Canary)

## Strategy
Canary deployment

## Traffic Split
- 90% old model
- 10% new model

## Observation
- 24 hours

## Metrics
- accuracy proxy
- latency
- error rate

## Rollback Triggers
- Accuracy drop > 2%
- Latency > 300ms
- Error rate > 5%

## Rollback
Switch traffic back to old model immediately
