# ConvoCraft: Your Intelligent Chat Companion 🤖

## Scope of the Project
This project aims on building a question answering bot that uses the **Langchain** framework and the **OpenAI GPT model**. The bot can answer questions about a specific set of documents that have been provided to it.

## - LLMs
<b>Large language models (LLMs)</b> are a type of artificial intelligence that can be used to understand and generate text. LLMs are trained on massive datasets of text, and they can be used for a variety of tasks, such as question answering, translation, and summarization.

## - Langchain
<b>Langchain</b> is an open-source framework for building natural language processing applications using large language models (LLMs). Langchain provides a standard interface for chains, lots of integrations with other tools, and end-to-end chains for common applications.

## - Openai models
OpenAI models are a suite of large language models (LLMs) that can be used for a variety of natural language processing (NLP) tasks. Some of the most popular OpenAI models include GPT-3.5 turbo, GPT-4, DALL-E.

# Flow of the Project
!['Flow diagram of this project](Flow_diagram\flow.png)

## 1) <b>Documents:</b>
-  The first step is to gather the documents that the bot will be able to answer questions about. These documents can be in either **PDF** or **CSV** format. 
- PDF files are commonly used to store documents that contain a lot of text, such as books and articles. 
- CSV files are commonly used to store data in a table format, such as spreadsheets and databases.
## 2) <b>Chunks:</b> 
- The documents are then chunked into smaller pieces. This is done to make it easier for the bot to process the documents.
## 3) <b>Embeddings:</b> 
- Embedding is the process of representing words and phrases as numerical vectors. This allows the bot to better understand the meaning of the text. 
- The chunks are embedded using the <b>OpenAI text-embedding-ada-002 model</b>. This model is trained on a massive dataset of text and code, which allows it to learn the relationships between words and phrases.

## 4) **Vector Store:**
- The embeddings are then stored in a **FAISS** vector store. FAISS is a library for efficient similarity search in dense vectors. 
- This allows the bot to quickly access the embeddings when it needs to answer a query.

## 5) **Query:** 
- The user then enters a query. This is a question that they want the bot to answer.

## 6) **Embeddings:** 
- The query is then embedded. This is done using the same embedding model that was used to embed the chunks.

## 7) **Semantic Search and Ranked Result:**
- By comparing the semantic similarity between the query embeddings and the chunk embeddings in the vector store, ranked results are returned.
- This helps to improve the accuracy and efficiency of the query answering process.
- Providing the model only the ranked results allows the model to focus on the most relevant results. This can improve the accuracy of the model's answer, as the model will not be distracted by irrelevant results.

## 8) **Memory:**
- The bot is provided with a **buffer memory** of the most recent queries and answers. This allows the bot to learn from its previous interactions with users and improve its ability to answer future queries.

## 9) **Answer:**
- Finally, the ranked results and buffer memory are passed to the LLM model(**GPT-3.5 turbo**) along with the user query to generate an answer.


