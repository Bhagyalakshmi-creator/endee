import streamlit as st
from sentence_transformers import SentenceTransformer
from endee_client import EndeeClient
from openai import OpenAI

# Initialize
st.set_page_config(page_title="DocuFast - Powered by Endee")
client = EndeeClient()
model = SentenceTransformer('all-MiniLM-L6-v2') # 384 dimensions
llm_client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

st.title("🚀 DocuFast: Semantic Search with Endee")

# 1. Setup Index
if st.button("Initialize Endee Index"):
    res = client.create_index("docs_index", dimension=384)
    st.success(f"Index created: {res}")

# 2. Upload and Index
uploaded_file = st.file_uploader("Upload a text file", type=['txt'])
if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    # Simple chunking
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    
    with st.spinner("Indexing into Endee..."):
        vectors = model.encode(chunks).tolist()
        metadata = [{"text": c} for c in chunks]
        client.insert("docs_index", vectors, metadata)
    st.success("Indexed successfully!")

# 3. Chat / Query
query = st.text_input("Ask a question about your document:")
if query:
    # Vector Search
    query_vec = model.encode([query])[0].tolist()
    search_results = client.search("docs_index", query_vec, top_k=3)
    
    # Context Building
    context = "\n".join([res['metadata']['text'] for res in search_results['hits']])
    
    # RAG - Generate Answer
    response = llm_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer based on the context provided."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
        ]
    )
    st.write("### Answer:")
    st.write(response.choices[0].message.content)
