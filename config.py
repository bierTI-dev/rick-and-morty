import os


mongo = {
    "db_name": os.getenv('MONGO_DBNAME', "rick-n-morty"),
    "connection_url": os.getenv('MONGO_CONN_URL'),
}
