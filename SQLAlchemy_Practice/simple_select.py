from main import session
from models import User,Comment
from sqlalchemy import select

# statement = select(User).where(User.username.in_(['shiva','Benny']))
# result = session.scalars(statement)


users = session.query(User).all()


for user in users:
    print(user) 



