-- Creating USER Table
CREATE TABLE USER (
    User_ID INT AUTO_INCREMENT PRIMARY KEY, -- Auto-increment for User ID
    User_Name VARCHAR(100) NOT NULL,
    Phone_Number VARCHAR(15),
    Email_Address VARCHAR(100),
    Password VARCHAR(50) NOT NULL
);

-- Creating CUSTOMER Table
CREATE TABLE CUSTOMER (
    User_ID INT,
    Bank_Account VARCHAR(50),
    Home_Address VARCHAR(255),
    PRIMARY KEY (User_ID),
    FOREIGN KEY (User_ID) REFERENCES USER(User_ID) ON DELETE CASCADE
);

-- Creating ADMIN Table
CREATE TABLE ADMIN (
    User_ID INT,
    PRIMARY KEY (User_ID),
    FOREIGN KEY (User_ID) REFERENCES USER(User_ID) ON DELETE CASCADE
);

-- Create the Products table 
CREATE TABLE PRODUCTS (
    Product_ID INT AUTO_INCREMENT PRIMARY KEY,  -- Auto-increment for Product ID
    ProName VARCHAR(200),
    Brand VARCHAR(200),
    Cost DECIMAL(10,2),
    Price DECIMAL(10,2),
    ProDescription TEXT,
    Category VARCHAR(50),
    Image VARCHAR(500),
    Quantity_Available INT,
    Quantity_Sold INT,
    Popular_Items BOOLEAN DEFAULT FALSE         -- Default to not popular item
);

-- Create the General Merchandise table with product ID and color attributes
CREATE TABLE GENERAL_MERCHANDISE (
    Product_ID INT PRIMARY KEY,
    Color VARCHAR(20),
    FOREIGN KEY (Product_ID) REFERENCES PRODUCTS(Product_ID) ON DELETE CASCADE
);

-- Create the Food and Beverage table with product ID and sell by date.
CREATE TABLE FOOD_BEVERAGE (
    Product_ID INT PRIMARY KEY,
    Sell_By DATE,
    FOREIGN KEY (Product_ID) REFERENCES PRODUCTS(Product_ID) ON DELETE CASCADE
);

-- Create the Orders table
CREATE TABLE ORDERS (
    Order_ID INT AUTO_INCREMENT PRIMARY KEY,   -- Auto-increment for Order ID
    User_ID INT,
    Order_Status ENUM('in_progress', 'completed') DEFAULT 'in_progress',    
    Order_Date DATETIME DEFAULT NULL,
    Total_Price DECIMAL(10, 2) DEFAULT NULL,                    
    FOREIGN KEY (User_ID) REFERENCES USER(User_ID)
);

-- Create the Order Item table
CREATE TABLE ORDER_ITEM (
    Order_Item_ID INT AUTO_INCREMENT PRIMARY KEY,      
    Order_ID INT,
    Product_ID INT,
    Quantity INT NOT NULL,
    FOREIGN KEY (Order_ID) REFERENCES ORDERS(Order_ID) ON DELETE CASCADE,
    FOREIGN KEY (Product_ID) REFERENCES PRODUCTS(Product_ID)
);

-- Create the Payment table
CREATE TABLE PAYMENT (
    Payment_ID INT AUTO_INCREMENT PRIMARY KEY, -- Auto-increment for Payment ID
    User_ID INT,                               -- Foreign key linking to the user who made the payment
    Order_ID INT,                              -- Foreign key linking to the related order
    Order_Date DATETIME DEFAULT NULL,          -- The date the payment was made
    Total_Amount DECIMAL(10,2),                -- The total amount paid for the order
    FOREIGN KEY (User_ID) REFERENCES USER(User_ID),
    FOREIGN KEY (Order_ID) REFERENCES ORDERS(Order_ID)
);


-- Create the Delivery table
CREATE TABLE DELIVERY (
    Delivery_ID INT AUTO_INCREMENT PRIMARY KEY, -- Auto-increment for Delivery ID
    User_ID INT,
    Order_ID INT,
    Delivery_Method VARCHAR(50),
    Delivery_Address TEXT,
    FOREIGN KEY (User_ID) REFERENCES USER(User_ID),
    FOREIGN KEY (Order_ID) REFERENCES ORDERS(Order_ID)
);

-- Create the Rating table
CREATE TABLE RATING (
    Rate_ID INT AUTO_INCREMENT PRIMARY KEY,    -- Auto-increment for Rating ID
    Comments TEXT,
    Product_ID INT,
    User_ID INT,
    Rate_Score INT,
    FOREIGN KEY (Product_ID) REFERENCES PRODUCTS(Product_ID),
    FOREIGN KEY (User_ID) REFERENCES USER(User_ID)
);
