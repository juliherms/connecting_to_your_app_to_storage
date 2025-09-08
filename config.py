import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Classe de configuração da aplicação Flask.
    Carrega configurações de variáveis de ambiente com fallback para valores padrão.
    """
    
    # Configurações de Segurança
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Configurações do Banco de Dados SQL Server
    SQL_SERVER = os.getenv('SQL_SERVER')
    SQL_DATABASE = os.getenv('SQL_DATABASE')
    SQL_USER_NAME = os.getenv('SQL_USER_NAME')
    SQL_PASSWORD = os.getenv('SQL_PASSWORD')
    
    # Construção da URI de conexão do SQLAlchemy
    SQLALCHEMY_DATABASE_URI = (
        f'mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/'
        f'{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server&'
        f'trustServerCertificate=no&encrypt=yes'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configurações do Azure Blob Storage
    BLOB_ACCOUNT = os.getenv('BLOB_ACCOUNT')
    BLOB_STORAGE_KEY = os.getenv('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.getenv('BLOB_CONTAINER')

    @classmethod
    def init_app(cls, app):
        """
        Inicializa a aplicação Flask com as configurações.
        Pode ser usado para configurações específicas de ambiente.
        """
        pass
