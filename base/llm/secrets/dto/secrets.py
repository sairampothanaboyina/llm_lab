import os
from dotenv import load_dotenv

class Secret:

    OPENAI_API_KEY: str
    def __init__(self):
        load_dotenv(override=True)
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

