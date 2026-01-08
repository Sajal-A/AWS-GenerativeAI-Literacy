# Tool Use
Tool use is a capability that allows a large language model to tell the calling application to invoke a function with parameters supplied by the model. 
The available functions and supported parameters are passed to the model along with a prompt. It's important to note that the large language model does not call a function itself 
- it just returns JSON and lets the calling application do the rest.

Why is native tool use so important? 
Because now we get built-in support for turning free-form content into automation-friendly and analytics-friendly structured data. 
While advanced prompt engineers had some success manually building tool use applications with existing large language models, it was often brittle, 
or XML-based, or susceptible to creating invalid JSON.

Tool Use with the Amazon Bedrock Converse API follows these steps:

1. The calling application passes (A) tool definitions and (B) a triggering message to the large language model.
2. If the request matches a tool definition, the model generates a tool use request, including the parameters to pass to the tool.
3. The calling application extracts the parameters from the model’s tool use request and passes them to the corresponding local function for the tool.
4. The calling application can then either use the tool result directly, or pass the tool result back to the model to get a follow-on response.
5. The model either returns a final response, or requests another tool.

# We'll walk you through 
- tool use with the Amazon Bedrock Converse API
- Calling a function based on the toolUse content block
- Passing the tool result back to LLM (Claude)
- Error handling: letting Claude know that tool use failed.
