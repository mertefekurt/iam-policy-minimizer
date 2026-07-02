from __future__ import annotations

from iam_policy_minimizer.models import Rule

PROJECT_NAME = 'iam-policy-minimizer'
SUMMARY = 'Find broad IAM policy statements before cloud access is merged.'
SAMPLE_RISK = 'Action * Resource * Effect Allow'
SAMPLE_CLEAN = 'Action s3:GetObject Resource arn:aws:s3:::reports/* Effect Review'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='wildcard-action',
        severity='high',
        pattern='Action\\s+\\*',
        message='wildcard action detected',
        recommendation='replace with explicit actions',
    ),
    Rule(
        code='wildcard-resource',
        severity='medium',
        pattern='Resource\\s+\\*',
        message='wildcard resource detected',
        recommendation='scope resources tightly',
    ),
    Rule(
        code='allow-effect',
        severity='low',
        pattern='Effect\\s+Allow',
        message='allow statement present',
        recommendation='verify this allow is required',
    ),
)
