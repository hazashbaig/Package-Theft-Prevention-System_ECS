import mysql.connector
import json

sql_conn = mysql.connector.connect(
        host = "192.168.1.144",
        user = "root",
        password = "",
        database = "ecs"
    )

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
        print(order_ids)

        if order_no in order_ids:
            order_ids.remove(order_no)
            orders_data["Orders"] = order_ids

            # Update the record in the database
            update_query = f"UPDATE barcode SET orders = '{json.dumps(orders_data)}' WHERE regno = '{student_reg_no}'"
            cursor.execute(update_query)
            sql_conn.commit()

             # Insert into "orders delivered" table
            insert_query = f"INSERT INTO `orders delivered` (regno, order_no) VALUES ('{student_reg_no}', '{order_no}')"
            cursor.execute(insert_query)
            sql_conn.commit()

            print(f"Order {order_no} marked as delivered for student {student_reg_no}")
        else:
            print(f"Order {order_no} not found for student with regno {student_reg_no}")
    else:
        print(f"Student with regno {student_reg_no} not found.")

def enterText():
    review = input("Please enter your review: ")
    return review

def storeReview(student_reg_no, review):
    global sql_conn
    cursor = sql_conn.cursor()

    # Insert the review into the "reviews" table with automatic timestamp
    insert_query = f"INSERT INTO reviews (regno, review) VALUES ('{student_reg_no}', '{review}')"
    cursor.execute(insert_query)
    sql_conn.commit()

    print("Review stored successfully!")

print(get_all_orders())