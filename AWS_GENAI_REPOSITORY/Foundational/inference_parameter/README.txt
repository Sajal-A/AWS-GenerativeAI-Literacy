# Inference Parameter

Inference parameters  are used to configure the response behavior of the foundation model. 
Inference parameters vary from model to model:

- At a minimum, they can be used to influence the variability (Temperature, Top P) and token length of the response.
	- Temperature: controlling response variability
	- You can think of tokens as either a word or part of a word. The overall ratio of tokens per word varies from model to model. Many common words could be represented as a single token, 
	while less common words might contain multiple tokens.
- Stop Sequences are another common parameter, useful for splitting few-shot prompt examples or stopping the model from having a conversation with itself.

You can see the various inference parameters for each model in the Amazon Bedrock console, along with definitions for those parameters.