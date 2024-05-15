import fdb, pyodbc

def conectar_db(host, database='c:/syspdv/syspdv_srv.fdb'):
    connection = fdb.connect(host=host,
                      database=database,
                      user='SYSDBA',
                      password='masterkey',
                      charset='ISO8859_1')
    return connection

def conectar_db_sql(host, _db, user, pwd):
    #cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=localhost;DATABASE=syspdv;Trusted_Connection=yes;')
    #conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=syspdv;Trusted_Connection=yes;')
    conn = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={host};DATABASE={_db};UID={user};PWD={pwd};Encrypt=no;')
    return conn


