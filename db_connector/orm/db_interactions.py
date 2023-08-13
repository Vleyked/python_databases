import sqlalchemy as sa

# Create the Book database connection
engine = sa.create_engine("sqlite:///books.sqlite")
Base = sa.MetaData()

author_table = sa.Table(
    "authors",
    Base,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
    sa.Column("name", sa.String(255)),
)

books_table = sa.Table(
    "books",
    Base,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
    sa.Column("title", sa.String(255)),
    sa.Column("author_id", sa.Integer, sa.ForeignKey("authors.id")),
    sa.Column("genre_id", sa.Integer, sa.ForeignKey("genres.id")),
)

genres_table = sa.Table(
    "genres",
    Base,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
    sa.Column("name", sa.String(255)),
)

# Create the tables
Base.create_all(bind=engine)

author1 = author_table.insert().values(name="Stephen King")
author2 = author_table.insert().values(name="Tom Clancy")
author3 = author_table.insert().values(name="John Grishom")

book1 = books_table.insert().values(title="The Shining", author_id=1, genre_id=1)
book2 = books_table.insert().values(title="Patriot Games", author_id=2, genre_id=2)
book3 = books_table.insert().values(title="The Firm", author_id=3, genre_id=2)

genre1 = genres_table.insert().values(name="Horror")
genre2 = genres_table.insert().values(name="Thriller")
