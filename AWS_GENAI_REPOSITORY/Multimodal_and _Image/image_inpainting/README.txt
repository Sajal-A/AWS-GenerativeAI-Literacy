# Image Inpainting

-  We will build an image inpainting application using Amazon Nova Canvas, Amazon Bedrock, and Streamlit.
 We'll be using the Boto3 library to interact with Nova Canvas.

- The image inpainting pattern uses Nova Canvas’s image mask inpainting capability. It requires two image files:
	- The original image.
	- An image mask consisting of black and white pixels. 
	The black pixels indicate the mask portion of the image. 
	Since we’re inpainting, the black pixels will be repainted.

- We'll programmatically generate an image mask based on a set of predetermined values, or allow the user to specify 
rectangular coordinates for a custom-generated image mask. For an example of using a pre-created image mask.

## Use cases
The image inpainting pattern is good for the following use cases:

	- Brainstorm decoration ideas by swapping out specific areas of a room photo.
	- Change a portion of the image that is too bare, or has distractions that should be removed.
	- Allowing a user to select areas of an image that should be repainted.



