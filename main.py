from Brand import Brand
from Auto import Auto
from DBExecutor import DBExecutor
from User import User

db = DBExecutor()
'''
# Добавим юзера в базу
user = User(first_name='Michael', last_name='Jordan', birthday_date='23/11/1946')
db.push_user(user)

# Добавим авто в базу
auto = Auto(name='Camry', year=2015)
db.push_auto(auto)

# Добавим бренд в базу
brand = Brand(name='TOYOTA')
db.push_brand(brand)
'''

brand_map = {'TOYOTA': ['Land Cruser', 'Camry'], 'LEXUS': 'LS540'}
#db.create_auto_brand_path(brand_map)

#auto = Auto(name='Corolla', year=2004,)
#db.push_auto(auto, 'TOYOTA')

my_name = db.get_user_by_first_name('Jack')
for name in my_name:
    print(name.name, name.id, name.auto_id)




db.session.close()
