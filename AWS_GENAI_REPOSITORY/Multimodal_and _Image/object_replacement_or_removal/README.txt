# Object Replacement or Removal

- We will build an image object replacement application using Amazon Nova Canvas, Amazon Bedrock, and Streamlit. 
We'll be using the Boto3 library to interact with Nova Canvas.

- Nova Canvas supports mask prompting. This allows us to specify items to remove from an image without having to 
know their exact dimensions. Nova Canvas will automatically mask the specified items so that something else can be inserted in their place.

## Use cases
- The object replacement or removal pattern is good for the following use cases:

	- Removing people from a vehicle photo
	- Removing clutter from a house photo
	- Replacing a piece of furniture or decoration with a similarly-sized item




