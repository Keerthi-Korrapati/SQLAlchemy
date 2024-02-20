from sqlalchemy import create_engine,text


engine = create_engine("postgresql://postgres:ke12@localhost:5432/Python-Postgres",echo=True)

with engine.connect() as connection:
    result = connection.execute(text('SELECT "name" FROM employee'))

    print(result.all())