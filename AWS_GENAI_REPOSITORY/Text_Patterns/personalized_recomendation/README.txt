# Personalised Recommendation
- we will build a personalized recommendations application with Amazon Bedrock and Streamlit.

- The personalized recommendations pattern is good for the following use cases:
	- Creating personalized product recommendations, including a justification for each recommendation.
	- Creating custom "10 best" articles for vacation destinations, colleges, vehicles, or anything else that lends itself to that type of article.


# Architecture Overview
- A document is broken up into chunks of text. The chunks are passed to Titan Embeddings to be converted to vectors. The vectors are then saved to the vector database.
- The user submits a request.
- The question is converted to a vector using Amazon Titan Embeddings, then matched to the closest vectors in the vector database.
- The combined content and request are then used to generate a personalized recommendation to return to the user.