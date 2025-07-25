import os
from base.llm.secrets.const.secret_type import SecretType

class Secret:

    __SECRETS: dict[SecretType, str]

    def __init__(self):
        self.__SECRETS = {SecretType.CHATGPT: os.getenv("OPENAI_API_KEY")}

    def get_secret(self, secret_type: SecretType) -> str:
        if secret_type is None:
            raise ValueError(f"Secret type {secret_type} is not defined")
        return self.__SECRETS[secret_type]



