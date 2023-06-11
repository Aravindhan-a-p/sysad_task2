import mysql.connector as py
PATH = "./studentDetails.txt"
# Connect to the MySQL database
cnx = py.connect(
    host="localhost",
    database="postgres",
    user="root",
    password="root",
    port=5432
    )
cursor = cnx.cursor()
def initialising_tables():
 query = """
    CREATE TABLE IF NOT EXISTS studentdetails (
            rollno INTEGER PRIMARY KEY,
            name VARCHAR(50),
            hostel VARCHAR(15),
            room INTEGER,
            mess INTEGER,
            messpreference CHAR(3),
            dept VARCHAR(10),
            year INTEGER
    );
    """
    cursor.execute(query)
    cnx.commit()
    def dept(rollno):
    first4 = rollno[:4]
    if first4 == "1061": return "CSE"
    elif first4 == "1031": return "Civil"
    elif first4 == "1021": return "Chem"
    elif first4 == "1071": return "EEE"
    elif first4 == "1081": return "ECE"
    elif first4 == "1101": return "ICE"
    elif first4 == "1111": return "Mech"
    elif first4 == "1121": return "MME"
    elif first4 == "1141": return "Arch"
    elif first4 == "1011": return "Prod"
    else: return "NA"

def insert_data():
    with open(PATH) as f:
        # Skipping the first line as it contains the column names
        _ = f.readline()

        for line in f:
            l = line.split()
            cursor.execute(
                "INSERT INTO studentdetails VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING",
                (l[1], l[0], l[2], l[3], l[4], l[5], dept(l[1]), '2022')
            )
            cnx.commit()
        
def view_data():
    cursor.execute("SELECT * FROM studentdetails")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    

def main():
    initialising_tables()
    insert_data()
    view_data()

main()
