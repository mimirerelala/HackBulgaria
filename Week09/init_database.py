import sqlite3


def create_database():
    conn = sqlite3.connect('cinema.db')
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS movies(
                movie_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                movie_name VARCHAR(255) NOT NULL,
                movie_rating REAL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS projections(
                projection_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                movie_id INTEGER NOT NULL,
                projection_type VARCHAR(5),
                projection_date_time DATE,
                FOREIGN KEY(movie_id) REFERENCES movies(movie_id))''')
    c.execute('''CREATE TABLE IF NOT EXISTS reservations(
                reservation_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                username VARCHAR(255) NOT NULL,
                movie_id INTEGER NOT NULL,
                row TINYINT NOT NULL,
                column TINYINT NOT NULL,
                FOREIGN KEY(movie_id) REFERENCES movies(movie_id))''')
    # Insert rows of data
    c.execute('''INSERT INTO movies (movie_name,movie_rating)
                VALUES ("The Hunger Games: Catching Fire",7.9),
                 ("Wreck-It Ralph",7.8),
                 ("Her",8.3)''')
    c.execute('''INSERT INTO projections (movie_id,projection_type,projection_date_time)
                VALUES ("1","3D ","2014-04-01T19:10"),
                 ("1","2D ","2014-04-01T19:00"),
                 ("1","4DX","2014-04-02T21:00"),
                 ("3","2D ","2014-04-05T20:20"),
                 ("2","3D ","2014-04-02T22:00"),
                 ("2","2D ","2014-04-02T19:30")''')
    c.execute('''INSERT INTO reservations(username,movie_id,row,column)
                VALUES ("RadoRado",1,2,1),
                ("RadoRado",1,3,5),
                ("RadoRado",1,7,8),
                ("Ivo",3,1,1),
                ("Ivo",3,1,2),
                ("Mysterious",5,2,3),
                ("Mysterious",5,2,4)''')
    # could use execute many!!!
    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

