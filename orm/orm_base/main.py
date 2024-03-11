from models import *


def get_publisher(DSN):
    engine = sq.create_engine(DSN)
    Session = sessionmaker(bind=engine)
    session = Session()
    create_tables(engine)
    target = input('Введите имя или ID искомого издателя: ')
    if target.isdigit():
        publisher = Publisher.id
        target = int(target)
    else:
        publisher = Publisher.name
    author = session.query(Publisher).filter(publisher == target).all()
    print(author[0])
    res = session.query(Shop).join(Stock, Shop.id == Stock.id_shop) \
        .join(Book, Book.id == Stock.id_book) \
        .join(Publisher, Book.id_publisher == Publisher.id) \
        .filter(publisher == target).all()
    for shop in res:
        print(shop)
    session.close()


get_publisher('DSN')
