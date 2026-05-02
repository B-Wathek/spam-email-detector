# DataContract — Spam Email Dataset

## 1. Contract Definition

This contract ensures dataset correctness before training or evaluation.

---

## 2. Valid Data Rules

### Syntactic Rules
- text must be string
- text must not be empty
- no corrupted rows

---

### Structural Rules
- No duplicate rows
- No label leakage (no label inside text)
- Each row must have both text and label

---

### Statistical Rules
- Spam ratio must be between 20% and 80%
- No single source dominates > 70%
- Text length distribution must be stable
