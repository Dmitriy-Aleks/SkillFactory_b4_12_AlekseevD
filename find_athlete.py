import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from users import connect_db
from users import User

# базовый класс моделей таблиц
Base = declarative_base()

class Athelete(Base):
	__tablename__ = "athelete"
	id = sa.Column(sa.INTEGER, primary_key=True)
	# age = sa.Column(sa.INTEGER)
	birthdate = sa.Column(sa.TEXT)
	# gender = sa.Column(sa.TEXT)
	height = sa.Column(sa.REAL)
	name = sa.Column(sa.TEXT)
	# weight = sa.Column(sa.INTEGER)
	# gold_medals = sa.Column(sa.INTEGER)
	# silver_medals = sa.Column(sa.INTEGER)
	# bronze_medals = sa.Column(sa.INTEGER)
	# total_medals = sa.Column(sa.INTEGER)
	# sport = sa.Column(sa.TEXT)
	# country = sa.Column(sa.TEXT)

def find(session):
	user_id = input("Введите идентификатор пользователя:\n")
	user = session.query(User).filter(User.id == user_id).first()

	# Для отладки и проверки можно раскоментить
	# print(user.first_name, user.last_name, user.birthdate, user.height)

	atheletes = session.query(Athelete).all()

	if user:
		# поиск ближайшего атлета по дате рождения
		candidate1 = atheletes[0]
		for athelete in atheletes:
			birthdate1 = datetime.strptime(athelete.birthdate, '%Y-%m-%d')
			birthdate2 = datetime.strptime(user.birthdate, '%Y-%m-%d')
			birthdate3 = datetime.strptime(candidate1.birthdate, '%Y-%m-%d')
			diff_birth1 = abs(birthdate1-birthdate2).days
			diff_birth2 = abs(birthdate3-birthdate2).days
			if diff_birth1 < diff_birth2: 
				candidate1 = athelete

		print("{} was born on {}".format(candidate1.name, candidate1.birthdate))  

		# поиск ближайшего атлета по росту
		candidate2 = atheletes[0]
		for athelete in atheletes:
			if athelete.height:
				diff_height1 = abs(athelete.height-user.height)
				diff_height2 = abs(candidate2.height-user.height)
				if diff_height1 < diff_height2:
					candidate2 = athelete
		print("{} height is {} m".format(candidate2.name, candidate2.height))

	else:
		print ("Пользователь не найден")

def  main():
	session = connect_db()
	result = find(session)
	session.commit()

if __name__ == "__main__":
	main()