from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Auto import Auto
from User import User

engine = create_engine('sqlite:///C:/Python/PycharmProjects/DB_Executor/DataBase/AutoDB.db', echo=True)
Session = sessionmaker(bind=engine)
Session = Session()

# Добавим юзера в базу
user = User(first_name='John', last_name='Smit', birthday_date='01/06/1987')
Session.add(user)
Session.commit()

# Добавим авто в базу
auto = Auto(name='Lexus', year=2010)
Session.add(auto)
Session.commit()
