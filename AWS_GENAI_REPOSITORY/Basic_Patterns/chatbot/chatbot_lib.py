import boto3

# sets the upper limit for previous chat message kept in memory.
MAX_MESSAGES = 20

# ChatMessage class is used to store text messages.
class ChatMessage:
    def __init__(self, role, text):
        self.role = role
        self.text = text


# Add a function to convert the ChatMessage to Converse API format
# This format allows us to send a list of current and past messages to Amazon Bedrock for processing
def convert_chat_messages_to_converse_api(chat_message):
    messages = []

    for chat_msg in chat_message:
        messages.append({
            "role" : chat_msg.role,
            "content" : [
                {"text" : chat_msg.text}
            ]
        })
    
    return messages


# Add function to call Amazon Bedrock
def chat_with_model(message_history, new_text=None):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')

    new_text_message = ChatMessage('user',text=new_text)
    message_history.append(new_text_message)

    num_of_msg = len(message_history)

    if num_of_msg > MAX_MESSAGES:
        del message_history[0 : (num_of_msg - MAX_MESSAGES) * 2] #make sure we remove both the user and assistant responses

    messages = convert_chat_messages_to_converse_api(message_history)

    response = bedrock.converse(
        modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        messages=messages,
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0,
            "topP": 0.9,
            "stopSequences": []
        },
    )

    output = response['output']['message']['content'][0]['text']
    response_message = ChatMessage('assistant', output)

    message_history.append(response_message)

    return 
    