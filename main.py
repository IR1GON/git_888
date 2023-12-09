import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="root",
    host="127.0.0.1",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
    INSERT INTO products (title, price, warranty_period_days)
    VALUES 
    ('Product 1 no sugar', 60, 20),
    ('Product 2 no sugar', 55, NULL),
    ('Product 3 with sugar', 40, 30),
    ('Product 4 no sugar', 70, 15),
    ('Product 5 with sugar', 30, NULL),
    ('Product 6 no sugar', 80, 25),
    ('Product 7 with sugar', 45, NULL)
    -- and other entries
""")
conn.commit()

cur.execute("SELECT * FROM products WHERE price > 50")
result_1 = cur.fetchall()
print("Products with price greater than 50:")
for row in result_1:
    print(row)

cur.execute("SELECT * FROM products WHERE warranty_period_days = 20")
result_2 = cur.fetchall()
print("\nProducts with a 20-day warranty period:")
for row in result_2:
    print(row)

cur.execute("SELECT * FROM products WHERE title LIKE '%no sugar%'")
result_3 = cur.fetchall()
print("\nProducts without sugar:")
for row in result_3:
    print(row)

cur.execute("SELECT * FROM products LIMIT 3")
result_4 = cur.fetchall()
print("\nThe first three products:")
for row in result_4:
    print(row)

cur.execute("SELECT * FROM products OFFSET 3 LIMIT 3")
result_5 = cur.fetchall()
print("\nThe second batch of three products:")
for row in result_5:
    print(row)


cur.close()
conn.close()
