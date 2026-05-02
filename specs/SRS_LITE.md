# SRS LITE — Spam Email Detection AI Feature

## 1. System Overview

This system classifies email text into:
- spam
- not_spam

It is designed as a lightweight AI feature with real-time inference and strict performance constraints.

---

## 2. Input Schema

### Request
```json id="input1"
{
  "text": "string (email content)"
}
