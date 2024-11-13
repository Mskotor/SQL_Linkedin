import sqlite3

# << Connect to the database >>
connection = sqlite3.connect('WSDA_Music.db')

# << Create a cursor object >>
cursor = connection.cursor()

# << Basic Query >>
# result = connection.execute("""
# SELECT
#     FirstName,
#     LastName,
#     Email
# FROM
#     Customer
# """)

# << Column alias >>
# result = connection.execute("""
# SELECT
#     FirstName AS Name,
#     LastName AS Surname
#     Email
# FROM
#     Customer
# """)

# << Sorting >>
# Default = ASC, DESC (descending)
# result = connection.execute("""
# SELECT
#     FirstName AS Name,
#     LastName AS Surname,
#     Email
# FROM
#     Customer
# ORDER BY
#     Surname DESC
# """)

# << Limiting results >>
# result = connection.execute("""
# SELECT
#     FirstName AS Name,
#     LastName AS Surname,
#     Email
# FROM
#     CUstomer
# ORDER BY
#     Surname DESC,
#     Name
# LIMIT
#     10
# """)

# << Section 4 exercise >>
result = connection.execute(""""
SELECT
    name
FROM
    Track
WHERE
    type = 'table' AND name = 'Name'
""").fetchall()



# for row in result:
#     print(row)
