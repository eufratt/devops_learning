import os
import time

import psycopg


def get_message():
    return "DevOps app is running"


def check_database():
    with psycopg.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", "5432")),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            return cursor.fetchone()[0] == 1


def run():
    if check_database():
        print("Database connection OK", flush=True)

    while True:
        print(get_message(), flush=True)
        time.sleep(5)


if __name__ == "__main__":
    run()
