# Image Masking 

- we will build an image masking application using Amazon Nova Canvas, Amazon Bedrock, and Streamlit.
 We'll be using the Boto3 library to interact with Nova Canvas.

- There are two key concepts to understand when editing images using Amazon Nova Canvas
	-  masking and painting.

**Masking**

- Masking is the process of marking a portion of an image to be redrawn or preserved. 
Nova Canvas supports two masking methods:

- An image mask is a special image file that indicates the pixels that should be masked in the original image. 
Black pixels indicate what is masked, and white pixels mark what is not masked. The image mask should have the following characteristics:

	- The same dimensions and resolution as the original image file
	- PNG file format
	- Either RGB or grayscale
	- No alpha channel

- A mask prompt is a way to dynamically mask an image by using a prompt. 
The prompt can be one or more words that describes what to mask. 
Behind the scenes, Nova Canvas will automatically create a mask based on that prompt.

**Painting**

- Painting is the creation of new imagery using an image generation model. 
There are two modes of painting available with Nova Canvas:

	- Inpainting is the process of repainting all of the pixels within the masked area of an image. 
	When using an image mask, all of the black pixels will be repainted. When using a mask prompt, 
	the items indicated in the mask prompt will be repainted.

	- Outpainting is the process of painting all the pixels outside of the masked area of an image.
	 When using an image mask, all of the white pixels will be repainted. When using a mask prompt, 
	the items indicated in the mask prompt will be preserved, and everything else will be repainted.


## Use cases

- The image masking pattern is good for the following use cases:

	- Adding items to an image
	- Removing undesired items from an image
	- Changing the background of an image
	- Extending an image