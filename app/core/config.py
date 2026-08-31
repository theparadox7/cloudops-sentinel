from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CloudOps Sentinel"
    app_env: str = "development"
    debug: bool = True
    database_url: str = ""
    
    database_name: str
    database_user: str
    database_password: str
    cloud_sql_instance: str
    

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()