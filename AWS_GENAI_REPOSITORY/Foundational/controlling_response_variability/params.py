import boto3, sys

## build a function to call amazon bedrock with the appropriate inference parameter for the model
def get_text_response(model, input_content):
    session = boto3.Session()
    # instantiate the Amazon bedrock client
    bedrock = session.client(service_name = 'bedrock-runtime')

    # set the user message
    message = {
        "role" : "user",
        "content" : [{"text" : input_content}]
    }

    response = bedrock.converse(
        modelId = model, # setting the model
        messages = [message],
        inferenceConfig = {
            "maxTokens" : 1000,
            "temperature" : 0,
            "topP" : 0.9,
            "stopSequences" : []
        }
    )

    return response['output']['message']['content'][0]['text']


# display the response
response = get_text_response(sys.argv[1],sys.argv[2]) # pass the argumnents from the command line.

print(response)