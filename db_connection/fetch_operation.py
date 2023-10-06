from db_connection.db_connection_python import get_db_connection

db_connector = get_db_connection()

db_cursor = db_connector.cursor()
db_cursor.execute("select * from employee")
# print(db_cursor)
# for r in db_cursor:
#     print(r)

# first_record = db_cursor.fetchone()
# print(f"the first record only {first_record}")

all_records = db_cursor.fetchall()
print(f'all records {all_records}')
