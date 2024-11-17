import sqlite3

conn = sqlite3.connect('../data/yellowpages.db')
cursor = conn.cursor()

# Create a table Yellow Pages
# business name, address, phone number, website, category, description
cursor.execute('''
    CREATE TABLE IF NOT EXISTS yellow_pages (
        id INTEGER PRIMARY KEY,
        business_name TEXT,
        address TEXT,
        phone_number TEXT,
        website TEXT,
        category TEXT,
        description TEXT
    )
''')

data_rows = [('Pets.com', 'San Francisco, California', '(505) 302-1234', 'pet.com', 'Pets',
              'Pets.com was an online pet food retailer'),
             ('Popeyes', 'Arabi, Louisiana, United States', '(503) 132-2334', 'Popeyes.com', 'Restaurants',
              'American multinational chain of fried chicken restaurants'),
             ('Samsung Group', 'Samsung Digital City, Yeongtong District, Suwon, South Korea', '(505) 453-3455',
              'Samsung.com', 'Consumer Electronics', 'Appliance and electronics corporations')]

# Insert a record
# cursor.executemany(
#     "INSERT INTO yellow_pages (business_name, address, phone_number, website, category, description) VALUES (?, ?, ?, ?, ?, ?)",
#     data_rows)
#
# # Commit the changes
# conn.commit()

# Retrieve data
cursor.execute('SELECT * FROM yellow_pages WHERE business_name like \'S%\'')
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()
