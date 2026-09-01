from sqlalchemy import create_engine

from app.core.config import settings
from app.db.connection import connector


def getconn():
    return connector.connect(
        settings.cloud_sql_instance,
        "pg8000",
        user=settings.database_user,
        password=settings.database_password,
        db=settings.database_name,
        ip_type="public",
    )


engine = create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)