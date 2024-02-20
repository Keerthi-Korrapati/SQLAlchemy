from models import User,Comment
from main import session


user1 = User(
    username = 'keerthi',
    email_address = "keerthi@sql.irg",
    comments = [
        Comment(text="Hello World"),
        Comment(text="Please subscribe")
    ]
)

shiva = User(
    username = 'shiva',
    email_address = "shiva@sql.irg",
    comments = [
        Comment(text="What's up?"),
        Comment(text="Please subscribe")
    ]
)

benny = User(
    username = 'Benny',
    email_address = "Benny@sql.irg",
)


session.add_all([user1,shiva,benny])

session.commit()