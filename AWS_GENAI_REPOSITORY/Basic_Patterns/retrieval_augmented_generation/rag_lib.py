import itertools
import boto3 
import chromadb
from chromadb.utils.embedding_functions import AmazonBedrockEmbeddingFunction

## Add a function to connect to the ChromaDB collection
# This will allow us to access the previously created Chroma vector database

def get_collection(path, collection_name):
    session = boto3.Session()
    embedding_function = AmazonBedrockEmbeddingFunction(session=session, model_name="amazon.titan-embed-text-v2:0")
    
    client = chromadb.PersistentClient(path=path)
    collection = client.get_collection(collection_name, embedding_function=embedding_function)

    return collection


## Add the function to retrieve results from the vectore store
def get_vector_search_results(collection, question):
    results = collection.query(
        query_texts = [question],
        n_results = 4
    )

    return results


## Add a function to call Amazon Bedrock
"""
This code searches the previously created index based on the user's input, adds the best matches 
to a prompt along with the user's text, and then sends the combined prompt to the model.
"""

def get_rag_response(question):

    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')

    collection = get_collection('/environment/workshop/data/chroma',"bedrock_faqs_collection")

    search_results = get_vector_search_results(collection, question)

    flattened_results_list = list(itertools.chain(*search_results['documents']))

    rag_content = '\n\n'.join(flattened_results_list)

    print(rag_content)

    message = {
        "role" : "user",
        "content" : [
            {"text" : rag_content},
            {"text" : "Based on the content above, please answer the following question."},
            {"text" : question }
        ]
    }

    response = bedrock.converse(
        modelId="us.amazon.nova-lite-v1:0",
        messages=[message],
        inferenceConfig={
            "maxTokens": 2000,
            "temperature": 0,
            "topP": 0.9,
            "stopSequences": []
        },
    )
    return response['output']['message']['content'][0]['text'], flattened_results_list
