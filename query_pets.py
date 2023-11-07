import sqlite3

def main():
    # Connect to the database
    conn = sqlite3.connect('pets.db')
    cur = conn.cursor()

    while True:
        person_id = int(input("Enter a person's ID (or -1 to exit): "))

        if person_id == -1:
            break

        cur.execute('SELECT first_name, last_name, age FROM person WHERE id = ?', (person_id,))
        person_data = cur.fetchone()

        if person_data:
            print(f"{person_data[0]} {person_data[1]}, {person_data[2]} years old")
            cur.execute('SELECT pet.name, pet.breed, pet.age FROM pet JOIN person_pet ON pet.id = person_pet.pet_id WHERE person_pet.person_id = ?', (person_id,))
            pet_data = cur.fetchall()

            for pet in pet_data:
                print(f"owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old")
        else:
            print("Person not found.")

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()
