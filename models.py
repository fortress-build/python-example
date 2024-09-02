from fortress_sdk_python import Fortress

##[TODO]Fill in the org_id and api_key
client = Fortress(
    org_id='your-org-id', 
    api_key='your-api-key')


#[TODO]Insert a tenantID here
conn = client.connect_tenant(tenant_id='your-tenant-id')

cursor = conn.cursor()


# Define the Task table using SQL
create_table_sql = """
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN DEFAULT FALSE
);
"""

# Create the table
cursor.execute(create_table_sql)
conn.commit()

# Function to insert a task
def insert_task(title):
    insert_sql = "INSERT INTO tasks (title) VALUES (%s) RETURNING id;"
    cursor.execute(insert_sql, (title,))
    task_id = cursor.fetchone()[0]
    conn.commit()
    return task_id

# Function to get all tasks
def get_all_tasks():
    select_sql = "SELECT id, title, done FROM tasks;"
    cursor.execute(select_sql)
    return cursor.fetchall()

# Example usage
if __name__ == "__main__":
    # Insert a task
    task_id = insert_task("Complete SQL example")
    print(f"Inserted task with ID: {task_id}")

    # Query all tasks
    all_tasks = get_all_tasks()
    print("All tasks:")
    for task in all_tasks:
        print(f"ID: {task[0]}, Title: {task[1]}, Done: {task[2]}")

# Don't forget to close the connection when you're done
