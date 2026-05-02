# DataSpec — Spam Email Detection Dataset

## 1. Purpose
This dataset is used to train and evaluate a spam email classification model.

---

## 2. Data Source
- Synthetic + public spam email samples
- Manually labeled for training/testing

---

## 3. Schema

| Field | Type   | Description            |
|------|--------|------------------------|
| text | string | Email content          |
| label | int   | 0 = not_spam, 1 = spam |

---

## 4. Data Quality Rules

- No missing values allowed
- Text must be UTF-8 encoded
- No empty strings
- Labels must be binary (0 or 1)

---

## 5. Versioning
Dataset version: v1.0

Stored under `/data/spam.csv`
