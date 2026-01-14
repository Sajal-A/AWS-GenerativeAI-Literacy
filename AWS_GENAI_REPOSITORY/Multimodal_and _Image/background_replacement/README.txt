# Background replacement

- We will build an image background replacement application using Amazon Nova Canvas, Amazon Bedrock, and Streamlit. We'll be using the Boto3 library to interact with Nova Canvas.

- Nova Canvas supports mask prompting. This allows us to specify items to preserve from an image without having to know their exact dimensions. Nova Canvas will automatically mask 
the specified items so that something new can be painted in the background.

- Understanding the steps
	- Start with the original object image ( Input-img = 'a laptop on the table near a Christmas tree' )
	- Specify the object to mask ( "laptop" )
	- Specify what should be painted in the unmasked area ("laptop on a table at the beach")
	- Outpaint the unmasked area of the original image (output-img = "a laptop on a table at the beach")


## Outpainting mode: Default vs Precise

Canvas supports two outpainting modes:

- Default mode allows the masked image to potentially extend into the new background. 
This is helpful when you have existing background elements within your mask that should be extended seamlessly, or 
when the masked item should blend together smoothly with the background.

- Precise mode prevents the masked image from extending into the new background. 
This is important when you have a product that cannot be extended - it just needs to be placed on a new background.


## Use cases
- The image background replacement pattern is good for the following use cases:

	- Creating alternate scenery for product photos
	- Removing distractions and clutter from the background of product photos
	- Creating new marketing or article images using a person or object from another image

