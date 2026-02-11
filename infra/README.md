🧐 Overview
This solves the problem of "information overload" by allowing users to upload vast amounts of text or PDF data and query it using natural language. Unlike traditional keyword search, DocuFast uses Semantic Search to understand the intent behind a query.
The core of this project is Endee, which handles the high-dimensional vector indexing and similarity search with extreme efficiency.
✨ Key Features
Instant Indexing: Rapidly convert documents into vector embeddings.
SIMD Accelerated Search: Uses Endee’s hardware-level optimizations (AVX2/Neon) for lightning-fast retrieval.
RAG Workflow: Integrates with OpenAI/Ollama to provide accurate, grounded answers.
Modern UI: A clean Streamlit interface for document management and chatting.
🏗 Architecture
Ingestion: User uploads a document 
 Text is chunked 
 sentence-transformers generates 384-dimension embeddings.
Storage: Embeddings are stored in the Endee Vector Database via REST API.
Retrieval: User asks a question 
 Question is vectorized 
 Endee performs a Cosine Similarity search.
Generation: Top-k results are sent as context to an LLM (GPT-4o) to generate a final answer.
🛠 Tech Stack
Vector Database: Endee (Forked & Optimized)
Embeddings: all-MiniLM-L6-v2 (Sentence-Transformers)
LLM: OpenAI GPT-4o-mini (or Ollama for local setups)
Frontend: Streamlit
Backend: Python 3.10+
🚀 Getting Started
Prerequisites
Docker & Docker Compose
Python 3.10 or higher
An OpenAI API Key (Optional: for the Generation part)
1. Setting up Endee
The easiest way to run the Endee server is using Docker.
code
Bash
# Clone the repository (including the Endee fork)
git clone --recursive https://github.com/[YOUR_GITHUB_USERNAME]/docufast.git
cd docufast

# Start the Endee Vector Database
docker run -d \
  -p 8080:8080 \
  -v endee-data:/data \
  --name endee-server \
  endeeio/endee-server:latest
2. Setting up the Application
code
Bash
# Install dependencies
pip install -r requirements.txt

# Set your API Key
export OPENAI_API_KEY='your-api-key-here'

# Run the Streamlit app
streamlit run src/app.py
💡 Usage
Initialize Index: Click the "Initialize Endee Index" button on the sidebar.
Upload Data: Drag and drop a .txt or .pdf file.
Search & Chat: Type a question in the chat box. DocuFast will retrieve the most relevant sections from Endee and answer based on that context.
⚡ Why Endee?
During the development of DocuFast, Endee was chosen over other vector databases for several reasons:
Performance: Its native implementation in C++ with SIMD (Single Instruction, Multiple Data) support ensures that search latency remains low even as the dataset grows.
Efficiency: The ndd binary is lightweight and high-performance, making it ideal for high-throughput AI agents.
Developer Friendly: The REST API is intuitive, allowing for quick integration into Python-based AI workflows.
📂 Project Structure
code
Text
.
├── infra/              # Contains the Endee submodule/fork
├── src/
│   ├── app.py          # Main UI and logic
│   ├── endee_client.py # Custom wrapper for Endee API
│   └── utils.py        # Text processing & embedding helpers
├── requirements.txt    # Python packages
├── docker-compose.yml  # Deployment configuration
└── README.md           # You are here!
🤝 Contributing
Contributions are welcome! Please fork the repository and submit a Pull Request.
