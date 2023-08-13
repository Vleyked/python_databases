"""
1. Alter table

* Add a rating column to the movies table
* Add a phone column to the customers table
* Create Indexes 
    - `idx_movies_director` on movies
    - `idx_movie_actors_movie` on movie_actors
    - `idx_movie_actors_actor` on movie_actors
    - `idx_rentals_movie` on rentals
    - `idx_rentals_customer` on rentals

2. Data manipulation

* directors 
    name
    Steven Spielberg
* movies
    title, director_id, release_date, genre, rental_price
    Jurassic Park, 1, 1993-0611, Adventure, 11
* customers
    username, email, phone
    yourname, test@test.com, 666123123
* rentals
        movie_id, customer_id, rental_date, return_date, returned
        1, 1, 2000-01-01, null, 0

3. Queries
* Get the title of a movie filtered by the director with a join
* Get title of a movie
* Get title, client_id, rental_date of that movie filtered by customer name
    HINTS: JOIN (rentals, customers) WHERE  

"""

import sqlite3

# Connect to the db
conn = sqlite3.connect("movies.sqlite")
cursor = conn.cursor()


# 1. Alter table

# * Add a rating column to the movies table
# * Add a phone column to the customers table

cursor.execute(
    """
ALTER TABLE movies ADD COLUMN rating REAL
"""
)

cursor.execute(
    """
ALTER TABLE customers ADD COLUMN phone TEXT
"""
)

# * Create Indexes
#     - `idx_movies_director` on movies
#     - `idx_movie_actors_movie` on movie_actors
#     - `idx_movie_actors_actor` on movie_actors
#     - `idx_rentals_movie` on rentals
#     - `idx_rentals_customer` on rentals

cursor.execute(
    """
CREATE INDEX idx_movies_director ON movies (director_id)
"""
)

cursor.execute(
    """
CREATE INDEX idx_movie_actors_movie ON movie_actors (movie_id)
"""
)

cursor.execute(
    """
CREATE INDEX idx_movie_actors_actor ON movie_actors (actor_id)
"""
)
cursor.execute(
    """
CREATE INDEX idx_rentals_movie ON rentals (movie_id)
"""
)
cursor.execute(
    """
CREATE INDEX idx_rentals_customer ON rentals (customer_id)
"""
)

# Insert into directors
cursor.execute(
    """
INSERT INTO directors (name)
VALUES ('Steven Spielberg'),
('Alfred Hitchcock'),
('Martin Scorcese')
"""
)

# Insert into movies
cursor.execute(
    """
INSERT INTO movies (title, director_id, release_date, genre, rental_price, rating)
VALUES ('Jurassic Park', 1, '1993-06-11', 'Adventure', 11, 9.3),
('Family Plot', 2, '1976-04-05', 'Comedy', 7, 6.8),
('Goodfellas', 3, '1990-01-01', 'Crime', 11, 8.7)
"""
)

# # Insert into customers
cursor.execute(
    """
INSERT INTO customers (username, email, phone)
VALUES ('user1', 'user1@gmail.com', '666666666'),
('user2', 'user2@gmail.com', '666999999'),
('user3', 'user3@gmail.com', '666777777')
"""
)

# # Insert into rentals
cursor.execute(
    """
INSERT INTO rentals (movie_id, customer_id, rental_date, returned)
VALUES (1, 1, '2023-08-13', 0),
(3, 3, '2023-08-12', 0)
"""
)

# 3. Queries


def movies_by_director(director_name: str, cursor):
    """Fetch movie title by director name

    Arguments
    ---------
        director_name: The name of the director

    Returns
    -------

        Filtered movie titles
    """
    cursor.execute(
        """
    SELECT title FROM movies
    JOIN directors ON movies.director_id = directors.director_id
    WHERE directors.name = ?
    """,
        (director_name,),
    )
    return cursor.fetchall()


def rentals_by_customer(customer_username: str, cursor):
    """Fetch the movie.title, client_id, rental_date

    Arguments
    ---------
        customer_name: The nae of a customer

    Returns
    -------
        Filtered movie.title, client_id, and rental_date
    """

    cursor.execute(
        """
    SELECT movies.title, customers.customers_id, rentals.rental_date
    FROM movies
    JOIN rentals ON movies.movies_id = rentals.movie_id
    JOIN customers ON rentals.customer_id = customers.customers_id
    WHERE customers.username = ?
    """,
        (customer_username,),
    )

    return cursor.fetchall()


# print(movies_by_director("Martin Scorcese", cursor=cursor))

print(rentals_by_customer("user1", cursor=cursor))

conn.commit()
conn.close()
