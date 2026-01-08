# RAG

- Large language models are prone to hallucination, which is just a fancy word for making up a response. 
To correctly and consistently answer questions, we need to ensure that the model has real information available to support its responses. 
We use the Retrieval-Augmented Generation (RAG) pattern to make this happen.

- With Retrieval-Augmented Generation, we first pass a user's prompt to a data store. 
This might be in the form of a query to Amazon Kendra . We could also create a numerical representation of the prompt using Amazon Titan Embeddings to pass to a vector database. 
We then retrieve the most relevant content from the data store to support the large language model's response.

- In this practise, we will use a local Chroma  database to demonstrate the RAG pattern. 
In a real-world scenario, you will most likely want to use a persistent data store through Amazon Kendra or Knowledge Bases for Amazon Bedrock .

## USE CASE

- The Retrieval-Augmented Generation pattern is good for the following use cases:

	- Question & answer, supported by specialized knowledge or data
	- Intelligent search

- The architecture overview:
	- A document is broken up into chunks of text. The chunks are passed to Titan Embeddings to be converted to vectors. The vectors are then saved to the vector database.
	- The user submits a question.
	- The question is converted to a vector using Amazon Titan Embeddings, then matched to the closest vectors in the vector database.
	- The combined content from the matching vectors + the original question are then passed to the large language model to get the best answer.
