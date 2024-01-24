import os

DATABASE_NAME = os.getenv('DATABASE_NAME') if os.getenv('DATABASE_NAME') is not None else "test"
DATABASE_IP = os.getenv('DATABASE_IP') if os.getenv('DATABASE_IP') is not None else "localhost"
DATABASE_PORT = os.getenv('DATABASE_PORT') if os.getenv('DATABASE_PORT') is not None else "5432"
DATABASE_USER = os.getenv('DATABASE_USER') if os.getenv('DATABASE_USER') is not None else "postgres"
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD') if os.getenv('DATABASE_PASSWORD') is not None else "root"
