import sqlite3 
connect = sqlite3.connect('./DB_Sqlite/patients.db')
db = connect.cursor() ##stores information from above function

db.execute("DROP TABLE IF EXISTS patient_table") #sends a query that looks into
#the database called patients.db to see if there is a table called patients_table
# and if it exists, it will delete it
connect.commit() #we need to commit the function in order for it to work

#CREATE A NEW TABLE
table = """CREATE TABLE patient_table (mrn VARCHAR(255) NOT NULL, 
firstname CHAR(25) NOT NULL,
lastname CHAR(25) NOT NULL,
pronouns CHAR(25) NOT NULL,
dob CHAR(25) NOT NULL,
provider CHAR(25) NOT NULL,
insurance CHAR(25) NOT NULL,
last_visit CHAR(25) NOT NULL 
);
""" #Creates a table called 'patient_table', the semicolon tells SQL that 
#we're done with that one statement. #VARCHAR and CHAR are strings 

db.execute(table)
connect.commit()

#Now we're going to insert dummy data within our patient table 
#db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('12345', 'John', 'Smith', '01/01/2000')")
#in parenthesis after patient_table we provide the columns in which we want to insert information, 
# and in values we insert what we want to insert
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, pronouns, dob, provider, insurance, last_visit) values('23456', 'Diana', 'Mendez', 'she/her', '02/02/2001', 'Dr.Arias', 'HealthFirst', '01/28/2022')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, pronouns, dob, provider, insurance, last_visit) values('34567', 'Mary', 'Smith', 'she/her', '03/03/2002', 'Dr.Duck', 'UnitedHealth', '05/15/2022')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, pronouns, dob, provider, insurance, last_visit) values('45678', 'Michael', 'Smith', 'he/him', '04/04/2003', 'Dr.German', '1199', '10/11/2022')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, pronouns, dob, provider, insurance, last_visit) values('56789', 'Brittany', 'Kusi', 'she/her', '05/05/2004', 'Dr. Hants', 'HealthFirst', '07/26/2022')")


connect.commit()

#Close the connection
connect.close()