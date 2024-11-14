import sqlite3
from idlelib.debugger_r import restart_subprocess_debugger

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
#     Customer
# ORDER BY
#     Surname DESC,
#     Name
# LIMIT
#     10
# """)

# << Section 4 exercise >>
# result = connection.execute(""""
# SELECT
#     name
# FROM
#     Track
# WHERE
#     type = 'table' AND name = 'Name'
# """).fetchall()

# << How many customers bought 2 songs @ 0.99 each >>
# result = connection.execute("""
# SELECT
#     CustomerId,
#     Total
# FROM
#     Invoice
# WHERE
#     Total = 1.98
# """)

# << How many invoices exist between 1.98 and 5.00 >>
# result = connection.execute("""
# SELECT
#     CustomerId,
#     InvoiceDate,
#     Total
# FROM
#     Invoice
# WHERE
#     Total >= 1.85 AND Total <= 5.00
# ORDER BY
#     InvoiceDate
# """)
# Or Total BETWEEN 1.98 AND 5.00

# << How many invoices are 1.98 or 3.96 >>
# result = connection.execute("""
# SELECT
#     CustomerId,
#     InvoiceDate,
#     Total
# FROM
#     Invoice
# WHERE
#     Total = 1.98 OR Total = 3.96
# ORDER BY
#     InvoiceDate
# """)
# Or Total IN (1.98, 3.96)

# << How many invoices were billed to Brussels?
# result = connection.execute("""
# SELECT
#     InvoiceDate,
#     BillingCity,
#     Total
# FROM
#     Invoice
# WHERE
#     BillingCity = 'Brussels'
# """)

# << How many invoices were billed in cities that start with B? >>
# result = connection.execute("""
# SELECT
#     InvoiceDate,
#     BillingCity,
#     Total
# FROM
#     Invoice
# WHERE
#     BillingCity LIKE 'B%'
# """)

# << How many invoices were billed on 2010-05-22
# result = connection.execute("""
# SELECT
#     InvoiceDate,
#     BillingCity,
#     Total
# FROM
#     Invoice
# WHERE
#     InvoiceDate = '2010-05-22 00:00:00'
# """)
# Or DATE(InvoiceDate) = '2010-05-22'

# # << All invoices that were billed after 2010-05-22 and have a total of less than 3.00 >>
# result = connection.execute("""
# SELECT
#     InvoiceDate,
#     BillingCity,
#     Total
# FROM
#     Invoice
# WHERE
#     DATE(InvoiceDate) > '2010-05-22' AND Total < 3.00
# """)

# << All invoices who's billing city starts with P or D >>
# result = connection.execute("""
# SELECT
#     InvoiceDate,
#     BillingCity,
#     Total
# FROM
#     Invoice
# WHERE
#     BillingCity LIKE 'P%' OR BillingCity LIKE 'D%'
# """)

# << All invoices that are greater than 1.98 from any cities whose name starts with P or D >>
result = connection.execute("""
SELECT
    InvoiceDate,
    BillingCity,
    Total
FROM
    Invoice
WHERE
    (BillingCity LIKE 'P%' OR BillingCity LIKE 'D%') AND (Total > 1.98)
""")


for row in result:
    print(row)
