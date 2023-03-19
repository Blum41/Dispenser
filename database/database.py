from supabase import Client, create_client
from os import getenv


class Database:
    def __init__(self):
        self.client: Client = create_client(
            supabase_url=getenv("SUPABASE_URL"),
            supabase_key=getenv("SUPABASE_ANON_KEY")
        )
        print(getenv("SUPABASE_ANON_KEY"))
        print("zv")
        user = self.client.auth.sign_in_with_password({
            "email": "remi.alban@insa-cvl.fr",
            "password": "password"
        })
        print("ac")
        self.client.postgrest.auth(user.session.access_token)
