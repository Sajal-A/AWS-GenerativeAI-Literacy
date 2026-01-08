## Tool Use with the Amazon Bedrock Converse API
# Defining a tool and sending a message that will make Claude ask for tool use

import boto3, json, math

print("=======Defining a tool and sending a message that will make Claude ask for tool use=====\n")

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime')

tool_list = [
    {
        "toolSpec" : {
            "name": "factorial",
            "description": "Calculate the factorial of x.",
            "inputSchema": {
                "json":{
                    "type": "object",
                    "properties":{
                        "x":{
                            "type":"number",
                            "description":"The number to pass the function."
                        }
                    },
                    "required":["x"]
                }
            } 
        }
    }
]


msg_list = []

intial_msg = {
    "role": "user",
    "content": [
        {"text" : "What is the factorial of 7?"}
    ]
}
msg_list.append(intial_msg)

response = bedrock.converse(
    modelId = "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    messages = msg_list,
    inferenceConfig = {
        "maxTokens" : 1000,
        "temperature" : 0
    },
    toolConfig = {
        "tools" : tool_list
    },
    system = [
        {"text":"You must only do math by using a tool."}
    ]
)

res_msg = response['output']['message']
print(json.dumps(res_msg, indent=4))
msg_list.append(res_msg)

## Calling a function based on the toolUse content block.
# loop through the response msg's content block. 
# use the factorial tool if requested, and print any content block from the LLM's msg

print("====Calling a function based on the toolUse content block.=====")

response_content_blocks = res_msg['content']

for content_block in response_content_blocks:
    if 'toolUse' in content_block:
        tool_use_block = content_block['toolUse']
        tool_use_name  = tool_use_block['name']

        print(f"Using tool {tool_use_name}")

        if tool_use_name == "factorial":
            tool_result_value = math.factorial(tool_use_block['input']['x'])
            print(tool_result_value)

    elif 'text' in content_block:
        print(content_block['text'])


## Passing the tool result back to Claude
# loop through the content blocks from the response message, and check for a tool use request
# if there's tool use request, we'll call the named tool and pass it the input parameter provided by claude
# build a msg with a toolResult content block to send back to Claude for a final response

print("=====Passing the tool result back to Claude=====")
follow_up_content_blocks = []

for content_block in response_content_blocks:
    if 'toolUse' in content_block:
        tool_use_block = content_block['toolUse']
        tool_use_name = tool_use_block['name']

        if tool_use_name == 'factorial':
            tool_result_value = math.factorial(tool_use_block['input']['x'])

            follow_up_content_blocks.append({
                "toolResult" : {
                    "toolUseId" : tool_use_block['toolUseId'],
                    "content" : [
                        {
                            "json" : {
                                "result" : tool_result_value
                            }
                        }
                    ]
                }
            })

if len(follow_up_content_blocks) > 0:
    follow_up_message = {
        "role" : "user",
        "content" : follow_up_content_blocks
    }
    msg_list.append(follow_up_message)

    response = bedrock.converse(
        modelId = "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        messages=msg_list,
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0
        },
        toolConfig={
            "tools": tool_list
        },
        system=[{"text":"You must only do math by using a tool."}]
    )

    response_message = response['output']['message']
    
    msg_list.append(response_message)
    print(json.dumps(msg_list, indent=4))



## Error handling - letting Claude know that tool use failed
# let's build an error to send backto the LLM, so that Claude can decide what to do next

print("=====Error handling - letting Claude know that tool use failed=====\n")

del msg_list[-2:] #Remove the last request and response

content_block = next((block for block in response_content_blocks if 'toolUse' in block), None)

if content_block:
    tool_use_block = content_block['toolUse']
    error_tool_result = {
        "toolResult" : {
            "toolUseId" : tool_use_block['toolUseId'],
            "content" : [
                {
                    "text" : "invalid function: factorial"
                }
            ],
            "status" : "error"
        }
    }

    follow_up_message = {
        "role" : "user",
        "content" : [error_tool_result]
    }

    msg_list.append(follow_up_message)

    response = bedrock.converse(
        modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        messages=msg_list,
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0
        },
        toolConfig={
            "tools": tool_list
        },
        system=[{"text":"You must only do math by using a tool."}]
    )

    response_message = response['output']['message']
    print(json.dumps(response_message, indent=4))
    msg_list.append(response_message)

    print("======Display the overall message history======")
    print(json.dumps(msg_list, indent=4))


