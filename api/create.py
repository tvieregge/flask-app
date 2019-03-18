create_table = """CREATE TABLE posts (
                      id INT PRIMARY KEY,
                      text TEXT,
                      parent INT
                  );"""

insert_into = """INSERT INTO users (username, password)
                 VALUES ('admin', 'test');"""

insert_two = """INSERT INTO users (username, password)
                 VALUES ('two', 'two');"""

where = """SELECT * FROM users
           WHERE username='admin'"""
