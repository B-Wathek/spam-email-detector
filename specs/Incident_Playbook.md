# Incident Playbook

## Data Incident
- schema change
- missing values  
→ stop pipeline, fix data

## Model Incident
- accuracy drop  
→ rollback, retrain

## Infrastructure Incident
- latency high  
→ restart, scale, rollback

## Rollback Steps
1. switch to previous model
2. verify system
3. log incident

## Postmortem
update tests/specs
