from db_connection.db_connection_python import get_db_connection

db_connector = get_db_connection()

db_cursor = db_connector.cursor()

insert_query = "Insert into employee(Name, Role, Id, Salary) values(%s, %s, %s, %s)"
employee_details = [("venkat", "Sr QA", "333", 300000), ("naresh", "Sr Dev", "444", 250000), ("shiva", "Jr Dve",  "555", 150000)]

db_cursor.executemany(insert_query, employee_details)

db_connector.commit()

db_connector.close()

