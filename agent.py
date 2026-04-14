from agno.agent import Agent
from agno.knowledge.embedder.google import GeminiEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.models.google import Gemini
from agno.vectordb.pgvector import PgVector  # Change this import
import os

os.environ["GOOGLE_API_KEY"] = "your_google_api_key_here"  # Set your Google API key as an environment variable
# Database Connection String
# Format: "postgresql+psycopg://user:password@host:port/dbname"
db_url = "postgresql+psycopg://postgres:Ankitabhagwat@localhost:5432/OnlinePaymentFraudAgentDB"

knowledge = Knowledge(
    vector_db=PgVector(
        table_name="app_guide_embeddings",
        db_url=db_url,
        embedder=GeminiEmbedder(),
    ),
)

# Load your text file
# Note: Ensure the table is created before inserting
knowledge.insert(path="C:\\Users\\ankita bhagwat\\OneDrive - Vsky Solutions\\OnlinePaymentFraudDetection\\knowledgebase.txt")

agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    knowledge=knowledge,
    instructions=[
        "Search your knowledge base to help users understand how to use the GuardAI application.",
        "Explain transaction fields like 'Receiver' and 'Sender' in simple terms.",
        "Provide step-by-step guidance for analyzing a transaction."
    ],
    markdown=True,
)

# agent.print_response("How do I get started with the application?", stream=True)