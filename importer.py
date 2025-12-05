from pathlib import Path
import csv
from database import get_server_connection, get_connection

TABLE_ORDER = [
    "User",
    "AgentCreator",
    "AgentClient",
    "BaseModel",
    "CustomizedModel",
    "Configuration",
    "InternetService",
    "LLMService",
    "DataStorage",
    "ModelServices",
    "ModelConfigurations",
]


class Importer:
    def __init__(self, path: str):
        self.path = Path(path)

    def _run_ddl(self):
        conn = get_server_connection()
        cur = conn.cursor()
        try:
            with open("project.sql", "r") as ddl_file:
                ddl = ddl_file.read()
            statements = ddl.split(";")
            for stmt in statements:
                stmt = stmt.strip()
                if not stmt:
                    continue
                cur.execute(stmt)
            conn.commit()
        finally:
            cur.close()
            conn.close()

    def _import_table_csv(self, cursor, table_name: str):
        csv_path = self.path / f"{table_name}.csv"
        if not csv_path.exists():
            return
        with open(csv_path, newline="") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            rows = list(reader)
        if not rows:
            return
        num_cols = len(rows[0])
        placeholders = ",".join(["%s"] * num_cols)
        sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
        cursor.executemany(sql, rows)

    def import_from_path(self) -> bool:
        conn = None
        cur = None
        try:
            self._run_ddl()
            conn = get_connection()
            cur = conn.cursor()
            for table in TABLE_ORDER:
                self._import_table_csv(cur, table)
            conn.commit()
            return True
        except Exception as e:
            print("Import error:", e)
            if conn is not None:
                conn.rollback()
            return False
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
