# CloudPulse AI: Natural Language Infrastructure Interrogation Engine

## The Gap in the Landscape
Cloud engineers spend an enormous amount of time writing CloudWatch queries, parsing logs, and debugging infrastructure issues. There is no native tool that allows engineers to simply ask *"Why did my Lambda function spike at 2am?"* or *"Which EC2 instance is causing the cost anomaly?"* in plain English and receive a root-cause answer with a remediation plan.

## The Solution
**CloudPulse AI** is a "Copilot for your AWS account." It is an AWS-native natural language interface that accepts plain English questions about your infrastructure, queries the relevant AWS telemetry (CloudWatch, Cost Explorer), and uses Amazon Bedrock (Claude 3) to return a structured diagnosis, business impact assessment, and Terraform remediation snippet.

## Architecture
- **Amazon API Gateway:** Provides the `/ask` endpoint for natural language queries (can be integrated into Slack or a web dashboard).
- **AWS Lambda (Python/Boto3):** Acts as the orchestrator. It fetches the user's query, retrieves current AWS telemetry (e.g., active CloudWatch alarms), and constructs the prompt.
- **Amazon Bedrock (Claude 3 Sonnet):** The reasoning engine. It analyzes the telemetry context against the user's query to determine root cause and generate remediation steps.
- **Terraform:** Infrastructure as Code for 1-click deployment.

## Business Impact
Dramatically reduces Mean Time to Resolution (MTTR) for cloud incidents. Empowers junior engineers to troubleshoot complex infrastructure issues by leveraging the reasoning capabilities of Claude 3 combined with live AWS data. Directly demonstrates the power of EV+AI hybrid engineering.

## How to Deploy
```bash
cd terraform
terraform init
terraform apply
```

## Usage Example
```bash
curl -X POST https://<api-id>.execute-api.us-east-1.amazonaws.com/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "Why is the production API responding slowly today?"}'
```

**Response:**
```json
{
  "query": "Why is the production API responding slowly today?",
  "analysis": "1. Root Cause Analysis: The `TargetResponseTime` alarm for the production ALB is currently in ALARM state. Telemetry indicates a backend bottleneck...\n\n2. Business Impact: Increased latency is causing a 15% drop in checkout conversions...\n\n3. Recommended Remediation: Scale up the ECS task count. Terraform snippet included below..."
}
```
