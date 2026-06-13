# Security Policy

## About This Project

`cloudpulse-ai` is an **infrastructure observability tool** developed by Merkaba AI Risk Management. It accesses live CloudWatch telemetry and processes it using LLMs.

## Reporting a Vulnerability

If you discover a security vulnerability — including prompt injection risks in the query parser or excessive IAM permissions in the deployment templates — please report it to:

**Email:** security@merkabacreatives.org
**Subject line:** `[SECURITY] cloudpulse-ai — <brief description>`

We will acknowledge receipt within 48 hours.

## Security Design Notes

- Telemetry data is analyzed entirely within the AWS ecosystem using Amazon Bedrock.
- IAM roles are strictly read-only for CloudWatch data.
