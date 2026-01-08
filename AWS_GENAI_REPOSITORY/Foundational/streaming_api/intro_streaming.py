import json, boto3

## define the callback handler for streaming results
# This function allows us to print response chunks as they are returned from the streaming api

def chunk_handler(chunk):
    print(chunk,end='')


## Define the function to call the Amazon Bedrock streaming API
def get_streaming_response(prompt, streaming_callback):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')
    
    message = {
        "role": "user",
        "content": [ { "text": prompt } ]
    }
    
    response = bedrock.converse_stream(
        modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        messages=[message],
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0.0
        }
    )

    stream = response.get('stream')
    for event in stream:
        if "contentBlockDelta" in event:
            streaming_callback(event['contentBlockDelta']['delta']['text'])


## Display the response
prompt = "Tell me a story about two puppies and two kitten who became best friends."

get_streaming_response(prompt, chunk_handler)
print("\n")