CREATE TABLE users (
 id INT NOT NULL PRIMARY KEY,
 name VARCHAR(64) NOT NULL,
 address VARCHAR(64) NOT NULL,
 mail_address VARCHAR(64) NOT NULL,
 password VARCHAR(64) NOT NULL
);



CREATE TABLE events (
 event_id INT NOT NULL PRIMARY KEY,
 user_id INT,
 delivery_date VARCHAR(32) NOT NULL,
 info VARCHAR(64) NOT NULL,
 FOREIGN KEY (user_id) REFERENCES users(id)
);

