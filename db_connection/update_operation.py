from db_connection.db_connection_python import get_db_connection

db_connector = get_db_connection()

db_cursor = db_connector.cursor()

update_query = "Update employee SET Salary=500000 where Name='venkat'"

db_cursor.execute(update_query)

db_connector.commit()

db_connector.close()
