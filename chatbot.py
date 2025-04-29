from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class Chatbot:
    def __init__(self, pdf_texts):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Modelo para embeddings
        self.pdf_texts = pdf_texts
        self.embeddings = self.create_embeddings(pdf_texts)
        self.index = self.create_index(self.embeddings)

    def create_embeddings(self, texts):
        # Cria embeddings a partir do texto
        return self.model.encode(texts, convert_to_tensor=True)

    def create_index(self, embeddings):
        # Cria um índice FAISS para busca
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)  # Criação do índice de similaridade
        index.add(np.array(embeddings))  # Adiciona os embeddings ao índice
        return index

    def get_answer(self, query):
        # Converte a pergunta em embedding
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, k=1)  # Busca pela resposta mais próxima
        return self.pdf_texts[indices[0][0]]  # Retorna o texto mais próximo
