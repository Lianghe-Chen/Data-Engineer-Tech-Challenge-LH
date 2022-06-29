CREATE TABLE Cars (
    SalesID int,
    Manufacturer varchar(255),
    ModelName varchar(255),
    SerialNumber varchar(255),
    Weight varchar(255),
    Price varchar(255),
    CustomerName varchar(255),
    CustomerPhone varchar(255),
    Salesperson varchar(255),
    Characteristics varchar(255)
);

SELECT * FROM Cars;

SELECT customername, price FROM Cars;

SELECT manufacturer, COUNT(manufacturer) FROM Cars
GROUP BY manufacturer
ORDER by COUNT(manufacturer) desc
LIMIT 3