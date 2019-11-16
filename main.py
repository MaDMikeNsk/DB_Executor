from Brand import Brand
from Auto import Auto
from DBExecutor import DBExecutor
from User import User

db = DBExecutor()

brand_map = {'TOYOTA': ['Land Cruser', 'Camry', 'Corolla'], 'LEXUS': 'LS540'}


some_name = 'Hanks'
my_users = db.get_user_by_last_name(some_name)
if my_users:
    for user in my_users:
        print(user.first_name)
else:
    print(f'No users with last name {some_name} found')

users = db.get_user_by_first_name('Michael')
for user in users:
    print(user.User.last_name, user.User.birthday_date, user.AutoUser.auto_id)
print(type(users), len(users))
db.session.close()
