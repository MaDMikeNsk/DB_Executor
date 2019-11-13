from Brand import Brand
from Auto import Auto
from DBExecutor import DBExecutor
from User import User

db = DBExecutor()

# Добавим юзера в базу
user = User(first_name='Michael', last_name='Jordan', birthday_date='23/11/1946')
db.push_user(user)

# Добавим авто в базу
auto = Auto(name='Camry', year=2015)
db.push_auto(auto)

# Добавим бренд в базу
brand = Brand(name='TOYOTA')
db.push_brand(brand)