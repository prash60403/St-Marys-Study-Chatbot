# RAG-Based Educational Chatbot

## Introduction

This project is a RAG (Retrieval-Augmented Generation) based educational chatbot developed using Python, LangChain, ChromaDB, Hugging Face embeddings, and Streamlit. The chatbot is trained using Second PU textbooks such as Python, Physics, Chemistry, and Mathematics. Instead of depending completely on pre-trained Large Language Models, the chatbot retrieves answers directly from the uploaded textbook content and provides subject-related responses to students.

The system converts textbook content into vector embeddings and stores them in a vector database. Whenever a student asks a question, the chatbot retrieves the most relevant textbook information and generates accurate answers based on the educational content.

---

# Project Workflow

The project workflow begins with setting up the development environment and database system. Initially, a GitHub repository is created to manage the project source code, and the repository is cloned into the local Visual Studio Code environment for development.

After setting up the repository, a `requirements.txt` file is created to store all required Python libraries and dependencies. These libraries are then installed to prepare the environment for the chatbot application.

The project structure is organized into different folders such as `src` and `textbook`. The `textbook` folder contains all the educational PDF textbooks required for training the RAG-based chatbot. These textbooks include subjects such as Python, Physics, Chemistry, and Mathematics.

Inside the `src` folder, vectorization scripts are created to process and convert textbook content into vector embeddings. Vectorization helps transform textual information into numerical vector format so that machine learning models can understand and retrieve relevant information efficiently. This vector-based retrieval system improves chatbot accuracy and forms the foundation of the RAG architecture.

---

# Textbook Processing and Vectorization

The `vectorized_book.py` file is responsible for processing textbook content and converting it into embeddings. This module initializes all required libraries including LangChain, Hugging Face embedding models, text splitters, and Chroma vector database.

Environment variables are loaded inside this module to manage important configurations such as Groq API keys, textbook file paths, and vector database locations. Different directories such as working directory, parent directory, vector database directory, and chapter vector database directory are initialized for proper project organization.

The Hugging Face embedding model is then initialized to convert textbook text into vector embeddings. These embeddings help represent textual data numerically so that semantic similarity searches can be performed efficiently.

Text splitting techniques are used to divide large textbook content into smaller chunks before embedding generation. This improves retrieval performance and helps the chatbot locate accurate information quickly.

The project contains functions such as `vectorize_book_and_store_to_database`, which converts entire textbook data into vector embeddings and stores them subject-wise inside the vector database. Another function called `vectorize_chapters` stores vector embeddings chapter-wise, allowing students to access chapter-specific question answering and learning support.

---

# Vectorization Script

The `vectorized_script.py` file acts as the execution script for the vectorization process. This script helps run the vectorization functions automatically and generates vector database files from textbook content.

When executed, the script reads textbook PDFs, converts them into vector embeddings using the embedding model, and stores them inside the Chroma vector database. This database becomes the retrieval system used by the chatbot during question answering.

---

# Chat Utility Functions

The `chat_utility.py` file contains helper functions used throughout the chatbot application.

The `GetChapterList` function helps retrieve available chapters from the stored database so that students can access subject-wise and chapter-wise content easily.

Another utility function is used for YouTube video recommendations. Based on the student’s query, the chatbot can recommend related educational YouTube videos to improve learning support and provide additional study resources.

---

# Main Application Pipeline

The `main.py` file acts as the central pipeline of the chatbot application. This file integrates all modules together and controls the complete chatbot workflow.

Initially, all required libraries and environment variables are loaded. Helper functions are used to set up the vector database and initialize the chatbot retrieval chain.

The `GetVectorDatabasePath` function retrieves the correct vector database path for the selected subject or chapter.

Next, the `SetUpChain` function initializes the embedding model, vector store, language model, and conversation memory. The embedding model helps retrieve relevant textbook chunks, while the vector store performs semantic similarity search on stored embeddings.

The chatbot uses the Groq LLM model for generating final responses. Conversation memory is initialized to maintain context during continuous interactions with students.

The system uses a `Conversational Retrieval Chain`, which combines retrieval and generation together. This chain retrieves relevant textbook embeddings from the vector database and passes them to the language model to generate accurate educational responses.

The retrieval chain includes several important parameters such as:

* Language model
* Conversation memory
* Retriever
* Chain type
* Return source documents
* Chat history management

These parameters help maintain conversational context and improve the quality of generated answers.

---

# Streamlit Chatbot Interface

The chatbot frontend interface is developed using Streamlit.

Inside the Streamlit application, page configurations and chatbot titles are initialized to create a clean educational chatbot interface.

The application includes functionalities such as:

* Displaying previous chat messages
* Managing user input fields
* Showing chatbot responses
* Maintaining chat history
* Handling conversation flow dynamically

Students can type questions related to their Second PU subjects, and the chatbot retrieves accurate answers directly from textbook content.

---

# Running the Application

After completing the setup and vectorization process, the chatbot application is executed using Streamlit. Running the main application starts the educational chatbot interface, allowing students to interact with the system and test subject-related question answering.

The chatbot retrieves textbook-based information instead of depending only on pretrained AI knowledge, making responses more syllabus-oriented and educationally accurate.

---

# Technologies Used

| Technology   | Purpose                                   |
| ------------ | ----------------------------------------- |
| Python       | Backend development                       |
| LangChain    | RAG pipeline and retrieval chain          |
| Hugging Face | Embedding model generation                |
| ChromaDB     | Vector database storage                   |
| Groq LLM     | AI response generation                    |
| Streamlit    | Frontend chatbot interface                |
| GitHub       | Version control and repository management |

---

# Advantages of the Project

* Provides textbook-based accurate answers
* Supports subject-wise and chapter-wise retrieval
* Uses vector embeddings for semantic search
* Improves educational learning support
* Maintains conversational memory
* Recommends related educational YouTube videos
* Uses scalable RAG architecture
* Interactive and user-friendly chatbot interface

---

# Conclusion

This project successfully demonstrates the implementation of a RAG-based educational chatbot using textbook data from Second PU subjects. By combining vector embeddings, retrieval systems, language models, and conversational memory, the chatbot provides accurate and syllabus-focused educational assistance to students.

The system improves learning by retrieving answers directly from textbook content instead of relying completely on pretrained AI models. The modular architecture and vector database integration make the project scalable, efficient, and suitable for future enhancements such as voice support, multilingual learning, student authentication, and cloud deployment.
