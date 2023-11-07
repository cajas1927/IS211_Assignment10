import sqlite3

def main():
    # Connect to the database
    conn = sqlite3.connect('pets.db')
    cur = conn.cursor()

    # Define the data to be loaded
    data_to_insert = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23),
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'AlaskanMalamute', 3, 0),
        (3, 'Max', 'CockerSpaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'CockerSpaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1),
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6)
    ]

    # Insert data into the tables
    for item in data_to_insert:
        if len(item) == 2:
            cur.execute('INSERT INTO person_pet VALUES (?, ?)', (item[0], item[1]))
        else:
            cur.execute('INSERT INTO person VALUES (?, ?, ?, ?)', (item[0], item[1], item[2], item[3]))
            cur.execute('INSERT INTO pet VALUES (?, ?, ?, ?, ?)', (item[0], item[4], item[5], item[6], item[7]))

    conn.commit()

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()
