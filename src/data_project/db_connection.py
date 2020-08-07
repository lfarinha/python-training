import pyodbc


def connect():
    driver = 'ODBC Driver 17 for SQL Server'
    server = '192.168.1.189'
    database = 'flask'
    user = 'sa'
    password = '40634630Leo*'
    cnxn = pyodbc.connect(
        f"DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}"
    )
    return cnxn.cursor()


def select():
    query = "SELECT * FROM dbo.covid_19_data"
    connection = connect()
    result = connection.execute(query)
    row = result.fetchone()
    print(row)


if __name__ == '__main__':
    select()
