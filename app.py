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
# result = connection.execute("""
# SELECT
#     InvoiceDate,
#     BillingCity,
#     Total
# FROM
#     Invoice
# WHERE
#     (BillingCity LIKE 'P%' OR BillingCity LIKE 'D%') AND (Total > 1.98)
# """)

# << Customers spending between 7 ad 15 >>
# result = connection.execute("""
# SELECT
#     InvoiceDate,
#     BillingCity,
#     Total,
#     CASE
#         WHEN Total < 2.00 THEN 'Baseline Purchase'
#         WHEN Total BETWEEN 2.00 AND 6.99 THEN 'Low Purchase'
#         WHEN Total BETWEEN 7.00 AND 15.00 THEN 'Target Purchase'
#         ELSE 'Top Performer'
#     END AS 'PurchaseType'
# FROM
#     Invoice
# WHERE
#     PurchaseType = 'Top Performer'
# """)
# CASE / END shows where IF / ELSE logic is located
# END AS shows name of the new column

# << Section 5 exercise >>
# result = connection.execute("""
# SELECT
#     Name,
#     Composer,
#     UnitPrice,
#     CASE
#         WHEN UnitPrice <= 0.99 THEN 'Budget'
#         WHEN UnitPrice BETWEEN 1.00 AND 1.49 THEN 'Regular'
#         WHEN UnitPrice BETWEEN 1.50 AND 1.99 THEN 'Premium'
#         ELSE 'Exclusive'
#     END AS PriceCategory
# FROM
#     Track
# ORDER BY
#     PriceCategory
# """)

# << Simple joins >>
# result = connection.execute("""
# SELECT *
# FROM
#     Invoice
# INNER JOIN
#     Customer ON Invoice.CustomerId = Customer.CustomerId
# ORDER BY
#     Customer.CustomerId
# """)

# << Inner Join >>
# Returns matching records that are present in both tables

# << Left Outer Join >>
# Returns all records form the left table, and matches them with the right table

# << Right Outer Join >>
# Returns all records from the right table, and matches them with the left table

# << Which employees are responsoble for top 10 sales >>
# result = connection.execute("""
# SELECT *
# FROM
#     Invoice
# INNER JOIN Customer ON Invoice.CustomerID = Customer.CustomerID
# INNER JOIN Employee ON Customer.SupportRepID = Employee.EmployeeID
# ORDER BY
#     Invoice.Total DESC
# LIMIT 10
# """)

# << Section 6 exercise >>
# Write a SQL query to generate a report that lists each customer along with their assigned support representative
# result = connection.execute("""
# SELECT
#     Customer.FirstName AS 'CustomerFirstName',
#     Customer.LastName AS 'CustomerLastName',
#     Employee.FirstName AS 'SupportRepFirstName',
#     Employee.LastName AS 'SupportRepLastName'
# FROM
#     Customer
# LEFT OUTER JOIN Employee ON Customer.SupportRepID = Employee.EmployeeID
# ORDER BY
#     SupportRepLastName,
#     SupportRepFirstName
# """)

# << Concatenating strings >>
# In SQL we concatenate table fields with pipe symbol ||
# result = connection.execute("""
# SELECT
#     FirstName,
#     LastName,
#     FirstName||' '||LastName||' '||Address||' '||City
# FROM
#     Customer
# WHERE
#     Country = 'USA'
# """)

# << Separating strings >>
# Spliting text is done with SUBSTR() function
# result = connection.execute("""
# SELECT
#     FirstName,
#     LastName,
#     PostalCode,
#     SUBSTRING(PostalCode, 1, 5) AS 'Postal Code'
# FROM
#     Customer
# WHERE
#     Country = 'USA'
# """)

# << UPPER AND LOWER >>

# << Date functions >>
# STRFTIME()
# result = connection.execute("""
# SELECT
#     FirstName,
#     LastName,
#     BirthDate,
#     STRFTIME('%Y-%m-%d', BirthDate) AS 'Birthdate no hour',
#     STRFTIME('%Y-%m-%d', 'now') - STRFTIME('%Y-%m-%d', BirthDate) AS 'Age'
# FROM
#     Employee
# """)

# << Aggregate functions >>
# result = connection.execute("""
# SELECT
#     SUM(Total) AS 'Total Sales',
#     AVG(Total) AS 'Average Sale',
#     MAX(Total) AS 'Max Sale',
#     MIN(Total) AS 'Min Sale',
#     COUNT(Total)
# FROM
#     Invoice
# """)

# << Nesting functions >>
# result = connection.execute("""
# SELECT
#     SUM(Total) AS 'Total Sales',
#     ROUND(AVG(Total), 2) AS 'Average Sale',
#     MAX(Total) AS 'Max Sale',
#     MIN(Total) AS 'Min Sale',
#     COUNT(Total)
# FROM
#     Invoice
# """)

for column in result.description:
    print(column[0], end=" | ")
print()

for row in result:
    print(row)
