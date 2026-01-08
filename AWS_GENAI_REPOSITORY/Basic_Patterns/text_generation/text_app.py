import streamlit as st 
from text_lib import get_text_response

st.set_page_config(page_title="Text to Text") #HTML title
st.title("Text to Text") #page title

input_text = st.text_area("Input text", label_visibility="collapsed") #display a multiline text box with no label
go_button = st.button("Go", type="primary") #display a primary button

if go_button: #code in this if block will be run when the button is clicked
    
    with st.spinner("Working..."): #show a spinner while the code in this with block runs
        response_content = get_text_response(input_content=input_text) #call the model through the supporting library
        
        st.write(response_content) #display the response content


