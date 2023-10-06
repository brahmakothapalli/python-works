from db_connection.db_connection_python import get_db_connection

db_connector = get_db_connection()

db_cursor = db_connector.cursor()

delete_query = "delete from employee where Id='555'"

db_cursor.execute(delete_query)

db_connector.commit()

db_connector.close()
