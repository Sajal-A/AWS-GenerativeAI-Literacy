# Image Understanding

- We will build an image understanding application using Anthropic Claude 3, Amazon Bedrock, and Streamlit. We'll be using the Boto3 library to interact with Anthropic Claude.

- The image understanding pattern requires two inputs:

	- One or more images to analyse.
	- A prompt to describe what you want to know about the images.

## Use cases
- The image understanding pattern is good for the following use cases:
	- Generate accessible alternate text and image captions
	- Use in an image processing pipeline to detect if an image is inappropriate or a mismatch for its related content
	- Use in an image processing pipeline to automate mask prompting and inpainting/outpainting actions
	- Categorize images
	- Extract text from images
	- Many more 
