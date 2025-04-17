import csv
import psycopg2
from config import load_config
from connect import get_connect

#Search by Pattern
def search_by_pattern(config):
    conn = get_connect(config)
    cur = conn.cursor()
    pattern = input("Enter search pattern (part of name or phone): ")
    query = """
        SELECT id, name, phone 
        FROM PhoneBook 
        WHERE name ILIKE %s OR phone ILIKE %s
    """
    like_pattern = f"%{pattern}%"
    cur.execute(query, (like_pattern, like_pattern))
    records = cur.fetchall()
    if records:
        print("\nMatching records:")
        for record in records:
            print(f"ID: {record[0]}, Name: {record[1]}, Phone: {record[2]}")
    else:
        print("No matching records found.")
    cur.close()
    conn.close()

def main():
    config = load_config()
    print("Search by pattern")

    search_by_pattern(config)

if __name__ == '__main__':
    main()
