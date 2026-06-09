import json
import boto3
import os

bedrock = boto3.client('bedrock-runtime')
cloudwatch = boto3.client('cloudwatch')

def get_cloudwatch_alarms():
    """Fetches current CloudWatch alarms in ALARM state."""
    response = cloudwatch.describe_alarms(StateValue='ALARM')
    alarms = []
    for alarm in response.get('MetricAlarms', []):
        alarms.append({
            "AlarmName": alarm['AlarmName'],
            "MetricName": alarm['MetricName'],
            "StateReason": alarm['StateReason']
        })
    return alarms

def lambda_handler(event, context):
    """
    CloudPulse AI:
    Accepts a natural language query about AWS infrastructure, fetches relevant telemetry,
    and uses Bedrock (Claude 3) to generate a human-readable diagnosis and remediation plan.
    """
    try:
        body = json.loads(event.get('body', '{}')) if isinstance(event.get('body'), str) else event
        query = body.get('query')
        
        if not query:
            return {"statusCode": 400, "body": json.dumps({"error": "query is required"})}

        # In a full implementation, we would route the query to specific AWS APIs based on intent.
        # For this prototype, we'll fetch active alarms as context.
        active_alarms = get_cloudwatch_alarms()
        
        system_prompt = """
        You are CloudPulse AI, an expert AWS Cloud Architect. 
        Analyze the user's natural language query along with the provided AWS telemetry context.
        Provide a structured response with:
        1. Root Cause Analysis
        2. Business Impact
        3. Recommended Remediation (include Terraform or AWS CLI snippets if applicable)
        """
        
        prompt = f"User Query: {query}\n\nAWS Telemetry Context (Active Alarms):\n{json.dumps(active_alarms, indent=2)}"
        
        # Call Bedrock (Claude 3 Sonnet)
        bedrock_response = bedrock.invoke_model(
            modelId='anthropic.claude-3-sonnet-20240229-v1:0',
            contentType='application/json',
            accept='application/json',
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 1000,
                "system": system_prompt,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            })
        )
        
        response_body = json.loads(bedrock_response['body'].read())
        ai_analysis = response_body['content'][0]['text']

        return {
            "statusCode": 200,
            "body": json.dumps({
                "query": query,
                "analysis": ai_analysis
            })
        }

    except Exception as e:
        print(f"CloudPulse error: {e}")
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
