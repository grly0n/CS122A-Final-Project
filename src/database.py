import mysql.connector

# CHANGE THESE TWO VALUES:
MYSQL_PASSWORD = "Dary123"
MYSQL_SOCKET = "/tmp/mysql.sock"

DB_CONFIG = {
    "user": "root",
    "password": MYSQL_PASSWORD,
    "unix_socket": MYSQL_SOCKET,
}

DB_NAME = "final_project"


def get_server_connection():
    return mysql.connector.connect(**DB_CONFIG)


def get_connection():
    return mysql.connector.connect(database=DB_NAME, **DB_CONFIG)
