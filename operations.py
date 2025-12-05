from typing import List
import csv
import mysql.connector
from database import get_connection

def _print_table(rows):
    for row in rows:
        print(",".join(str(col) for col in row))

# Q2 insertAgentClient
def insert_agent_client(uid: int, username: str, email: str,
                        card_number: int, card_holder: str,
                        expiration_date: str, cvv: int, zip_code: int,
                        interests: str) -> None:
    conn = get_connection()
    try:
        cur = conn.cursor()
        # Insert into User
        cur.execute(
            "INSERT INTO User (uid, email, username) VALUES (%s, %s, %s)",
            (uid, email, username),
        )

        # Insert into AgentClient
        cur.execute(
            """
            INSERT INTO AgentClient
            (uid, interests, cardholder, expire, cardno, cvv, zip)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (uid, interests, card_holder, expiration_date,
             card_number, cvv, zip_code),
        )

        conn.commit()
        print("Success")
    except mysql.connector.Error as e:
        print(e)
        conn.rollback()
        print("Fail")
    finally:
        cur.close()
        conn.close()

# Q3 addCustomizedModel
def add_customized_model(mid: int, bmid: int) -> None:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO CustomizedModel (bmid, mid) VALUES (%s, %s)",
            (bmid, mid),
        )
        conn.commit()
        print("Success")
    except mysql.connector.Error:
        conn.rollback()
        print("Fail")
    finally:
        cur.close()
        conn.close()

# Q4 deleteBaseModel
def delete_base_model(bmid: int) -> None:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM BaseModel WHERE bmid = %s", (bmid,))
        conn.commit()
        if cur.rowcount > 0:
            print("Success")
        else:
            print("Fail")
    except mysql.connector.Error:
        conn.rollback()
        print("Fail")
    finally:
        cur.close()
        conn.close()

# Q5 listInternetService
def list_internet_service(bmid: int) -> None:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT i.sid, i.endpoints AS endpoint, i.provider
            FROM ModelServices ms
            JOIN InternetService i ON ms.sid = i.sid
            WHERE ms.bmid = %s
            ORDER BY i.provider ASC
            """,
            (bmid,),
        )
        rows = cur.fetchall()
        _print_table(rows)
    finally:
        cur.close()
        conn.close()

# Q6 countCustomizedModel
def _parse_bmid_list(bmid_arg: str) -> List[int]:
    s = bmid_arg.strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
        return [int(x.strip()) for x in s.split(",") if x.strip()]
    else:
        return [int(s)]

def count_customized_model(bmid_arg: str) -> None:
    bmid_list = _parse_bmid_list(bmid_arg)
    placeholders = ",".join(["%s"] * len(bmid_list))

    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            f"""
            SELECT b.bmid, b.description,
                   COUNT(c.mid) AS customizedModelCount
            FROM BaseModel b
            LEFT JOIN CustomizedModel c
                   ON b.bmid = c.bmid
            WHERE b.bmid IN ({placeholders})
            GROUP BY b.bmid, b.description
            ORDER BY b.bmid ASC
            """,
            tuple(bmid_list),
        )
        rows = cur.fetchall()
        _print_table(rows)
    finally:
        cur.close()
        conn.close()

# Q7 topNDurationConfig
def top_n_duration_config(uid: int, N: int) -> None:
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT ac.uid,
                   c.cid,
                   c.labels AS label,
                   c.content,
                   MAX(mc.duration) AS duration
            FROM AgentClient ac
            JOIN Configuration c ON c.client_uid = ac.uid
            JOIN ModelConfigurations mc ON mc.cid = c.cid
            WHERE ac.uid = %s
            GROUP BY ac.uid, c.cid, c.labels, c.content
            ORDER BY duration DESC, c.cid ASC
            LIMIT %s
            """,
            (uid, N),
        )
        rows = cur.fetchall()
        _print_table(rows)
    finally:
        cur.close()
        conn.close()

# Q8 listBaseModelKeyword
def list_base_model_keyword(keyword: str) -> None:
    conn = get_connection()
    try:
        cur = conn.cursor()
        like_pattern = f"%{keyword}%"
        cur.execute(
            """
            SELECT DISTINCT b.bmid,
                            i.sid,
                            i.provider,
                            l.domain
            FROM BaseModel b
            JOIN ModelServices ms ON b.bmid = ms.bmid
            JOIN InternetService i ON ms.sid = i.sid
            JOIN LLMService l ON i.sid = l.sid
            WHERE l.domain LIKE %s
            ORDER BY b.bmid ASC
            LIMIT 5
            """,
            (like_pattern,),
        )
        rows = cur.fetchall()
        _print_table(rows)
    finally:
        cur.close()
        conn.close()

# Q9 printNL2SQLresult
def print_nl2sql_result() -> None:
    with open("nl2sql_results.csv", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print(",".join(row))
