-- Insert 16 sample users (8 customers, 8 admins)
INSERT INTO USER (User_Name, Phone_Number, Email_Address, Password) VALUES
('Alice Johnson', '408-555-1234', 'alice@example.com', 'password1'),
('Bob Smith', '408-555-5678', 'bob@example.com', 'password2'),
('Charlie Brown', '408-555-9012', 'charlie@example.com', 'password3'),
('Diana Ross', '408-555-3456', 'diana@example.com', 'password4'),
('Ethan Hunt', '408-555-7890', 'ethan@example.com', 'password5'),
('Fiona Green', '408-555-2345', 'fiona@example.com', 'password6'),
('George White', '408-555-6789', 'george@example.com', 'password7'),
('Hannah Lee', '408-555-0123', 'hannah@example.com', 'password8'),
('Ivy Clark', '408-555-4567', 'ivy@example.com', 'password9'),
('Jack Black', '408-555-8901', 'jack@example.com', 'password10'),
('Karen Blue', '408-555-2345', 'karen@example.com', 'password11'),
('Leo King', '408-555-6780', 'leo@example.com', 'password12'),
('Mona Lisa', '408-555-1122', 'mona@example.com', 'password13'),
('Nina Brown', '408-555-3344', 'nina@example.com', 'password14'),
('Oscar Wilde', '408-555-5566', 'oscar@example.com', 'password15'),
('Paul Green', '408-555-7788', 'paul@example.com', 'password16');

-- Insert 8 customers with detailed home addresses in San Jose
INSERT INTO CUSTOMER (User_ID, Bank_Account, Home_Address) VALUES
(1, 'BA12345', '1234 Market St, San Jose, CA 95112'),
(2, 'BA23456', '5678 Santa Clara St, San Jose, CA 95113'),
(3, 'BA34567', '9101 Winchester Blvd, San Jose, CA 95128'),
(4, 'BA45678', '2468 Blossom Hill Rd, San Jose, CA 95123'),
(5, 'BA56789', '1357 Willow St, San Jose, CA 95125'),
(6, 'BA67890', '8642 Senter Rd, San Jose, CA 95111'),
(7, 'BA78901', '3141 Story Rd, San Jose, CA 95127'),
(8, 'BA89012', '7890 The Alameda, San Jose, CA 95126');

-- Insert 8 admins
INSERT INTO ADMIN (User_ID) VALUES
(9), (10), (11), (12), (13), (14), (15), (16);

INSERT INTO PRODUCTS (ProName, Brand, Cost, Price, ProDescription, Category, Image, Quantity_Available, Quantity_Sold, Popular_Items)
VALUES 
('Disneyland StellaLou Lovely Plush Charm Keychain', 'Disney', 15.00, 35.00, 
'Featuring StellaLou in her signature pastel colors and delicate details, this 2024 plush charm is made of soft, huggable material with embroidered features. Perfect for bags, backpacks, or as a collectible, this lovely keychain adds a touch of Disney magic to your everyday adventures!', 
'GENERAL_MERCHANDISE', 'https://storage.googleapis.com/eshop_product_images/Stella_Lou_KeyChain.jpg', 50, 30, TRUE),

('Universal Sticky Notes', 'Kawaii Paper Art', 0.99, 5.99, 
'Take notes over a full moon! This Universe Sticky Note set comes in 6 different colors. Easily write over with pens, pencils, or markers due to its paper material. It makes for a great gift for galaxy lovers or bookworms. List out to-do lists or reminders on a unique moon.', 
'GENERAL_MERCHANDISE', 'https://storage.googleapis.com/eshop_product_images/Universal_Sticky_Notes.jpg', 50, 20, FALSE),

('Northeastern Logo Tote Bag', 'Northeastern', 2.99, 19.99, 
'NEU Logo Tote Bag: 16"H x 14"W x 0"D. Perfect for hauling textbooks, snacks, and all your hopes and dreams of surviving finals—because who needs sleep when you have style?', 
'GENERAL_MERCHANDISE', 'https://storage.googleapis.com/eshop_product_images/NEU_Tote_Bag.jpg', 30, 45, TRUE),

('3D Squishy Sakura Decompression Notebook', 'Tokyo Supplies', 3.50, 12.50, 
'Our super kawaii 3D squishy fun character notebook featuring an array of adorable animal characters, including a unicorn, duck, pig, and rabbit.', 
'GENERAL_MERCHANDISE', 'https://storage.googleapis.com/eshop_product_images/3D_Notebook.jpg', 25, 5, FALSE),

('Stanley Quencher H2.0 FlowState Stainless Steel Vacuum', 'Stanley', 20.00, 45.00, 
'Stanley Quencher H2.0 FlowState Stainless Steel Vacuum Insulated Tumbler with Lid and Straw for Water, Iced Tea or Coffee, Smoothie and More, Rose Quartz 2.0, 40 OZ / 1.18 L', 
'GENERAL_MERCHANDISE', 'https://storage.googleapis.com/eshop_product_images/Stanley_Steel_Vacuum.jpg', 18, 2, FALSE),

('Logitech MX Master 3S Wireless Mouse', 'Logitech', 40.00, 99.99, 
'Wireless Performance Mouse, Ergo, 8K DPI, Track on Glass, Quiet Clicks, USB-C, Bluetooth, Windows, Linux, Chrome - Graphite', 
'GENERAL_MERCHANDISE', 'https://storage.googleapis.com/eshop_product_images/Logitech_Wireless_Mouse.jpg', 15, 5, FALSE),
('Northeastern Hoodie', 'Northeastern', 25.00, 55.00, 
'Survive midterms, nail project presentations, ace interviews, and land that dream job – all while staying comfy in this trusty Northeastern hoodie, your ultimate partner in academic crime!', 
'GENERAL_MERCHANDISE', 'https://storage.googleapis.com/eshop_product_images/Northeastern_Hoodie.jpg', 100, 50, TRUE),
('Kanken Backpack', 'Fjallraven Kanken', 40.00, 90.00, 
'Signature logo patch, Length: 10.25in / 26cm, Height: 14.5in / 37cm, Depth: 4.25in / 11cm', 
'GENERAL_MERCHANDISE', 'https://storage.googleapis.com/eshop_product_images/Kanken_Backpack.jpg', 8, 2, FALSE),
('Fresh Cut Fruit Cup - 12 Oz', 'NEU Deli', 1.00, 4.99, 
'Enjoy a refreshing and healthy snack with our Fresh Cut Fruit Cup – a delightful mix of juicy, ripe fruits, perfectly portioned for on-the-go freshness and a burst of natural sweetness!', 
'FOOD_BEVERAGE', 'https://storage.googleapis.com/eshop_product_images/Fruit_Cup.jpg', 3, 7, FALSE),
('Lays Potato Chips Spicy Crayfish Flavor (3 Bags)', 'Lay''s', 6.00, 12.99, 
'Enjoy the bold and unique taste of Lays Potato Chips in Spicy Crayfish Flavor, available in a convenient pack of 3 bags for a satisfying snack anytime.', 
'FOOD_BEVERAGE', 'https://storage.googleapis.com/eshop_product_images/Lays_Potato_Chips.jpg', 45, 80, TRUE),
('La Fermière Jasmine', 'La Fermière', 1.29, 3.99, 
'La Fermière Jasmine Yogurt 4.9OZ: Because sometimes your taste buds deserve a spa day with a hint of floral bliss.', 
'FOOD_BEVERAGE', 'https://storage.googleapis.com/eshop_product_images/LaFermiere_Yogurt.jpg', 20, 5, FALSE),
('San Francisco Assorted Chocolates', 'See Candies', 8.00, 20.00, 
'Featuring illustrated images of beautiful San Francisco, this assortment is brimming with customer favorites. From Milk Almond Caramel to Dark Marzipan, you’ll adore these nutty, chewy and soft center classics. Approximately 26 pieces.', 
'FOOD_BEVERAGE', 'https://storage.googleapis.com/eshop_product_images/SF_Chocolates.jpg', 7, 3, FALSE),
('Arrowhead Mountain Spring Bottle Water', 'Arrowhead', 0.30, 0.99, 
'16.9 Oz. 100% mountain spring water: zero calories, no sweeteners and no artificial colors or flavors.', 
'FOOD_BEVERAGE', 'https://storage.googleapis.com/eshop_product_images/Arrowhead_Bottle_Water.jpg', 31, 69, TRUE),
('Hee Creek Black Sesame Snack', 'Hee Creek', 9.00, 24.50, 
'Nutritious Hee Creek Black Sesame Balls 12.7 oz (40 pieces)– a delicious way to support hair health and vitality.', 
'FOOD_BEVERAGE', 'https://storage.googleapis.com/eshop_product_images/Hee_Creek_Black_Sesame_Balls.jpg', 9, 1, FALSE),
('Japanese Kit Kat Multi-Flavor Packet', 'KitKat', 9.99, 21.99, 
'This assortment features 20 KitKats with 10 different flavors, including 2 KitKats for each unique flavor, ensuring a delightful variety in every box', 
'FOOD_BEVERAGE', 'https://storage.googleapis.com/eshop_product_images/Japanese_KitKat.jpg', 17, 23, FALSE);


INSERT INTO GENERAL_MERCHANDISE (Product_ID, Color) VALUES
(1, 'Purple'),
(2, 'Multi-Color'),
(3, 'Black'),
(4, 'Yellow'),
(5, 'Rose'),
(6, 'Black'),
(7, 'Black'),
(8, 'Blue');



INSERT INTO FOOD_BEVERAGE (Product_ID, Sell_By) VALUES
(9, '2024-10-27'),
(10, '2025-12-31'),
(11, '2024-11-25'),
(12, '2025-06-30'),
(13, '2026-12-31'),
(14, '2025-12-31'),
(15, '2025-12-31');

#ORDER / ORDER ITEMS / RATING
-- Insert sample data into ORDERS table
INSERT INTO ORDERS (User_ID, Order_Status, Order_Date, Total_Price) VALUES
(1, 'completed', '2024-11-17', 40.99),    -- Order 1 for User 1
(1, 'completed', '2024-11-17', 189.99),    -- Order 2 for User 1
(2, 'completed', '2024-11-17', 38.49),    -- Order 3
(3, 'completed', '2024-11-17', 4.99),    -- Order 4
(4, 'completed', '2024-11-17', 154.95),    -- Order 5
(5, 'completed', '2024-11-17', 24.50),    -- Order 6
(6, 'completed', '2024-11-17', 2.97),    -- Order 7
(7, 'completed', '2024-11-17', 3.69);    -- Order 8

-- Insert sample data into ORDER_ITEM table
INSERT INTO ORDER_ITEM (Order_ID, Product_ID, Quantity) VALUES
-- Order 1
(1, 1, 1),     -- Disneyland StellaLou Keychain, 1 quantity
(1, 2, 1),     -- Universal Sticky Notes, 1 quantity
-- Order 2
(2, 3, 2),     -- Stanley Quencher Tumbler, 2 quantities
(2, 4, 1),     -- Logitech MX Master 3S Mouse, 1 quantity
-- Order 3
(3, 5, 1),     -- Japanese Kit Kat Multi-Flavor Packet, 1 quantity
(3, 7, 1),     -- 3D Squishy Sakura Notebook, 1 quantity
-- Order 4
(4, 8, 1),     -- Fresh Cut Fruit Cup, 1 quantity
-- Order 5
(5, 6, 1),     -- Northeastern Hoodie, 1 quantity
(5, 12, 5),    -- NEU Logo Tote Bag, 5 quantities
-- Order 6
(6, 15, 1),    -- Hee Creek Black Sesame Snack, 1 quantity
-- Order 7
(7, 14, 3);    -- Arrowhead Mountain Spring Bottle Water, 3 quantities

-- Insert sample data into RATING table
INSERT INTO RATING (Comments, Product_ID, User_ID, Rate_Score) VALUES
('Amazing quality and cute design!', 1, 1, 5),
('Useful for all my notes, I love it!', 2, 2, 4),
('Keeps my drinks cold for hours!', 3, 3, 5),
('Very ergonomic, worth the price.', 4, 4, 4),
('Great assortment, loved every flavor!', 5, 5, 5),
('Stylish and comfy hoodie, perfect for college.', 6, 1, 5),
('Super adorable and squishy, perfect for journaling.', 7, 2, 4),
('Fresh and sweet, a great snack.', 8, 6, 3),
('Awesome for travel and everyday use.', 12, 5, 4),
('Nutritious and delicious, great snack!', 15, 4, 5);


#PAYMENT / DELIVERY
-- Insert data into the PAYMENT table
-- Insert data into the PAYMENT table
INSERT INTO PAYMENT (User_ID, Order_ID, Order_Date, Total_Amount)
VALUES 
    (1, 1, '2024-11-17', 40.99),
    (1, 2, '2024-11-17', 189.99),
    (2, 3, '2024-11-17', 38.49),
    (3, 4, '2024-11-17', 4.99),
    (4, 5, '2024-11-17', 154.95),
    (5, 6, '2024-11-17', 24.50),
    (6, 7, '2024-11-17', 2.97),
    (7, 8, '2024-11-17', 3.69);

-- Insert data into the DELIVERY table
INSERT INTO DELIVERY (User_ID, Order_ID, Delivery_Method, Delivery_Address)
VALUES 
    (1, 1, 'Standard', '123 Main St, Cityville, Country'),
    (2, 2, 'Express', '456 Oak St, Townsville, Country'),
    (3, 3, 'Standard', '789 Pine St, Villagetown, Country'),
    (4, 4, 'Standard', '101 Maple St, Hamlet City, Country'),
    (5, 5, 'Express', '202 Birch St, Metropolis, Country'),
    (6, 6, 'Standard', '3035 Homestead St, Santa Clara, Country'),
    (7, 7, 'Express', '366 Bird St, San Jose, Country');