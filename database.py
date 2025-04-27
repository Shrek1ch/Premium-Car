import sqlite3

def get_car():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    sql = "SELECT * FROM car"

    cursor.execute(sql)

    car = cursor.fetchall()

    print(car)
    
    conn.close()

    return car

get_car()