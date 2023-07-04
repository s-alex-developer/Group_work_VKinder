"""
    Модуль "db_models.py" содержит классы и методы для создания таблиц БД.

    Для создания таблиц в БД необходимо запустить этот модуль и заполнить файл с переменными окружения.

    Состав модуля:

        1. class SearchResults - модель создания таблицы БД "search_results", "Результаты поиска."

        2. class FavoriteProfiles - модель создания таблицы БД 'favorite_profiles', "Избранные профили."

        3. class BlockedProfiles - модель создания таблицы БД 'blocked_profiles', "Игнорируемые профили."

        4. Метод create_tables - создает таблицы в БД используя модели описанные в этом модуле.

        5. Метод delete_tables - удаляет все таблицы БД, созданные при помощи этого модуля.

"""


import sqlalchemy as sq
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class SearchResults(Base):

    __tablename__ = "search_results"

    id = sq.Column(sq.Integer, primary_key=True)
    result_id = sq.Column(sq.Integer, nullable=False)
    user_id = sq.Column(sq.Integer, nullable=False)
    vk_profile_href = sq.Column(sq.VARCHAR(50), nullable=False)
    first_name = sq.Column(sq.VARCHAR(50), nullable=False)
    last_name = sq.Column(sq.VARCHAR(50), nullable=False)
    photo_href_1 = sq.Column(sq.VARCHAR(50))
    photo_href_2 = sq.Column(sq.VARCHAR(50))
    photo_href_3 = sq.Column(sq.VARCHAR(50))

    __table_args__ = (sq.UniqueConstraint('user_id', 'vk_profile_href'),)

    def __str__(self):
        return f"search_results: id: {self.id}, user_id: {self.user_id}, result_id: {self.result_id}, " \
               f"vk_profile_href: {self.vk_profile_href}, first_name: {self.first_name}, last_name: {self.last_name}, "\
               f"photo_href_1: {self.photo_href_1}, photo_href_2: {self.photo_href_2}, " \
               f"photo_href_3: {self.photo_href_3}"


class FavoriteProfiles(Base):

    __tablename__ = 'favorite_profiles'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, nullable=False)
    vk_profile_href = sq.Column(sq.VARCHAR(50), nullable=False)
    first_name = sq.Column(sq.VARCHAR(50), nullable=False)
    last_name = sq.Column(sq.VARCHAR(50), nullable=False)
    photo_href_1 = sq.Column(sq.VARCHAR(30))
    photo_href_2 = sq.Column(sq.VARCHAR(30))
    photo_href_3 = sq.Column(sq.VARCHAR(50))

    __table_args__ = (sq.UniqueConstraint('user_id', 'vk_profile_href'),)

    def __str__(self):
        return f"favorite_profiles: id: {self.id}, user_id: {self.user_id}, vk_profile_href: {self.vk_profile_href}, "\
               f"first_name: {self.first_name}, last_name: {self.last_name}, photo_href_1: {self.photo_href_1},"\
               f"photo_href_2: {self.photo_href_2}, photo_href_3: {self.photo_href_3}"


class BlockedProfiles(Base):

    __tablename__ = 'blocked_profiles'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, nullable=False)
    vk_profile_href = sq.Column(sq.VARCHAR(50), nullable=False)

    __table_args__ = (sq.UniqueConstraint('user_id', 'vk_profile_href'),)

    def __str__(self):
        return f"blocked_profiles: id: {self.id}, user_id: {self.user_id}, vk_profile_href: {self.vk_profile_href}"


def create_tables():

    """ Метод создает таблицы в БД используя модели описанные в этом модуле. """

    from db_func import create_engine

    engine = create_engine()

    Base.metadata.create_all(engine)


def delete_tables():

    """ Метод удаляет все таблицы из БД созданные из этого модуля. """

    from db_func import create_engine

    engine = create_engine()

    Base.metadata.drop_all(engine)


if __name__ == "__main__":

    delete_tables()

    create_tables()