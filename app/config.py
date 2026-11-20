import os
from dotenv import load_dotenv 

# Load envoirment variables
load_dotenv()

class Settings:
    # ----- GEMINI EMBEDDINGS ----- 
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    # ----- VECTOR DB (QDRANT) ----- 
    QUDRANT_API_KEY = os.getenv('QUDRANT_API_KEY')
    QUDRANT_URL = os.getenv('QUDRANT_CLUSTER_ENDPOINT')
    QDRANT_COLLECTION = "production_rag"

    # ----- REASONING ENGINE -----
    GROQ_API_KEY = os.getenv('GROQ_API_KEY') 
    GROQ_FALLBACK_API_KEY = os.getenv('GROQ_FALLBACK_API_KEY')
    GROQ_MODEL = "llama-3.3-70b-versatile"

    # ----- LLM GATEWAY -----
    PORTKEY_API_KEY = os.getenv('PORTKEY_API_KEY')
    GROQ_SLUG =  "rag"     # primary: @rag/llama-3.3-70b-versatile
    GROQ_SLUG_2 = "brag"  # fallback: @brag/llama-3.1-8b-instant

    # ----- OBSERVABILITY -----
    LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING", "true")
    LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
    LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT", "rag_scale_test")
    LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT", "https://api.smith.langchain.com")


settings = Settings()

# Apply LangChain environment variables for automatic tracing
os.environ["LANGCHAIN_TRACING_V2"] = settings.LANGSMITH_TRACING
os.environ["LANGCHAIN_API_KEY"] = settings.LANGSMITH_API_KEY or ""
os.environ["LANGCHAIN_PROJECT"] = settings.LANGSMITH_PROJECT
os.environ["LANGCHAIN_ENDPOINT"] = settings.LANGSMITH_ENDPOINT

