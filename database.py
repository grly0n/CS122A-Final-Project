import mysql.connector

MYSQL_PASSWORD = ""
MYSQL_SOCKET = "/tmp/mysql.sock"
DB_NAME = "cs122a"

DB_CONFIG = {
    "user": "test",
    "password": "password",
    # "unix_socket": MYSQL_SOCKET
}


def get_server_connection():
    return mysql.connector.connect(**DB_CONFIG)


def get_connection():
    return mysql.connector.connect(database=DB_NAME, **DB_CONFIG)
