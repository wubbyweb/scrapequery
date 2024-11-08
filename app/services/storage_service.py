import os
from supabase import create_client, Client

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def store_embeddings(embeddings):
    response = supabase.table("embeddings").insert({"embedding": embeddings}).execute()
    return response

def match_embeddings(query_embedding):
    response = supabase.rpc("match_embeddings", {"query_embedding": query_embedding}).execute()
    return response.data