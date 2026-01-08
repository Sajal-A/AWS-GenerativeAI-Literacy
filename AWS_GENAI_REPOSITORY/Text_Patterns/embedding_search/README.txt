# Embedding Search

- We will build a simple embeddings search application with Titan Embeddings and Streamlit.
- This example is similar to the Retrieval-Augmented Generation.  we also match a query to the closest entries in a vector database. 
But in this case, we do not pass those matches to a large language model. Instead, we will just display those matches directly in the user interface. 
This can be useful if you want to troubleshoot a RAG application, or directly evaluate an embeddings model.

- The embeddings search pattern is good for the following use cases:
	- Identifying related items based on text descriptions
	- Application portfolio rationalization - particularly in cases where data between the companies or divisions is inconsistent, 
	matching applications based on their descriptions can accelerate the process of finding potential overlap.

# Architecture Overview
- A document is broken up into chunks of text. The chunks are passed to Titan Embeddings to be converted to vectors. The vectors are then saved to the vector database.
- The user submits a question.
- The question is converted to a vector using Amazon Titan Embeddings, then matched to the closest vectors in the vector database.
- The combined content from the matching vectors are then returned to the user