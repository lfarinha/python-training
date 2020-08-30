import pandas
import pyodbc


class Connection:

    def __init__(self, server=None, database=None, user=None, password=None):
        try:
            connection_string = ("Driver={ODBC Driver 17 for SQL Server};"
                               f"Server={server};Database={database};UID={user};PWD={password}")
            self.connection = pyodbc.connect(connection_string)
        except Exception as e:
            print('oops en la conexion')

    def select(self, query):
        try:
            data = pandas.read_sql(query, self.connection)
            return data.to_dict(orient='records')
        except Exception as e:
            print('oops en el query')

    def execute(self, query):
        try:
            self.connection.execute(query)
            self.connection.commit()
        except Exception as e:
            print('oops en el query')
