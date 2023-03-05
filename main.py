import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale


def upload_info(session):
    with open("tests_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for el in data:
            model = {"publisher": Publisher, "book": Book,
                     "shop": Shop, "stock": Stock, "sale": Sale}[el.get("model")]
            session.add(model(id=el.get("pk"), **el.get("fields")))
        session.commit()


def main():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    name_db = input("Введите название базы данных: ")
    DSN = f"postgresql://{login}:{password}@localhost:5432/{name_db}"
    engine = sqlalchemy.create_engine(DSN)

    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    upload_info(session)
    command = input("Введите имя издателя: ")
    query = session.query(Publisher).join(Stock).join(Shop).join(Book).join(Sale).filter(Publisher.name.ilike(f'%{command}%'))
    print(f'{query.stock.book.title} | {query.stock.shop.name} | {query.price} | {query.date_sale}')

    session.close()


if __name__ == '__main__':
    main()
