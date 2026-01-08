import json, boto3

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

msg_list = []

initial_msg = {
    "role" : "user",
    "content" : [
        {"text":"How are you today? What date is today?"}
    ],
}

msg_list.append(initial_msg)

response = bedrock.converse(
    modelId = "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    messages = msg_list,
    inferenceConfig = {
        "maxTokens" : 1000,
        "temperature" : 0
    }
)

response_msg = response['output']['message']
print(json.dumps(response_msg, indent=4))

print(f"\n===Alternating user and assitant messages===\n")
msg_list.append(response_msg)

print(json.dumps(msg_list, indent=4))

print(f"\n===Including an image in message===\n")

with open("/environment/workshop/labs/converse/image.webp","rb") as img_file:
    image_bytes = img_file.read()

img_msg = {
    "role" : "user",
    "content" : [
        {"text":"Image 1"},
        {
            "image" : {
                "format" : "webp",
                "source" : {
                    "bytes":image_bytes
                }
            }
        },
        {"text":"Please describe the image."}
    ]
}

msg_list.append(img_msg)

response = bedrock.converse(
    modelId = "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    messages = msg_list,
    inferenceConfig = {
        "maxTokens" : 1000,
        "temperature" : 0
    }
)

res_msg = response['output']['message']
print(json.dumps(res_msg, indent=4))


print("\n===Understanding and setting a system prompt===\n")

summary_message = {
    "role" : "user",
    "content" : [
        {"text" : "Can you please summarize our conversation so far?"}
    ],
}

msg_list.append(summary_message)

response = bedrock.converse(
    modelId = "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    messages = msg_list,
    system = [
        {"text":"Please respond to all the request in the style of a wizard."}
    ],
    inferenceConfig = {
        "maxTokens":2000,
        "temperature":0
    }
)
print(response)

response_msg = response['output']['message']

print(json.dumps(response_msg, indent=4))

msg_list.append(response_msg)

print("="*40)
# print(msg_list)
print("="*40)

print("\n====Getting response metadata and token counts====\n")
print("Stop Reason: ", response['stopReason'])
print("Usage:",json.dumps(response['usage'],indent=4))
