from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import Brand, User, Auto


class DBExecutor:
    def __init__(self):
        self.engine = create_engine('sqlite:///DataBase/CompanyCars.db', echo=True)
        session = sessionmaker(bind=self.engine)
        self.session = session.configure(bind=self.engine)
#        self.session = Session()

    def push_user(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.close()

    def push_auto(self, auto: Auto):
        self.session.add(auto)
        self.session.commit()
        self.session.close()

    def push_brand(self, brand: Brand):
        self.session.add(brand)
        self.session.commit()
        self.session.close()
