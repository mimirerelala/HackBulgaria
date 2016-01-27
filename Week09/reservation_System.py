import sqlite3
import os
import init_database

class Reservation_System:

    def __init__(self):
        if not os.path.exists('cinema.db'):
            init_database.create_database()
        self.conn = sqlite3.connect('cinema.db')

    def close(self):
        self.conn.close()

    def show_movies(self):
        c = conn.cursor()
        c.c.execute("""SELECT movie_id,movie_name,movie_rating FROM movies m ORDER BY m.movie_rating DESC""")
        all_movies = c.fetchall()
        print("Current movies:")
        for m in range(len(all_movies)):
            (m_id, m_name, m_rating) = all_movies[m]
            print("[{}] - {} ({})".format(m_id,m_name,m_rating))
        ###get the output :)


    def show_movie_projections(self, movie_id, date=None):
        if date is None:
            c.execute("""SELECT movie_name FROM movies WHERE movie_id=?""",(movie_id,))
            selected_movie = c.fetchone()[0]
            print("Projections for movie '{}':".format(selected_movie))
            c.execute("""SELECT projection_id,projection_date_time,projection_type FROM projections p WHERE movie_id=? ORDER BY p.projection_date_time""",(movie_id,))
            all_proj = c.fetchall()
            for p in all_proj:
                (p_id, p_date, p_type) = p
                print("[{}] - {} ({})".format(p_id, p_date, p_type))
        else:
            c.execute("""SELECT movie_name FROM movies WHERE movie_id=?""",(movie_id,))
            selected_movie = c.fetchone()[0]
            print("Projections for movie '{}' on {}:".format(selected_movie),date)
            c.execute("""SELECT projection_id,projection_date_time,projection_type FROM projections p WHERE movie_id=? and date(projection_date_time)=? ORDER BY p.projection_date_time""",(movie_id,date))
            all_proj = c.fetchall()
            for p in all_proj:
                (p_id, p_date, p_type) = p
                print("[{}] - {} ({})".format(p_id, p_date, p_type))

    def make_reservation(self, projection_id, username, row, col):
        pass

    def show_spots(self, projection_id):
        pass
