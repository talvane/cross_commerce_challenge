import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_EXTRACT: str

    class Config:
        env_prefix = ''
        env_file = os.path.expanduser('~/.env')
