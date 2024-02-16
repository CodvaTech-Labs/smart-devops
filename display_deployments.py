import mysql.connector
import sys

def get_deployment_counts(app_name):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
        host="emp-demo.caome5fucnvy.ap-south-1.rds.amazonaws.com",
        user="root",
        password="NewPassword",
        database="devops"
            )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query with placeholders for app_name
        query = """
            SELECT 
                COUNT(deployment_count) AS "total deployments",
                SUM(CASE WHEN deployment_status = 'PASS' THEN 1 ELSE 0 END) AS "passed deployments",
                SUM(CASE WHEN deployment_status = 'FAIL' THEN 1 ELSE 0 END) AS "failed deployments"
            FROM 
                deployment_logs
            WHERE 
                app_name = %s
        """

        # Execute the SQL query with the provided app_name
        cursor.execute(query, (app_name,))

        # Fetch the result
        result = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return result
    except mysql.connector.Error as error:
        print(f"Failed to fetch data: {error}")
        return None

# Example usage:
# Extract command-line arguments
app_name = sys.argv[1]
#app_name = 'Online-Library'
deployment_counts = get_deployment_counts(app_name)
if deployment_counts:
    print(f"Total Deployments: {deployment_counts[0]}")
    print(f"Passed Deployments: {deployment_counts[1]}")
    print(f"Failed Deployments: {deployment_counts[2]}")
