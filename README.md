![IAM Policy Minimizer cover](assets/readme-cover.svg)

# IAM Policy Minimizer

> Find broad IAM policy statements before cloud access is merged

This is a review desk for cloud security. The useful part is not a dashboard; it is the tiny repeatable moment where vague records become specific findings.

## Finding catalog for `iam-policy-minimizer`

| Finding | Level | Why it matters |
| --- | --- | --- |
| `wildcard-action` | high | wildcard action detected |
| `wildcard-resource` | medium | wildcard resource detected |
| `allow-effect` | low | allow statement present |

## Try the sample

```bash
git clone https://github.com/mertefekurt/iam-policy-minimizer.git
cd iam-policy-minimizer
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

```bash
iam-policy-minimizer examples/sample.txt
iam-policy-minimizer examples/sample.txt --json
```

## Reading the output

- Markdown is meant for humans reviewing a change.
- JSON is meant for CI, scripts, or saved reports.
- `--fail-on` lets the repo decide how strict a gate should be.
