# Create a Database
create database my-db;
use my-db;

# Create A Table mobiles Inventory

CREATE TABLE mobiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    release_date DATE,
    specifications JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

# Insert data values into table.
INSERT INTO mobiles (brand, model, price, release_date, specifications) VALUES 
('Apple', 'iPhone 13', 799.99, '2021-09-24', '{"RAM": "4GB", "Storage": "128GB", "Camera": "12MP"}'),
('Samsung', 'Galaxy S21', 699.99, '2021-01-29', '{"RAM": "8GB", "Storage": "256GB", "Camera": "64MP"}'),
('Google', 'Pixel 6', 599.99, '2021-10-28', '{"RAM": "8GB", "Storage": "128GB", "Camera": "50MP"}');


