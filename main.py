import mysql.connector

try:
    # connect to local db
    connection = mysql.connector.connect(
        user="root",
        password="",
        host="127.0.0.1",
        database="bookstore"
    )

    if connection.is_connected():
        print("connection success")
    
        q1 = '''SELECT c.id, c.name
                FROM customers c
                JOIN invoices i ON c.id = i.customer_id
                JOIN (
                    SELECT invoice_id, SUM(quantity) AS total_quantity
                    FROM invoice_lines
                    GROUP BY invoice_id
                    HAVING total_quantity > 5
                ) il ON i.id = il.invoice_id'''
        
        q2 = '''SELECT c.id, c.name
                FROM customers c
                LEFT JOIN invoices i ON c.id = i.customer_id
                WHERE i.customer_id IS NULL'''
        
        q3 = '''SELECT il.id, il.description, c.name
                FROM customers c
                JOIN invoices i ON c.id = i.customer_id
                JOIN invoice_lines il ON i.id = il.invoice_id'''
        
        try :
            # question 2b
            cursor = connection.cursor()
            cursor.execute(q1)

            rows = cursor.fetchall()

            print("question 2b")
            for row in rows:
                print(row)

            # question 2c
            cursor.execute(q2)

            rows = cursor.fetchall()

            print("question 2c")
            for row in rows:
                print(row)

            # question 2d
            cursor.execute(q3)

            rows = cursor.fetchall()

            print("question 2d")
            for row in rows:
                print(row)

            # close cursor
            cursor.close()
        except mysql.connector.Error as e:
            print(e)

        # close db connection
        connection.close()

except mysql.connector.Error as e:
    print(e)
