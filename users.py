import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"

# базовый класс моделей таблиц
Base = declarative_base()

class User(Base):
	__tablename__ = "user"
	id = sa.Column(sa.INTEGER, primary_key=True)
	first_name = sa.Column(sa.TEXT)
	last_name = sa.Column(sa.TEXT)
	gender = sa.Column(sa.TEXT)
	email = sa.Column(sa.TEXT)
	birthdate = sa.Column(sa.TEXT)
	height = sa.Column(sa.REAL)

def connect_db():
	# подключение к БД
	engine = sa.create_engine(DB_PATH)
	# cоздание фабрики сессии
	session = sessionmaker(engine)
	# возврат сессии
	return session()

def request_data():
	print("Привет! Введите Ваши данные! ")
	first_name = input("Введите Ваше имя: ")
	last_name = input("Введите Вашу фамилию: ")
	gender = input("Введите Ваш пол (Male/Female): ")
	email = input("Введите адрес электронной почты: ")
	birthdate = input("Введите день своего рождения в формате гггг-мм-дд: ")
	height = input("Введите свой рост в метрах: ")
	user = User(
		first_name = first_name,
		last_name = last_name,
		email = email,
		gender = gender,
		birthdate = birthdate,
		height = height,
	)
	return user


def  main():
	session = connect_db()
	user = request_data()
	session.add(user)
	session.commit()
	print ("Данные сохранены")


if __name__ == "__main__":
	main()
