import psycopg2
from psycopg2 import sql

try:
    connection=psycopg2.connect(
        host='ep-floral-term-33683890.us-east-2.aws.neon.fl0.io',
        user='fl0user',
        password= 'Sk0JKzr2BVMg',
        database= 'FacialRecognition'
    )
    print ('Conexión exitosa')
    
    cursor = connection.cursor()

    # Definir la sentencia SQL para el insert
    sql_insert = sql.SQL("""
        INSERT INTO FacialRecognition (id, genero, edad, emocion, raza)
        VALUES (%s, %s, %s, %s, %s)
    """)

    # Valores que deseas insertar
    valores = ('3', 'Hombre', 'Adulto', 'Enojado', 'Latino')

    # Ejecutar la sentencia SQL
    cursor.execute(sql_insert, valores)

    # Confirmar la transacción
    connection.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
except Exception as ex:
    print(ex)
    
