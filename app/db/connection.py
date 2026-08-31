from google.cloud.sql.connector import Connector, IPTypes

from app.core.config import settings


connector = Connector()


def get_connection():
    connection = connector.connect(
        settings.cloud_sql_instance,
        "pg8000",
        user=settings.database_user,
        password=settings.database_password,
        db=settings.database_name,
        ip_type=IPTypes.PUBLIC,
    )

    return connection