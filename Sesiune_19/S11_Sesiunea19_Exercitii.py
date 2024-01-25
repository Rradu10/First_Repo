'''Write a SQL statement that groups all countries by continents, and counts them.
Write a SQL statement that groups all countries by continent, and computes the total population per continent (SUM).
'''

import sqlite3

# Connect to the SQLite database (replace 'your_database.db' with your actual database name)
conn = sqlite3.connect('Countries.db')
cursor = conn.cursor()

# SQL statement to group countries by continents and count them
count_query = """
    SELECT continent, COUNT(country_name) AS country_count
    FROM Countries
    GROUP BY continent;
"""

# Execute the count query
cursor.execute(count_query)

# Fetch and print the results
count_results = cursor.fetchall()
print("Country count by continent:")
for result in count_results:
    print(f"{result[0]}: {result[1]} Countries")

# SQL statement to group countries by continent and compute the total population per continent
population_query = """
    SELECT continent, SUM(population) AS total_population
    FROM countries
    GROUP BY continent;
"""

# Execute the population query
cursor.execute(population_query)

# Fetch and print the results
population_results = cursor.fetchall()
print("\nTotal population by continent:")
for result in population_results:
    print(f"{result[0]}: {result[1]} total population")

# Close the connection
conn.close()