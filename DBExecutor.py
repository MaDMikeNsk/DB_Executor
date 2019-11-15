from typing import Dict

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from AutoUser import AutoUser
from AutoBrand import AutoBrand
from Brand import Brand
from Auto import Auto
from User import User


class DBExecutor:
    def __init__(self):
        self.engine = create_engine('sqlite:///DataBase/CompanyCars.db', echo=True)
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def push_user(self, user: User):
        self.session.add(user)
        self.session.commit()

    def push_auto(self, auto: Auto, brand_name: str):
        self.session.add(auto)
        self.session.commit()
        self.create_auto_brand_path({brand_name: [auto.name]})

    def push_brand(self, brand: Brand):
        self.session.add(brand)
        self.session.commit()

    def get_user_by_first_name(self, first_name):
        result = self.session.query(User, AutoUser).join(AutoUser, User.id == AutoUser.user_id).filter(User.first_name == first_name)
        self.session.commit()
        return result.all()

    def get_user_by_last_name(self, last_name):
        return self.session.query(User).filter(User.last_name == last_name).all()

    def create_auto_brand_path(self, brand_map: Dict):
        for brand in brand_map:
            current_brand = self.session.query(Brand).filter(Brand.name == brand)
            current_auto_list = self.session.query(Auto).filter(Auto.name.in_(brand_map[brand]))

            current_brand = current_brand[0] if current_brand else None

            auto_id_list = [auto.id for auto in current_auto_list]

            self.session.add_all(
                [
                    AutoBrand(
                        brand_id=current_brand.id,
                        auto_id=auto_id
                    ) for auto_id in auto_id_list
                ]
            )
            self.session.commit()
