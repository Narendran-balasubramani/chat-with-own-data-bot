# importing libraries
import os
import tempfile
import streamlit as st
from dotenv import load_dotenv
from backend import pdf_reader,get_conversation_chain,get_text_chunks,get_vectorstore,csv_reader

# ----------------------------------------------------------------


# side bar

with st.sidebar:
    # st.write('hai')
    model_preference=st.selectbox('Choose your preference: ',['OpenAI','HuggingFace'])
    
    if model_preference == 'HuggingFace':
        key=st.text_input('Enter your HuggingFace key',type='password')
        st.error('Huggingface is currently not available. Please choose Openai model',icon='⚠️')
        
    else:
        # os.environ['OPENAI_API_KEY']==st.text_input('Enter your OpenAI API key',type='password')
        OPENAI_API_KEY=st.text_input('Enter your OpenAI API key',type='password')


        doc_preference= st.selectbox('Choose prefered document type: ',['PDF','CSV'])
        doc_input = st.file_uploader(f'Upload your {doc_preference}',[doc_preference], accept_multiple_files=False)
        
        if st.button("Process"):
            if doc_preference=='CSV':
                with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                    tmp_file.write(doc_input.getvalue())
                    tmp_file_path = tmp_file.name
                text_chunks = csv_reader(tmp_file_path)
                st.write(text_chunks)
            else:
                raw_text = pdf_reader(doc_input)
                text_chunks = get_text_chunks(raw_text)
                st.write(text_chunks)
                

        # if st.button("Process"):
        #     try:
        #         with st.spinner("Processing"):
        #             # get pdf text
        #             raw_text = pdf_reader(doc_input) 

        #             # get the text chunks
        #             text_chunks = get_text_chunks(raw_text)

        #             # create vector store
        #             vectorstore = get_vectorstore(text_chunks)

        #             # create conversation chain
        #             st.session_state.conversation = get_conversation_chain(
        #                 vectorstore)
        #     except:
        #         st.warning('Please upload a vaild key/document.',icon='⚠️')

#--------------------------------------------------------------------------------------------------------



# main page
st.title('Chat with Bot')

with st.chat_message("assistant"):
    st.markdown('Hi there👋 I\'m your friendly AI assistant. I can help you answer your queries by uploading your documents. Just ask me anything!')

# initializing chat history - This is to show the previous converasation of the user and LLM.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Showing the previous conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# handling error
try:
    # checking for prompt
    if prompt :=  st.chat_input('Write your prompt here...'):
        # appending the user prompt to session state
        st.session_state.messages.append({"role": "user", "content": prompt})
        # displaying the prompt 
        with st.chat_message("user"):
            st.markdown(prompt)

        # displaying the answer
        with st.chat_message("assistant"):
            # getting response from the model through chain
            response = st.session_state.conversation({'question': prompt})
            st.markdown(response['result'])
        # adding the response from the model to session state
        st.session_state.messages.append({"role": "assistant", "content": response})

except:
        st.warning('Please upload a vaild key/document.',icon='⚠️')