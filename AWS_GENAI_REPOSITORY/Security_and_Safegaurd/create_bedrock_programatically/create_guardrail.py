import boto3, json, random, string

client = boto3.client(service_name='bedrock')


# Add the code to create a guardrail.
## We're creating a guardrail that filters Bitcoin conversations, toxic content, 
## discussions about the compitor "AnyCompany", and profanity. 

response = client.create_guardrail(
    name = "Guardrail-from-code-"+"".join(random.choices(string.ascii_lowercase, k=8)),
    description = 'string',
    topicPolicyConfig = {
        'topicsConfig' : [
            {
                "name" : "Bitcoin",
                "definition" : "Providing advice, direction, or examples of how to mine, use, or interact with Bitcoin, including Cryptocurrency-related third-party services.",
                "examples" : [
                    "How do I mine Bitcoin?",
                    "What is the current value of BTC?",
                    "Which instance is the best for crypto mining?",
                    "Is mining cryptocurrency against the terms?",
                    "How do I maximize my Bitcoin profits?",
                ],
                "type" : "DENY",
            }
        ]
    },
    contentPolicyConfig = {
        'filtersConfig' : [
            {"type" : "SEXUAL", "inputStrength" : "HIGH", "outputStrength": "HIGH"},
            {"type" : "HATE", "inputStrength" : "HIGH", "outputStrength" : "HIGH" },
            {"type": "VIOLENCE", "inputStrength": "HIGH", "outputStrength": "HIGH"},
            {"type": "INSULTS", "inputStrength": "HIGH", "outputStrength": "HIGH"},
            {"type": "MISCONDUCT", "inputStrength": "HIGH", "outputStrength": "HIGH"},
            {"type": "PROMPT_ATTACK", "inputStrength": "HIGH", "outputStrength": "NONE"},
        ]
    },
    wordPolicyConfig={
        "wordsConfig": [{"text": "AnyCompany"}],
        "managedWordListsConfig": [{"type": "PROFANITY"}],
    },
    sensitiveInformationPolicyConfig={
        "piiEntitiesConfig": [
            {"type": "NAME", "action": "ANONYMIZE"},
            {"type": "EMAIL", "action": "ANONYMIZE"},
        ],
    },
    blockedInputMessaging="Apologies, this model cannot be used to discuss inappropriate or off-topic content.",
    blockedOutputsMessaging="Apologies, the model's response to your request was blocked.",
)

guardrail_id = response['guardrailId']

## Create a guardrail version
# This creates a numbered version of the guardrail that can be used for testing or production purpose
# You can also use the built-in "DRAFT" version of a guardrail during development.abs

response = client.create_guardrail_version(
    guardrailIdentifier=guardrail_id,
)

# Display the guardrail ID.
print(guardrail_id)

