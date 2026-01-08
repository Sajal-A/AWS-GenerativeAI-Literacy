import streamlit as st 
from chatbot_app import chat_with_model

# Add the page title and configuration
st.set_page_config(page_title="Chatbot")
st.title("ChitChat Buddy!!!")

# Add the UI chat history to the session cache. 
# This allows us to re-render the chat history to the UI as the Streamlit app is re-run with each user interaction. 
# Otherwise, the old messages will disappear from the user interface with each new chat message.

if 'chat_history' not in st.session_state: # see if the chat history hasn't been created yet
    st.session_state.chat_history = [] # initialize the chat history

# Add the chat input controls
chat_container = st.container()

input_text = st.chat_input("Chat with your bot here.")

if input_text:
    chat_with_model(message_history= st.session_state.chat_history, new_text = input_text)

# Add the for loop to render previous chat messages
# Re-render the chat history (Streamlit re-runs this script, so need this to previous chat messages)
for message in st.session_state.chat_history: # loop through the chat history
    with chat_container.chat_message(message.role): # renders a chat line for the given role, containing everything in the with block
        st.markdown(message.text) # display the chat content


