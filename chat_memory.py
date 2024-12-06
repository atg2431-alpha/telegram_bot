import chromadb
from chromadb.config import Settings
from datetime import datetime

client = chromadb.PersistentClient(path="./chroma")

collection = client.get_or_create_collection("chat_memory")

def store_message(chat_id: str,message: str) -> None:
    """It will store the messages"""
    collection.add(
        documents=[message],
        metadatas=[{"chat_id": chat_id, "time": datetime.now().isoformat()}],
        ids = [f"{chat_id}_{datetime.now().timestamp()}"]
    )

def retrieve_messages(chat_id: str, n: int = 3) -> list:
    """Retrieve the most recent n messages for a chat."""
    results = collection.get(where={"chat_id": chat_id})
    if results["documents"]:
        messages = results["documents"][-n:]  # Get the most recent n messages
        return messages
    return []

def clear_memory(chat_id: str) -> None:
    """Clear all messages for a given chat."""
    collection.delete(where={"chat_id": chat_id})