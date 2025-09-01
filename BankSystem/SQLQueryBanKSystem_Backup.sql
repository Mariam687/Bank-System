CREATE TABLE Branch (
    Branch_id INT PRIMARY KEY,
    contact_num NVARCHAR(20),
    [Name] NVARCHAR(20) NOT NULL,
    [Address] NVARCHAR(50) NOT NULL,
    Employee_id INT
    
);

INSERT INTO Branch(Branch_id, Contact_num, [Name], [Address], employee_id)
VALUES
(1, '010-1234-5678', 'Bank Masr Tanta', 'tanta', 5), 
(2, '010-2345-6789', 'Bank Masr Giza', 'Giza', 2),   
(3, '010-3456-7890', 'Bank Masr Santa', 'santa', 13),
(4, '010-4567-8901', 'Bank Masr Cairo', 'Cairo', 4), 
(5, '010-5678-9012', 'Bank Masr Tanta', 'tanta', 15),
(6, '010-6789-0123', 'Bank Masr Giza', 'Giza', 6),   
(7, '010-7890-1234', 'Bank Masr Aswan', 'Aswan', 7), 
(8, '010-8901-2345', 'Bank Masr Tanta', 'tanta', 8), 
(9, '010-9012-3456', 'Bank Masr Cairo', 'Cairo', 19),
(10, '010-0123-4567', 'Bank Masr Cairo', 'Cairo', 10),
(11, '010-1234-5678', 'Bank Masr NasrCity', 'NasrCity', 11),
(12, '010-2345-6789', 'Bank Masr Cairo', 'Cairo', 2),
(13, '010-3456-7890', 'Bank Masr NasrCity', 'NasrCity', 3), 
(14, '010-4567-8901', 'Bank Masr NasrCity', 'NasrCity', 14),
(15, '010-5678-9012', 'Bank Masr Giza', 'Giza', 5),   
(16, '010-6789-0123', 'Bank Masr Giza', 'Giza', 6),   
(17, '010-7890-1234', 'Bank Masr Luxor', 'luxor', 17),
(18, '010-8901-2345', 'Bank Masr Luxor', 'luxor', 1), 
(19, '010-9012-3456', 'Bank Masr Luxor', 'luxor', 9), 
(20, '010-0123-4567', 'Bank Masr Dmnhor', 'Dmnhor', 21), 
(21, '010-1234-5678', 'Bank Masr Cairo', 'Cairo', 10),
(22, '010-2345-6789', 'Bank Masr Tanta', 'tanta', 15),
(23, '010-3456-7890', 'Bank Masr Giza', 'Giza', 6),   
(24, '010-4567-8901', 'Bank Masr Aswan', 'Aswan', 7), 
(25, '010-5678-9012', 'Bank Masr NasrCity', 'NasrCity', 14); 


CREATE TABLE Employee (
    Employee_id INT PRIMARY KEY,
    First_name NVARCHAR(20) NOT NULL,
    Last_name NVARCHAR(20) NOT NULL,
    Email NVARCHAR(50),
    [Password] NVARCHAR(50),
    Date_hired DATE,
    Salary DECIMAL(15,2),
    [Role] NVARCHAR(50),
    Permission SMALLINT,
    Branch_id INT,
   
);


-- Add the new column
ALTER TABLE employee ADD username VARCHAR(20);

-- Update the username column with values
UPDATE employee
SET username = LOWER(SUBSTRING(first_name, 1, 1) + last_name);


INSERT INTO employee (Employee_id, first_name, last_name, email, [password], Date_hired, salary, [Role], permission, Branch_id, username)
VALUES
(1, 'Ross', 'Hubble', 'rhubble0@weibo.com', 'qK5*1\\i%@s$9', '2024-06-23', 5000, 'Chairman', 5, 18, 'rhubble'),
(2, 'Theodore', 'Fayers', 'tfayers1@huffingtonpost.com', 'lE7.7ADFK4Sw?n(', '2024-12-01', 5500, 'CEO', 2, 2, 'tfayers'),
(3, 'Danit', 'Bardell', 'dbardell2@bbc.co.uk', 'qA6>GIOe8', '2024-10-16', 6000, 'CFO', 3, 13, 'dbardell'),
(4, 'Idalia', 'Mulvey', 'imulvey3@parallels.com', 'tO0=t\\F%Ia@QB', '2024-05-31', 6500, 'COO', 4, 4, 'imulvey'),
(5, 'Marlane', 'Heeran', 'mheeran4@uol.com.br', 'tW5,$vrk=vFVn*}', '2024-10-10', 7000, 'BranchManager', 5, 1, 'mheeran'),
(6, 'Ardelle', 'Greenacre', 'agreenacre5@msu.edu', 'pC1"$&Ez*Ckm~Zs', '2024-02-20', 7500, 'Sales Associate', 6, 6, 'agreenacre'),
(7, 'Bamby', 'Santora', 'bsantora6@usnews.com', 'bO2#vv<VFDxwTEZ', '2024-08-28', 8000, 'VP Accounting', 7, 7, 'bsantora'),
(8, 'Donnell', 'Jozefiak', 'djozefiak7@example.com', 'qQ1!7y$UL9NuR=', '2024-04-08', 8500, 'Executive Secretary', 8, 8, 'djozefiak'),
(9, 'Veradis', 'Eberle', 'veberle8@macromedia.com', 'kI8"*rsE', '2024-09-25', 9000, 'Teller', 9, 19, 'veberle'),
(10, 'Giacobo', 'O\\Doherty', 'godoherty9@icio.us', 'hD0/H3TI")j`.5', '2023-12-25', 9500, 'Teller', 10, 10, 'godoherty'),
(11, 'Belita', 'Tipper', 'btippera@nbcnews.com', 'mB2&V|Zu5GJ{!$T', '2024-02-22', 10000, 'Teller', 11, 11, 'btipper'),
(13, 'Fulton', 'Dallimare', 'fdallimarec@sina.com.cn', 'uY4"L`Kv', '2024-03-17', 10500, 'AccountOfficer', 13, 3, 'fdallimare'),
(14, 'Margalit', 'Sewall', 'msewalld@ycombinator.com', 'wS2(OxbYQ52Wy', '2024-04-21', 11000, 'AccountOfficer', 14, 14, 'msewall'),
(15, 'Aland', 'Fenby', 'afenbye@cnbc.com', 'zX6$,J{f8(?LJh', '2024-01-22', 11500, 'AccountOfficer', 15, 5, 'afenby'),
(16, 'Lyn', 'Prudham', 'lprudhamf@webeden.co.uk', 'iV3~(ERD1otK', '2024-10-28', 12000, 'AccountOfficer', 16, 6, 'lprudham'),
(17, 'Jo', 'Methven', 'jmethveng@hexun.com', 'sJ2!OtGimgFix\\e', '2024-04-08', 12500, 'AccountOfficer', 17, 17, 'jmethven'),
(18, 'Lula', 'Chasteney', 'lchasteneyh@nytimes.com', 'hR4"R=881oS~IB', '2024-10-24', 13000, 'AccountOfficer', 28, 18, 'lchasteney'),
(19, 'Tirrell', 'Tagg', 'ttaggi@xinhuanet.com', 'pT8!#.7?.>b1w(E', '2024-04-22', 13500, 'AccountOfficer', 19, 1, 'ttagg'),
(21, 'Kristoffer', 'Exeter', 'kexeterj@ezinearticles.com', 'xK1,{tB{_<', '2024-07-18', 14000, 'AccountOfficer', 20, 2, 'kexeter'),
(22, 'Kristoffer', 'Exeter', 'kexeterj@ezinearticles.com', 'xK1,{tB{_<', '2024-07-18', 14500, 'AccountOfficer', 2, 20, 'kexeter'),
(23, 'Kristoffer', 'Exeter', 'kexeterj@ezinearticles.com', 'xK1,{tB{_<', '2024-07-18', 15000, 'AccountOfficer', 21, 17, 'kexeter'),
(24, 'Danit', 'Bardell', 'dbardell2@bbc.co.uk', 'qA6>GIOe8', '2024-10-16', 15500, 'CFO', 3, 6, 'dbardell'),
(25, 'Fulton', 'Dallimare', 'fdallimarec@sina.com.cn', 'uY4"LKv', '2024-03-17', 16000, 'AccountOfficer', 17, 5, 'fdallimare');



alter table Branch
add constraint c2 FOREIGN KEY (Employee_id) REFERENCES employee(Employee_id) on delete set null on update cascade

alter table employee
add constraint c1 FOREIGN KEY (Branch_id) REFERENCES Branch(Branch_id)


CREATE TABLE Customer (
    Customer_id INT PRIMARY KEY,
    [Address] NVARCHAR(50),
    Email NVARCHAR(50),
    Date_joined DATE,
    Phone_num NVARCHAR(20),
    First_name NVARCHAR(20) NOT NULL,
    Last_name NVARCHAR(20) NOT NULL,
    Identification_number NVARCHAR(20) NOT NULL
);



INSERT INTO customer (Customer_id, first_name, last_name, Address, email, Date_joined, phone_num, Identification_number)
VALUES
(1, 'Karlan', 'Dabel', 'Cairo', 'kdabel0@webnode.com', '8/26/2024', '707-192-5327', '7696168568'),
(2, 'Benedicto', 'Blakeley', 'Tanta', 'bblakeley1@salon.com', '4/30/2024', '584-881-8841', '9042270969'),
(3, 'Kerry', 'Budcock', 'giza', 'kbudcock2@earthlink.net', '2/26/2024', '292-399-4091', '1359066748'),
(4, 'Alexina', 'Monk', 'tanta', 'amonk3@booking.com', '10/19/2024', '165-257-1261', '3263800302'),
(5, 'Beatriz', 'Streeten', 'Tanta', 'bstreeten4@apple.com', '1/7/2024', '124-326-4225', '7280992358'),
(6, 'Dusty', 'Andretti', 'Giza', 'dandretti5@virginia.edu', '8/6/2024', '478-607-6033', '8109566855'),
(7, 'Mia', 'Ruggs', 'Giza', 'mruggs6@examiner.com', '1/24/2024', '312-675-2540', '2285477597'),
(8, 'Wynnie', 'Masserel', '1287 Michigan Hill', 'wmasserel7@delicious.com', '7/2/2024', '945-579-9891', '9293042681'),
(9, 'Ky', 'Drane', '11 Elka Crossing', 'kdrane8@gnu.org', '3/20/2024', '304-887-5442', '6867375855'),
(10, 'Jazmin', 'Oakshott', '05347 Buell Drive', 'joakshott9@pcworld.com', '6/10/2024', '461-310-9618', '1140393375'),
(11, 'Wittie', 'Nutbean', '36 Spenser Center', 'wnutbeana@nyu.edu', '10/3/2024', '222-181-1248', '6762999727'),
(12, 'Tiler', 'Toretta', '33 Maple Wood Place', 'ttorettab@squarespace.com', '4/25/2024', '956-987-7923', '7243690041'),
(13, 'Gwyn', 'Nares', '2 Little Fleur Park', 'gnaresc@aol.com', '12/12/2024', '559-808-1143', '7068987109'),
(14, 'Lenora', 'McGibbon', '8 Waubesa Avenue', 'lmcgibbond@ehow.com', '8/14/2024', '750-531-8332', '6774992609'),
(15, 'Zarla', 'Hassey', '928 Glacier Hill Junction', 'zhasseye@gnu.org', '1/29/2024', '539-591-2008', '7593908178'),
(16, 'Tedda', 'Ruck', '3772 Lakewood Gardens Parkway', 'truckf@sfgate.com', '1/3/2024', '333-316-5476', '4681423033'),
(17, 'Winny', 'Cuerdall', '24 Johnson Drive', 'wcuerdallg@dagondesign.com', '2/16/2024', '332-558-5290', '6480291840'),
(18, 'Marlena', 'Walthall', '713 Pankratz Terrace', 'mwalthallh@e-recht24.de', '9/9/2024', '798-803-1796', '4913377779'),
(19, 'Arni', 'Lavell', '7836 Lyons Alley', 'alavelli@springer.com', '4/29/2024', '144-933-1536', '7992783999'),
(20, 'Drud', 'Nobes', '7306 Kennedy Parkway', 'dnobesj@salon.com', '2/22/2024', '194-753-1076', '2633305253'),
(21, 'Paola', 'Dancey', '264 Washington Plaza', 'pdanceyk@instagram.com', '1/16/2024', '250-905-2040', '669998095'),
(22, 'Danice', 'OLoughlin', '195 Chinook Crossing', 'doloughlinl@imdb.com', '12/20/2023', '848-965-8788', '8048894475'),
(23, 'Jocko', 'Gantley', '21 Kenwood Road', 'jgantleym@fc2.com', '3/19/2024', '661-647-8135', '8522578435'),
(24, 'Blythe', 'Quoit', '96010 Hintze Pass', 'bquoitn@telegraph.co.uk', '11/11/2024', '771-997-0229', '769049737'),
(25, 'Giffard', 'Grevile', '13680 Green Way', 'ggrevileo@wikimedia.org', '11/27/2024', '530-990-3045', '3089171716');

CREATE TABLE Account (
    Account_id INT PRIMARY KEY,
    [Status] NVARCHAR(20),
    Balance DECIMAL(18,2) DEFAULT 0,
    Date_created DATE,
    [Type] NVARCHAR(50),
    Customer_id INT NOT NULL,
    constraint c3 FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id)
);


INSERT INTO Account (Account_id, [Status], Balance, Date_created, [type], customer_id)
VALUES
(1, 'blocked', 0, '2024-03-23', 'laser', 1),
(2, 'closed', 0, '2024-09-17', 'jcb', 2),
(3, 'inactive', 0, '2024-09-20', 'visa-electron', 3),
(4, 'frozen', 0, '2024-03-07', 'solo', 4),
(5, 'active account', 0, '2024-05-06', 'visa', 5),
(6, 'inactive', 0, '2024-04-10', 'visa-electron', 6),
(7, 'blocked', 0, '2024-03-18', 'maestro', 7),
(8, 'closed', 0, '2024-04-17', 'jcb', 8),
(9, 'frozen', 0, '2024-03-20', 'jcb', 9),
(10, 'frozen', 0, '2024-07-11', 'jcb', 10),
(11, 'active account', 0, '2024-11-13', 'mastercard', 11),
(12, 'active account', 0, '2024-12-07', 'visa', 12),
(13, 'active account', 0, '2024-01-30', 'jcb', 13),
(14, 'active account', 0, '2024-08-21', 'visa', 14),
(15, 'closed', 0, '2024-01-04', 'americanexpress', 15),
(16, 'inactive', 0, '2024-10-03', 'laser', 16),
(17, 'blocked', 0, '2024-10-21', 'jcb', 17),
(18, 'blocked', 0, '2024-11-10', 'switch', 18),
(19, 'inactive', 0, '2024-08-27', 'switch', 19),
(20, 'active account', 0, '2024-02-13', 'maestro', 20),
(21, 'active account', 0, '2024-02-27', 'bankcard', 21),
(22, 'closed', 0, '2024-03-24', 'instapayment', 22),
(23, 'closed', 0, '2023-12-28', 'mastercard', 23),
(24, 'frozen', 0, '2024-07-09', 'jcb', 24),
(25, 'frozen', 0, '2024-11-27', 'maestro', 25);


CREATE TABLE Loan (
    Loan_id INT PRIMARY KEY,
    [Start] DATE NOT NULL,
    [End] DATE NOT NULL,
    [Status] NVARCHAR(20),
    Amount DECIMAL(18,2) NOT NULL,
    Rate DECIMAL(5,2),
    Purpose NVARCHAR(50),
    Account_id INT NOT NULL,
    
);

alter table loan
drop column rate

alter table loan 
alter column Account_id INT NULL

alter table loan
add constraint c4 FOREIGN KEY (Account_id) REFERENCES Account(Account_id) on delete set null on update cascade

INSERT INTO Loan VALUES (1, '2025-08-25', '2029-08-18', 'active', 10292.57, 'car', 17);
INSERT INTO Loan VALUES (2, '2026-08-21', '2030-04-29', 'closed', 14554.43, 'home', 7);
INSERT INTO Loan VALUES (3, '2025-12-31', '2027-08-19', 'active', 48217.88, 'education', 11);
INSERT INTO Loan VALUES (4, '2028-12-11', '2031-08-26', 'defaulted', 28958.17,'car', 23);

CREATE TABLE [Card] (
    Card_id INT PRIMARY KEY,
    [Password] NVARCHAR(255) default 1234,
    Number NVARCHAR(20) NOT NULL,
    [Status] NVARCHAR(20),
    Expired DATE NOT NULL,
    [Type] NVARCHAR(20),
    Account_id INT NOT NULL,
    
);


alter table loan 
alter column Account_id INT NULL

alter table loan 
add constraint c5 FOREIGN KEY (Account_id) REFERENCES Account(Account_id)  

INSERT INTO [Card] (Card_id, [password], [type], Number, Expired, [status], Account_id)
VALUES
(1, '#1b78fd', 'mastercard', '2010200551', '2033-11-01', 'blocked', 11),
(2, '#156eba', 'dolary', '2076425195', '2035-08-01', 'active', 12),
(3, '#585e12', 'mastercard', '3270017715', '2031-11-01', 'active', 3),
(4, '#438465', 'dolary', '259878731', '2047-06-01', 'closed', 14),
(5, '#15b956', 'student_visa', '1775923193', '2050-07-01', 'blocked', 10),
(6, '#ee8727', 'mastercard', '4706396743', '2041-12-01', 'active', 6),
(7, '#dc5730', 'visa', '7092978874', '2035-02-01', 'closed', 6),
(8, '#c2c856', 'student_visa', '1579868932', '2044-02-01', 'active', 8),
(9, '#f9aadf', 'visa', '4976206211', '2055-05-01', 'blocked', 9),
(10, '#6d7aa2', 'dolary', '4525587687', '2039-09-01', 'active', 1),
(11, '#39bf3f', 'mastercard', '4145433459', '2046-03-01', 'active', 1),
(12, '#30ee5d', 'dolary', '4834285022', '2018-08-01', 'closed', 12),
(13, '#01b9b1', 'student_visa', '3090703262', '2034-09-01', 'active', 3),
(14, '#efa9ce', 'mastercard', '6878526159', '2045-03-01', 'blocked', 4),
(15, '#ae47ad', 'visa', '6917646776', '2048-02-01', 'active', 15),
(16, '#35fbc9', 'dolary', '1020310340', '2039-05-01', 'active', 16),
(17, '#fffe35', 'visa', '9761451151', '2054-07-01', 'closed', 1),
(18, '#ca1986', 'mastercard', '6403331582', '2059-05-01', 'active', 8),
(19, '#4b080f', 'student_visa', '5036342194', '2024-02-01', 'blocked', 1),
(20, '#19ee45', 'visa', '4356538390', '2038-04-01', 'active', 2),
(21, '#f3fcbb', 'dolary', '6354133530', '2047-11-01', 'closed', 12),
(22, '#adefc7', 'visa', '8851347247', '2051-04-01', 'active', 12),
(23, '#35e770', 'mastercard', '8638725469', '2035-04-01', 'active', 2),
(24, '#d41332', 'visa', '5575367789', '2046-09-01', 'active', 20),
(25, '#49c59a', 'student_visa', '3817539770', '2030-06-01', 'blocked', 20);


CREATE TABLE [Transaction] (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Amount DECIMAL(18,2) NOT NULL,
    [Type] NVARCHAR(20),
    [Date] DATE NOT NULL,
    Account_id INT NOT NULL,
    constraint c6 FOREIGN KEY (Account_id) REFERENCES Account(Account_id)
);


alter table [Transaction]
add constraint c6 FOREIGN KEY (Account_id) REFERENCES Account(Account_id)


INSERT INTO [transaction] VALUES ( 7561.89, 'deposit', '2025-11-03', 14);
INSERT INTO [transaction] VALUES ( 6899.28, 'deposit', '2025-08-05', 18);
INSERT INTO [transaction] VALUES ( 5219.36, 'deposit', '2025-01-13', 24);
INSERT INTO [transaction] VALUES ( 7775.62, 'deposit', '2025-02-12', 6);
INSERT INTO [transaction] VALUES ( 9723.20, 'deposit', '2025-09-14', 8);
INSERT INTO [transaction] VALUES ( 9009.70, 'deposit', '2025-06-01', 25);
INSERT INTO [transaction] VALUES ( 5123.45, 'deposit', '2025-04-10', 21);
INSERT INTO [transaction] VALUES ( 6789.12, 'deposit', '2025-07-15', 5);
INSERT INTO [transaction] VALUES ( 8456.78, 'deposit', '2025-10-20', 3);
INSERT INTO [transaction] VALUES (9345.67, 'deposit', '2025-12-25', 13);
INSERT INTO [transaction] VALUES (6789.01, 'deposit', '2025-03-30', 17);
INSERT INTO [transaction] VALUES (7890.12, 'deposit', '2025-05-05', 22);
INSERT INTO [transaction] VALUES (5678.90, 'deposit', '2025-06-20', 16);
INSERT INTO [transaction] VALUES (6789.34, 'deposit', '2025-08-25', 7);
INSERT INTO [transaction] VALUES (7890.56, 'deposit', '2025-09-30', 12);
INSERT INTO [transaction] VALUES (8901.23, 'deposit', '2025-11-15', 4);
INSERT INTO [transaction] VALUES (9012.34, 'deposit', '2025-12-01', 23);
INSERT INTO [transaction] VALUES (5123.45, 'deposit', '2025-01-20', 15);
INSERT INTO [transaction] VALUES (6234.56, 'deposit', '2025-02-25', 19);
INSERT INTO [transaction] VALUES (7345.67, 'deposit', '2025-03-10', 9);
INSERT INTO [transaction] VALUES (8456.78, 'deposit', '2025-04-15', 11);
INSERT INTO [transaction] VALUES (9567.89, 'deposit', '2025-05-30', 1);
INSERT INTO [transaction] VALUES (5678.90, 'deposit', '2025-07-05', 2);
INSERT INTO [transaction] VALUES (6789.01, 'deposit', '2025-08-20', 10);
INSERT INTO [transaction] VALUES (7890.12, 'deposit', '2025-10-05', 20);

INSERT INTO [transaction] VALUES ( 1586.43, 'withdraw', '2025-10-03', 6);
INSERT INTO [transaction] VALUES ( 1335.23, 'withdraw', '2025-05-20', 3);
INSERT INTO [transaction] VALUES ( 1910.73, 'withdraw', '2025-03-18', 5);
INSERT INTO [transaction] VALUES ( 1851.48, 'withdraw', '2025-04-16', 1);
INSERT INTO [transaction] VALUES ( 1919.53, 'withdraw', '2025-06-12', 7);
INSERT INTO [transaction] VALUES ( 1670.99, 'withdraw', '2025-02-04', 9);
INSERT INTO [transaction] VALUES ( 1725.34, 'withdraw', '2025-09-04', 2);
INSERT INTO [transaction] VALUES ( 1934.22, 'withdraw', '2025-08-30', 4);
INSERT INTO [transaction] VALUES ( 1791.41, 'withdraw', '2025-11-05', 8);


CREATE TABLE incoming_transfers (
    Id INT PRIMARY KEY identity,
    [Date] DATE NOT NULL,
    Amount DECIMAL(18,2) NOT NULL,
    Destination_account INT NOT NULL,
    Account_id INT NOT NULL,
    
);

alter table incoming_transfers
add constraint c7 FOREIGN KEY (Account_id) REFERENCES Account(Account_id)

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-02-14 16:55', 500.22, 1, 1);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-09-21 08:19', 500.53, 22, 20);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-12-07 14:56', 706.82, 33, 13);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-08-23 06:35', 608.84, 40, 14);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-04-19 16:28', 308.47, 51, 1);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-12-13 19:56', 219.40, 60, 16);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-08-30 22:11', 110.77, 7, 17);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-07-28 02:25', 800.31, 8, 18);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-04-18 20:52', 298.90, 8, 9);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-03-20 08:38', 570.07, 11, 1);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-01-09 01:47', 100.90, 11, 1);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2023-12-30 11:17', 600.99, 2, 12);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-01-24 16:25', 600.76, 13, 3);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-08-08 08:31', 800.32, 4, 14);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-07-30 04:15', 898.28, 15, 5);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-04-03 07:48', 924.51, 16, 1);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-06-18 16:35', 924.65, 27, 17);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-09-25 00:47', 702.17, 18, 18);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-03-24 15:40', 254.29, 9, 8);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-10-08 14:19', 305.66, 20, 20);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-11-20 09:37', 828.62, 21, 8);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-04-26 12:59', 105.79, 20, 2);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-01-27 06:14', 250.98, 23, 7);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2023-12-25 08:50', 702.69, 24, 4);

INSERT INTO incoming_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-01-04 06:29', 156.64, 85, 2);

CREATE TABLE Noutgoing_transfers (
    Id INT PRIMARY KEY identity,
    [Date] DATE NOT NULL,
    Amount DECIMAL(18,2) NOT NULL,
    Destination_account INT NOT NULL,
    Account_id INT NOT NULL,
    
);


alter table outgoing_transfers
add constraint c8 FOREIGN KEY (Account_id) REFERENCES Account(Account_id)


INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-08-01 14:46', 117.61, 11, 20);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-08-28 22:01', 269.39, 21, 2);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-02-16 23:54', 947.86, 3, 3);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-12-06 00:25', 200.87, 44, 14);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-04-26 17:40', 602.42, 5, 15);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-04-23 19:42', 127.90, 6, 6);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-09-05 18:52', 567.12, 17, 7);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-08-19 01:52', 248.53, 8, 18);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ('2024-01-26 02:05', 114.80, 19, 19);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-07-19 07:40', 717.39, 1, 10);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-04-29 08:22', 240.94, 11, 1);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-01-14 17:05', 247.80, 2, 12);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2023-12-29 09:09', 304.75, 13, 3);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-04-21 02:49', 141.98, 4, 1);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-01-24 17:02', 120.63, 15, 5);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-11-19 06:11', 604.43, 14, 16);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-03-19 12:03', 702.83, 17, 7);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-07-07 04:46', 602.37, 8, 18);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-11-15 09:22', 904.13, 29, 9);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-07-16 06:21', 305.59, 20, 20);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-11-09 22:35', 622.02, 2, 1);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-08-21 23:15', 704.32, 22, 2);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-11-06 01:16', 804.93, 33, 23);

INSERT INTO outgoing_transfers ( [Date], Amount, Destination_account, Account_id)VALUES ( '2024-03-11 11:15', 801.49, 24, 4);


---------------------------------------------------------------------------------------
--enable TRIGGER TR_UpdateAccountBalance ON [Transaction];

CREATE TRIGGER TR_UpdateAccountBalance ON [Transaction]
AFTER INSERT 
AS
BEGIN
    DECLARE @AccountID INT, @Amount DECIMAL(18,2), @TransactionType VARCHAR(20);

    SET @AccountID = (SELECT Account_id FROM INSERTED);
    SET @Amount = (SELECT Amount FROM INSERTED);
    SET @TransactionType = (SELECT [Type] FROM INSERTED);

    IF @TransactionType = 'Withdraw'
    BEGIN
        DECLARE @CurrentBalance DECIMAL(18,2);
        SELECT @CurrentBalance = Balance FROM Account WHERE Account_id = @AccountID;

        IF @Amount > @CurrentBalance
            BEGIN
                RAISERROR ('Insufficient funds for withdrawal.', 16, 1);
                ROLLBACK TRANSACTION;
            END
        ELSE
            BEGIN
                UPDATE Account
                SET Balance = Balance - @Amount
                WHERE Account_id = @AccountID;
            END
    END
    ELSE IF @TransactionType = 'Deposit'
    BEGIN
        UPDATE Account
        SET Balance = Balance + @Amount
        WHERE Account_id = @AccountID;
    END
END;

---------------------------------------------------------------------------------------
--enable TRIGGER TR_incoming_transfers ON incoming_transfers
CREATE TRIGGER TR_incoming_transfers ON incoming_transfers
AFTER INSERT 
AS
BEGIN
    DECLARE @AccountID INT, @Amount DECIMAL(18,2)

    SET @AccountID = (SELECT Account_id FROM INSERTED);
    SET @Amount = (SELECT Amount FROM INSERTED);
  
    
                UPDATE Account
                SET Balance = Balance + @Amount
                WHERE Account_id = @AccountID;
          
END;

---------------------------------------------------------------------------------------
--enable TRIGGER TR_outgoing_transfers ON outgoing_transfers
CREATE TRIGGER TR_outgoing_transfers ON outgoing_transfers
AFTER INSERT 
AS
BEGIN
    DECLARE @AccountID INT, @Amount DECIMAL(18,2)

    SET @AccountID = (SELECT Account_id FROM INSERTED);
    SET @Amount = (SELECT Amount FROM INSERTED);
 
        DECLARE @CurrentBalance DECIMAL(18,2);
        SELECT @CurrentBalance = Balance FROM Account WHERE Account_id = @AccountID;

        IF @Amount > @CurrentBalance
            BEGIN
                RAISERROR ('Insufficient funds for transfer.', 16, 1);
                ROLLBACK TRANSACTION;
            END
        ELSE
            BEGIN
                UPDATE Account
                SET Balance = Balance - @Amount
                WHERE Account_id = @AccountID;
            END
   
  
END;

---------------------------------------------------------------------------------------

CREATE TRIGGER TR_Loan_AfterInsert ON Loan
AFTER INSERT
AS
BEGIN
    DECLARE @AccountID INT, @Amount DECIMAL(18,2)

    SELECT @AccountID = Account_id, @Amount = Amount FROM INSERTED;

    UPDATE Account
    SET Balance = Balance + @Amount
    WHERE Account_id = @AccountID;
END;


------------------------------------------------------------------------

CREATE PROCEDURE CheckUserCredentials
    @Username VARCHAR(255),
    @Password VARCHAR(255)
AS
BEGIN
    IF EXISTS (
        SELECT 1
        FROM Employee 
        WHERE Username = @Username
          AND Password = @Password
    )
    BEGIN
        SELECT 1;
    END
    ELSE
    BEGIN
        SELECT 0;
    END
END;

------------------------------------------------------------------------

CREATE Procedure Deposit_Withdraw (
    @Account_id INT,
    @Amount DECIMAL(18, 2),
    @TransactionType NVARCHAR(20),
    @TransactionDate DATE
)
AS
BEGIN
    DECLARE @CurrentBalance DECIMAL(18, 2);
    
    -- Check if the account exists
    IF EXISTS (SELECT 1 FROM Account WHERE Account_id = @Account_id)
    BEGIN
        
        -- Insert the transaction
        INSERT INTO [Transaction] VALUES (@Amount, @TransactionType, @TransactionDate, @Account_id);

        
    END
   
END;
------------------------------------------------------------------------

CREATE Procedure Transfer (
    @SAccount_id INT,
	@DAccount_id INT,
    @Amount DECIMAL(18, 2),
    @TransferDate DATE
)
AS
BEGIN
    
		BEGIN TRANSACTION;
	    BEGIN TRY
   
        INSERT INTO incoming_transfers values (@TransferDate, @Amount, @SAccount_id, @DAccount_id)
	    INSERT INTO outgoing_transfers values (@TransferDate, @Amount, @DAccount_id, @SAccount_id)

         COMMIT;
	 END TRY
	  BEGIN CATCH
        -- Rollback the transaction in case of error
        ROLLBACK;

       
    END CATCH
 
END;


------------------------------------------------------------------------

CREATE FUNCTION check_balance (
    @id INT,
    @withdraw_amount DECIMAL(18, 2)
)
RETURNS BIT
AS
BEGIN
    DECLARE @account_balance DECIMAL(18,2);
    SELECT @account_balance = balance FROM account WHERE account_id = @id;
    
    IF @account_balance >= @withdraw_amount
        RETURN 1;
   
    RETURN 0;
END;

------------------------------------------------------------------------

CREATE PROCEDURE My_Account
    @in INT
AS
BEGIN
    IF EXISTS (SELECT 1 FROM account WHERE Account_id = @in)
    BEGIN
        DECLARE @Status NVARCHAR(50), @Balance nvarchar(50);

       
        SELECT @Status = Status, @Balance = Balance
        FROM account
        WHERE Account_id = @in;

        
        IF (@Status = 'active account')
        BEGIN
            SELECT 'OK, how can I help you' AS Message, @Balance AS Balance;
        END
        ELSE
        BEGIN
            SELECT 'Sorry, try solving the problem with your account' AS Message;
        END
    END
    ELSE
    BEGIN
        SELECT 'Sorry, you have no account' AS Message;
    END
END

EXEC My_Account @in=11


