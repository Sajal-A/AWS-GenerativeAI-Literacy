import json
import boto3

## Initialize the Amazon Bedrock client library.
session = boto3.Session()

bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client

## Build the payload for the API call.
bedrock_model_id = "us.amazon.nova-lite-v1:0" #set the foundation model
prompt = "What is the largest city in India?" #the prompt to send to the model

# payload
# Here we are identifying the model to use, the prompt, and the inference parameters for the specified model.
messages = [
    {
        "role": "user",
        "content": [
            {"text": prompt}
        ]
    }
]

body = json.dumps({
    "schemaVersion": "messages-v1",
    "messages": messages,
    "inferenceConfig": {
        "maxTokens": 1024,
        "topP": 0.5,
        "topK": 20,
        "temperature": 0.0
    }
}) #build the request payload

## Call the Amazon Bedrock API.
# We use Bedrock's invoke_model function to make the call.
response = bedrock.invoke_model(body=body, 
                                modelId=bedrock_model_id, 
                                accept='application/json', 
                                contentType='application/json') #send the payload to Amazon Bedrock

## Display the response
# This extracts & prints the returned text from the model's response JSON.
print(response)
print("="*50)
response_body = json.loads(response.get('body').read()) # read the response
print(response_body)
print("="*50)
response_text = response_body["output"]["message"]["content"][0]["text"] #extract the text from the JSON response

print(response_text)
