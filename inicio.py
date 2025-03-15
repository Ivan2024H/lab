import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(host='localhost',
                                  user='postgres',
                                  password="gdb",
                                  database="Empresa")
    
    #connection = psycopg2.connect(user="postgres",
    #                              password="gdb",
    #                              host="127.0.0.1",
    #                              port="5432",
    #                              database="Empresa")
    connection.autocommit = True  
    # Create a cursor to perform database operations
    cursor = connection.cursor()
    '''
    # Print PostgreSQL details
    print("Informacion de la BD PostgreSQL ")
    print(connection.get_dsn_parameters(), "\n")
    '''
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("Estas conectado a - ", record, "\n")
    '''
    curclsor.execute("select * from activos")
    rows=cursor.fetchall()
    for row in rows:
          print(row)
    '''
 
    def insert_dato(v_id,v_nombre,v_costo):
       cursor = connection.cursor()
       query = f""" insert into activos(ID,nombre,costo) values ('{v_id}','{v_nombre}',{v_costo})"""
       cursor.execute(query)
    def valida_float(v_float):
        try:
            var = float(v_float)
            return True
        except(Exception, Error) as error:
            return False

    xv_id = input('Ingrese ID : ')
    xv_nombre = input('Ingrese Nombre : ')
    while True:
        xv_costo = input('Ingrese costo : ')
        if valida_float(xv_costo):
            break
      
    
    insert_dato(int(xv_id),xv_nombre,float(xv_costo))

except (Exception, Error) as error:
    print("Error al conectarse a PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL conecion cerrada")