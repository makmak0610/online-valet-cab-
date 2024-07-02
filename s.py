import tkinter as tk
from tkinter import ttk
import pymysql

# Establish a connection to the MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='saloni',
    database='userdata'
)

cursor = conn.cursor()

# Function to fetch data from the database and populate the Treeview
def load_data():
    # Clear existing data in the Treeview
    tree.delete(*tree.get_children())

    # Fetch data from the table
    cursor.execute("SELECT * FROM bd1")
    rows = cursor.fetchall()

    # Populate the Treeview
    for row in rows:
        tree.insert('', 'end', values=row)

# Function to filter data in the Treeview based on search query
def search_data():
    query = search_entry.get().lower()
    if query:
        for item_id in tree.get_children():
            values = tree.item(item_id, 'values')
            if any(query in str(value).lower() for value in values):
                tree.selection_add(item_id)
            else:
                tree.selection_remove(item_id)
    else:
        tree.selection_remove(*tree.get_children())

# Function to go back
def w1():
    root.destroy()
    import adminwel

# Create the main window
root = tk.Tk()
root.title('PyMySQL Database Table Viewer')

# Create a search bar
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

back_button = tk.Button(search_frame, text='Back', command=w1)
back_button.pack(side='left', anchor='nw')

search_label = tk.Label(search_frame, text='Search:')
search_label.pack(side='left')

search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side='left')

search_button = tk.Button(search_frame, text='Search', command=search_data)
search_button.pack(side='left')

# Create a Treeview widget with a scrollbar
tree = ttk.Treeview(root, columns=('ID', 'Username', 'Date', 'Pickup', 'Drop_loc', 'Drop_loc1', 'Distance', 'Bill'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Username', text='Username')
tree.heading('Date', text='Date')
tree.heading('Pickup', text='Pickup')
tree.heading('Drop_loc', text='Drop_loc')
tree.heading('Drop_loc1', text='Drop_loc1')
tree.heading('Distance', text='Distance')
tree.heading('Bill', text='Bill')

tree.column('ID', width=50)
tree.column('Username', width=200)
tree.column('Date', width=220)
tree.column('Pickup', width=100)
tree.column('Drop_loc', width=100)
tree.column('Drop_loc1', width=100)
tree.column('Distance', width=200)
tree.column('Bill', width=100)

# Create a vertical scrollbar and associate it with the Treeview
vsb = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
tree.configure(yscrollcommand=vsb.set)

# Pack the Treeview and scrollbar
tree.pack(side='left', fill='both', expand=True)
vsb.pack(side='right', fill='y')

# Load data into the Treeview
load_data()

# Button to refresh data
refresh_button = tk.Button(root, text='Refresh Data', command=load_data)
refresh_button.pack()

# Run the main loop
root.mainloop()

# Close the cursor and database connection
cursor.close()
conn.close()
