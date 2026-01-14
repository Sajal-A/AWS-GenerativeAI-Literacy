# Image Search

- We will build a simple image search application with Titan Multimodal Embeddings and Streamlit.

- Titan Multimodal Embeddings is a multimodal embeddings model for use cases like searching images by text, image, or a combination of text and image.

- This example is similar to the Embeddings Search. In this example, we create a searchable index of images by doing the following:
	- Read each image file in a local directory.
	- Pass the image bytes to Titan Multimodal Embeddings to get a numerical representation (AKA vector or embedding) of the image.
	- Save the embedding and metadata (including the path to the original image file) to a local Chroma  database.
- We can then search for images in the Chroma database using the following approach:
	- Convert a user’s search expression or uploaded image to a numerical representation using Amazon Titan Multimodal Embeddings.
	- Search the Chroma database for the closest matches.
	- Return and display the closest matching images.

## Use Cases
- The image search pattern is good for the following use cases:
	- Image collection search
	- Finding similar/identical images in a collection
	- Classifying images based on similarity to existing examples
