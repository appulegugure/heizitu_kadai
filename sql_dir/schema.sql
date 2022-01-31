--DROP TABLE users;
CREATE TABLE IF not exists users (
                username TEXT CHECK(LENGTH(username) >=0 and LENGTH(username) <= 21),
                age  INTEGER CHECK(age >= 0 and age <=120),
                PRIMARY KEY(username)
            );

