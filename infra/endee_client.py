import requests

class EndeeClient:
    def __init__(self, base_url="http://localhost:8080", token=None):
        self.base_url = base_url
        self.headers = {"Authorization": token} if token else {}

    def create_index(self, index_name, dimension):
        url = f"{self.base_url}/api/v1/index/create"
        payload = {"name": index_name, "dimension": dimension, "metric": "cosine"}
        return requests.post(url, json=payload, headers=self.headers).json()

    def insert(self, index_name, vectors, metadata):
        url = f"{self.base_url}/api/v1/vector/insert"
        payload = {
            "index_name": index_name,
            "vectors": vectors, # List of floats
            "metadata": metadata # List of dicts
        }
        return requests.post(url, json=payload, headers=self.headers).json()

    def search(self, index_name, query_vector, top_k=5):
        url = f"{self.base_url}/api/v1/search"
        payload = {
            "index_name": index_name,
            "vector": query_vector,
            "top_k": top_k
        }
        return requests.post(url, json=payload, headers=self.headers).json()
