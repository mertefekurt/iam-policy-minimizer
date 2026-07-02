# iam-policy-minimizer

> Find broad IAM policy statements before cloud access is merged.

## Review card Overview

Find broad IAM policy statements before cloud access is merged. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts IAM policy snippet. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
iam-policy-minimizer examples/sample.txt
iam-policy-minimizer examples/sample.txt --json --fail-on medium
python -m iam_policy_minimizer --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `wildcard-action` | high | wildcard action detected |
| `wildcard-resource` | medium | wildcard resource detected |
| `allow-effect` | low | allow statement present |

## Validation Notes

```bash
ruff check .
pytest
python -m iam_policy_minimizer --help
```

Example risky input:

```text
Action * Resource * Effect Allow
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
