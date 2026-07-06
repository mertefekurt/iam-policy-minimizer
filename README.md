# IAM Policy Minimizer

![IAM Policy Minimizer cover](assets/readme-cover.svg)

> Find broad IAM policy statements before cloud access is merged

![stack](https://img.shields.io/badge/stack-Python-16a34a?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-dc2626?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-7c3aed?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-0891b2?style=flat-square)

## At a glance

| Area | Detail |
| --- | --- |
| Focus | cloud security |
| Command | `iam-policy-minimizer` |
| Formats | text, JSON, JSONL, CSV |
| Output | Markdown table or JSON |

## What it checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `wildcard-action` | high | wildcard action detected |
| `wildcard-resource` | medium | wildcard resource detected |
| `allow-effect` | low | allow statement present |

## Try it locally

```bash
python -m pip install -e ".[dev]"
iam-policy-minimizer examples/sample.txt
iam-policy-minimizer examples/sample.txt --json --fail-on medium
```

## Notes from the code

`rules.py` keeps the project policy explicit, while `core.py` handles parsing and report rendering. The CLI stays thin on purpose so the checks are easy to test.

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m iam_policy_minimizer --help
```
