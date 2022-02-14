from db_connection import connect

genus = input("Podaj genus: ")

query = f"""SELECT * FROM species WHERE genus = '{genus}';"""

rows = connect(query)

try:
    for row in rows:
        print(row)
except:
    print('Query error')