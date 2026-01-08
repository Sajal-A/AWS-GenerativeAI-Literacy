import json, boto3
import numpy as np 

## define the function to get an embedding from Amazon Bedrock
def get_embedding(text):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')

    embedding_response = bedrock.invoke_model(
        body = json.dumps({"inputText":text}),
        modelId = "amazon.titan-embed-text-v2:0",
        accept = "application/json",
        contentType = "application/json"
    )
    response_body = json.loads(embedding_response['body'].read())
    return response_body['embedding']

## Define the classes to store embedding and the comparison results
class EmbedItem:
    def __init__(self, text):
        self.text = text
        self.embedding = get_embedding(text)

class ComparisonResult:
    def __init__(self, text, similarity):
        self.text = text
        self.similarity = similarity


## Define the function to compare the similarity of two vectors
# this implement the cosine similarity
def calculate_similarity(a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

## build the list of embeddings from the items.txt file
items = []

with open('/environment/workshop/labs/embedding/items.txt','r') as f:
    text_items = f.read().splitlines()

print(text_items)

for text in text_items:
    items.append(EmbedItem(text))

print(items)

## Compare embeddings and display lists to show how similar or different the various texts are:
# A similarity value of 1 means exactly the same.
# The smaller the similarity, the less similar are the embeddings

for t1 in items:
    print(f"Closest matches for '{t1.text}'")
    print('='*20)
    cosine_comparisons= []

    for t2 in items:
        similarity_score = calculate_similarity(t1.embedding, t2.embedding)

        cosine_comparisons.append(ComparisonResult(t2.text, similarity_score))
    
    cosine_comparisons.sort(key = lambda x : x.similarity, reverse=True )

    for c in cosine_comparisons:
        print("%.6f" % c.similarity, "\t", c.text)
    
    print()

