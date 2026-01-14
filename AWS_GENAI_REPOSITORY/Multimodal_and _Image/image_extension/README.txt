# Image Extension

- We will build an image extension application using Amazon Nova Canvas, Amazon Bedrock, and Streamlit. We'll be using the Boto3 library to interact with Nova Canvas.

- The image extension pattern is a special case of outpainting. By default, Nova Canvas outpainting works by taking an existing image, identifying a masked area to preserve, 
and repainting everything outside that masked area. To extend an image, we will need to programmatically resize the image and generate an image mask.


- Understand the steps:
	- Start with the original image
	- Place the original image within a larger blank image
	- Generate a mask for the original image area
	- Specify what should be outpainted in the extended area
	- Outpaint the blank area of the larger image


## Use cases
The image extension pattern is good for the following use cases:
	- Extending a product or marketing image to fit different dimension requirements.




