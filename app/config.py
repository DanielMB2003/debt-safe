from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Debt Pro Calculator"
    app_env: str = "development"


settings = Settings()