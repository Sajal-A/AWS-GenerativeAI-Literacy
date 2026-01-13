# Extracting CSV data from text

- We will build a CSV generator using Amazon Bedrock and Streamlit.

- Text to CSV allows us to extract tabular data from unstructured content. For example, we can extract information from a customer's email, 
including any referenced products, employees mentioned, sentiment, account numbers, and anything else the model can detect based on our prompt.
- To generate CSV, we first generate JSON through Amazon Bedrock's built-in tool use capabilities, which generate JSON responses based on a predefined JSON schema. 
We can then convert the JSON to CSV.

- The text to CSV pattern is good for the following use cases:

	- Email data extraction
	- Call transcript data extraction
	- Document data extraction
	- Sample dataset generation