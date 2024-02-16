import mysql.connector
import sys

# Extract command-line arguments
app_name = sys.argv[1]
deployment_count = int(sys.argv[2])  # Convert to int
deployment_status = sys.argv[3]

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="emp-demo.caome5fucnvy.ap-south-1.rds.amazonaws.com",
    user="root",
    password="NewPassword",
    database="devops"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define the INSERT query using placeholders
query = """
    INSERT INTO deployment_logs (app_name, deployment_count, deployment_status)
    VALUES (%s, %s, %s)
"""

try:
    # Execute the INSERT query with the provided variables
    cursor.execute(query, (app_name, deployment_count, deployment_status))
    
    # Commit the transaction
    connection.commit()
    print("Record inserted successfully!")
except mysql.connector.Error as error:
    # Rollback the transaction in case of an error
    connection.rollback()
    print(f"Failed to insert record: {error}")
finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
