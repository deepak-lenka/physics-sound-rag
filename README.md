# Physics Sound RAG System

This repository contains a Question Answering system for physics topics, particularly focused on sound. It uses a Retrieval-Augmented Generation (RAG) approach to provide accurate answers based on a curated dataset.

## Repository Link

https://github.com/deepak-lenka/physics-sound-rag.git

## Demo

https://x.com/iamdeepaklenka/status/1836090773219266858

Here's a quick demonstration of how the system works:
## Features

- Web-based interface for asking physics questions
- RAG system for retrieving relevant information
- FastAPI backend for efficient processing
- TF-IDF based retrieval system

## Models and Technologies Used

- **Sentence Transformer**: 'all-MiniLM-L6-v2' for creating embeddings
- **FAISS**: Facebook AI Similarity Search for efficient similarity search and clustering of dense vectors
- **TF-IDF Vectorizer**: From scikit-learn for text feature extraction
- **Cosine Similarity**: For measuring the similarity between query and text chunks
- **FastAPI**: For creating the web API
- **Jinja2**: For HTML templating
- **Axios**: For making HTTP requests from the frontend

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/deepak-lenka/physics-sound-rag.git
   cd physics-sound-rag
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Detailed Usage Steps

1. Prepare the data:
   - Ensure you have a text file named 'iesc111.txt' in the 'data' directory containing the physics content.

2. Process the text data:
   ```
   python src/process_text.py
   ```
   This script will:
   - Read the 'iesc111.txt' file
   - Split it into chunks
   - Save these chunks as JSON files in the 'data/chunks' directory

3. Create embeddings:
   ```
   python src/create_embeddings.py
   ```
   This script will:
   - Load the text chunks
   - Use the 'all-MiniLM-L6-v2' model to create embeddings
   - Create a FAISS index with these embeddings
   - Save the FAISS index and the text chunks for later use

4. Run the FastAPI server:
   ```
   uvicorn main:app --host 0.0.0.0 --port 8002
   ```
   This will start the server and the RAG system will be initialized, loading the saved embeddings and creating the TF-IDF matrix.

5. Open a web browser and navigate to `http://localhost:8002` to use the application.
   - Enter your physics question in the input field
   - Click "Ask" to submit your query
   - The system will retrieve relevant information and display the answer

## How It Works

1. When a query is submitted, the RAG system uses TF-IDF and cosine similarity to find the most relevant text chunks.
2. The system then extracts the most relevant sentences from these chunks based on the query.
3. The extracted information is used to formulate a response to the user's question.

## Project Structure

- `src/`: Contains the Python source files
  - `process_text.py`: Processes the raw text data
  - `create_embeddings.py`: Creates embeddings for the processed text
  - `rag_system.py`: Implements the RAG system
- `static/`: Contains static files (CSS)
- `templates/`: Contains HTML templates
- `main.py`: FastAPI application entry point
- `requirements.txt`: List of Python dependencies
- `data/`: Directory for storing the input text file and processed data

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE)

## Acknowledgements

- This project uses the 'all-MiniLM-L6-v2' model from the Sentence Transformers library.
- FAISS library by Facebook AI Research.
- FastAPI framework for building APIs with Python.
