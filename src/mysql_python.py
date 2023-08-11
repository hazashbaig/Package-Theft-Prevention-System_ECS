import mysql.connector
import json

sql_conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "ecs"
    )

def display_data(): 
    global sql_conn
    
    object = sql_conn.cursor()

    query = "SELECT orders FROM barcode"
    object.execute(query)


    rows = object.fetchall()

    for row in rows:
        for data in row:
            print(data)
            print(type(data))

# display_data(sql_conn)

def get_all_orders():
    global sql_conn
    cursor = sql_conn.cursor()

    # Fetch data from the "barcode" table
    query = "SELECT orders FROM barcode"
    cursor.execute(query)
    result = cursor.fetchall()

    orders = []
    # Process JSON data
    for row in result:
        orders_bytes = row[0]  # Assuming the retrieved data is in bytes
        orders_str = orders_bytes.decode('utf-8')  # Convert bytes to string
        orders_data = json.loads(orders_str)

        order_ids = orders_data.get("Orders", [])
        
        for order in order_ids:
            orders.append(order)


    return orders

def student_orders(reg_no):
    global sql_conn
    cursor = sql_conn.cursor()

    # Fetch data from the "barcode" table
    query = f"SELECT orders FROM barcode WHERE regno = '{reg_no}'"
    cursor.execute(query)
    result = cursor.fetchall()

    # Process JSON data
    for row in result:
        orders_bytes = row[0]  # Assuming the retrieved data is in bytes
        orders_str = orders_bytes.decode('utf-8')  # Convert bytes to string
        orders_data = json.loads(orders_str)

        order_ids = orders_data.get("Orders", [])

    return order_ids
    
def delete_order_for_student(student_reg_no, order_no):
    global sql_conn
    cursor = sql_conn.cursor()

    # Fetch data from the "barcode" table for the specified student
    query = f"SELECT orders FROM barcode WHERE regno = '{student_reg_no}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        orders_bytes = result[0]  # Assuming the retrieved data is in bytes
        orders_str = orders_bytes.decode('utf-8')  # Convert bytes to string
        orders_data = json.loads(orders_str)

        order_ids = orders_data.get("Orders", [])

        if order_no in order_ids:
            order_ids.remove(order_no)
            orders_data["Orders"] = order_ids

            # Update the record in the database
            update_query = f"UPDATE barcode SET orders = '{json.dumps(orders_data)}' WHERE regno = '{student_reg_no}'"
            cursor.execute(update_query)
            sql_conn.commit()

            print(f"Order {order_no} removed for student with regno {student_reg_no}")
        else:
            print(f"Order {order_no} not found for student with regno {student_reg_no}")
    else:
        print(f"Student with regno {student_reg_no} not found.")

