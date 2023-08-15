# importing libraries
import streamlit as st
from dotenv import load_dotenv
# from PyPDF2 import PdfReader
# from langchain import HuggingFaceHub, FAISS
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.embeddings import HuggingFaceBgeEmbeddings,OpenAIEmbeddings
# from langchain.chat_models import ChatOpenAI
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import ConversationalRetrievalChain
from backend import pdf_reader,get_conversation_chain,get_text_chunks,get_vectorstore

# ----------------------------------------------------------------



# # creating function to read the contents of the PDF
# def pdf_reader(pdf_doc):
#     text = ''
    
#     for pdf in pdf_doc:
#         pdf_reader = PdfReader(pdf)
#         for page in pdf_reader.pages:
#             text += page.extract_text()
#         return text


# # creating function to create chunks 
# def get_text_chunks(text):
#     text_splitter=CharacterTextSplitter(
#         separator='\n',
#         chunk_size=500,
#         chunk_overlap=100,
#         length_function=len)
#     chunks = text_splitter.split_text(text)
#     return chunks

# # creating function to create and store embeddings
# def get_vectorstore(chunks):
#     embeddings = OpenAIEmbeddings()
#     # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
#     vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
#     return vectorstore

# # Creating conversation chain
# def get_conversation_chain(vectorstore):
#     llm = ChatOpenAI()
#     # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

#     memory =ConversationBufferMemory(
#         memory_key='chat_history',  
#         return_messages=True
#     )
    
#     conversation_chain = ConversationalRetrievalChain.from_llm(
#         llm=llm,
#         retriever=vectorstore.as_retriever(),
#         memory=memory
#     )
#     return conversation_chain

#-------------------------------------------------------------------------------------------------------

# side bar

with st.sidebar:
    # st.write('hai')
    model_preference=st.selectbox('Choose your preference: ',['OpenAI','HuggingFace'])
    if model_preference == 'OpenAI':
        OPENAI_API_KEY=st.text_input('Enter your OpenAI API key')
    else:
        key=st.text_input('Enter your HuggingFace key')
    

    doc_input = st.file_uploader('Upload your PDF',['pdf'], accept_multiple_files=True)

    if st.button("Process"):
        with st.spinner("Processing"):
            # get pdf text
            raw_text = pdf_reader(doc_input)

            # get the text chunks
            text_chunks = get_text_chunks(raw_text)

            # create vector store
            vectorstore = get_vectorstore(text_chunks)

            # create conversation chain
            st.session_state.conversation = get_conversation_chain(
                vectorstore)

#--------------------------------------------------------------------------------------------------------





# main page
st.title('Chat with Bot')

# initializing chat history - This is to show the previous converasation of the user and LLM.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Showing the previous conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# checking for prompt
if prompt :=  st.chat_input('Write your prompt here...'):
    # appending the user prompt to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    # writing the prompt 
    with st.chat_message("user"):
        st.markdown(prompt)

    # writing the answer
    with st.chat_message("assistant"):
        # getting response from the model through chain
        response = st.session_state.conversation({'question': prompt})
        st.markdown(response['result'])
    # adding the response from the model to session state
    st.session_state.messages.append({"role": "assistant", "content": response})


# st.chat_input('Write your prompt here...')