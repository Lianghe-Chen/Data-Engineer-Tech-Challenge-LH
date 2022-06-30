## Section 2: Databases

For this section, I set up a PostgreSQL database using the base `docker` image [here](https://hub.docker.com/_/postgres). I created a `Dockerfile` which will stand up my database with the DDL statements needed to create the necessary tables. This was derived from the SQL file: `world.sql` which is the PostgreSQL part of the MySQL “World” database. For this car dealership, each table contains the following fields, characteristics and information:

- SalesID --> Unique identifier for each sale transaction.
- Manufacturer --> Car manufacturer.
- ModelName --> Name of car model.
- SerialNumber --> Serial number for each sale transaction.
- Weight --> Weight of car.
- Price --> Price of car.
- CustomerName --> Name of customer.
- CustomerPhone --> Phone number of customer.
- Salesperson --> Name of salesperson.
- Characteristics --> Characteristics of car sold.

I wrote SQL statements to query information from the database for each of the following tasks:

1. I want to know the list of our customers and their spending.
2. I want to find out the top 3 car manufacturers that customers bought by sales (quantity) and the sales number for it in the current month.

The SQL statements and queries are saved in the SQL file: `Cars_Script.sql`.
