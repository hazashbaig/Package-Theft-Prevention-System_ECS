import mysql.connector
import json

sql_conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "ecs"
    )

def display_data(sql_conn): 
    
    object = sql_conn.cursor()

    query = "SELECT orders FROM barcode"
    object.execute(query)


    rows = object.fetchall()

    for row in rows:
        for data in row:
            print(data)
            print(type(data))

# display_data(sql_conn)

def get_student_orders(sql_conn):
    cursor = sql_conn.cursor()

    # Fetch data from the "barcode" table
    query = "SELECT orders FROM barcode"
    cursor.execute(query)
    result = cursor.fetchall()

    # Process JSON data
    for row in result:
        orders_bytes = row[0]  # Assuming the retrieved data is in bytes
        orders_str = orders_bytes.decode('utf-8')  # Convert bytes to string
        print(orders_str)
        print(type(orders_str))
        # orders_data = json.loads(orders_str)

        # order_ids = orders_data.get("Orders", [])

        # # Process each order ID
        # for order_id in order_ids:
        #     print("Order ID:", order_id)

get_student_orders(sql_conn)

    
    
