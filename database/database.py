from supabase import Client, create_client
from os import getenv


class Database:
    def __init__(self):
        try:
            self.client: Client = create_client(
                supabase_url=getenv("SUPABASE_URL"),
                supabase_key=getenv("SUPABASE_ANON_KEY")
            )
        except:
            pass
