# CloudPulse AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AWS](https://img.shields.io/badge/AWS-Bedrock%20%7C%20CloudWatch-orange.svg)](https://aws.amazon.com/)
[![Security](https://img.shields.io/badge/security-infrastructure--observability-red.svg)](https://github.com/ojackson08/cloudpulse-ai)
[![Maintained by Merkaba AI Risk](https://img.shields.io/badge/maintained%20by-Merkaba%20AI%20Risk-blueviolet)](https://merkabacreatives.org/ai-risk)

**Natural language observability for AWS — Ask your infrastructure anything in plain English.**

---

## Overview

CloudPulse AI is an observability tool that fetches live AWS CloudWatch telemetry and uses Amazon Bedrock (Claude 3) to diagnose incidents and surface root causes in seconds. Instead of writing complex CloudWatch Insights queries or manually correlating metrics across dashboards, engineers can ask plain English questions like, "Why did the API Gateway latency spike at 3 PM?" and receive an AI-generated root cause analysis based on live telemetry data.

At Merkaba AI Risk Management, this tool is used for rapid incident response and infrastructure security investigations.

---

## Architecture

```
User (Natural Language Query)
    │
    ▼
Lambda (Query Parser)
    │
    ├── Translate query → CloudWatch Metric/Log filters
    │
    ├── Fetch live telemetry data (Boto3)
    │
    ▼
Amazon Bedrock (Claude 3)
    │
    └── Analyze telemetry + correlate events
    │
    ▼
Return Root Cause Analysis to User
```

---

## Security Properties

| Property | Implementation |
|---|---|
| **Data Privacy** | Telemetry is processed within the AWS boundary via Bedrock; no data sent to third-party APIs |
| **Access Control** | Lambda execution role strictly scoped to read-only CloudWatch access |
| **Audit Trail** | All AI queries and responses are logged via CloudTrail |
| **Network Security** | Bedrock API calls route through AWS PrivateLink |

---

## Case Study / Usage Notes

**Deployment at Merkaba AI Risk Management:**

During an internal security incident involving a suspected DDoS attack on an agent orchestration endpoint, CloudPulse AI was used to rapidly correlate WAF logs, ALB metrics, and Lambda concurrency limits. By asking "Summarize the traffic patterns from the top 5 IP addresses over the last hour," the response team identified the attack vector in 45 seconds, allowing them to deploy a WAF blocking rule 15 minutes faster than standard manual log analysis.

---

## Integration with Merkaba Security Stack

- [`aws-observability-alerting`](https://github.com/ojackson08/aws-observability-alerting) — Complements AI analysis with deterministic Slack alerts
- [`aws-security-compliance-automation`](https://github.com/ojackson08/aws-security-compliance-automation) — Auto-remediates issues surfaced by CloudPulse

---

## License

MIT License — see [LICENSE](./LICENSE) for details.

---

## Contact

**Merkaba AI Risk Management**
security@merkabacreatives.org
https://merkabacreatives.org/ai-risk
