from src.conf.database import session
from src.models import User, FileLinks


def get_links(user: User):
    """ Выборка ссылок переданного пользователя """

    file_links = session.query(FileLinks).filter(FileLinks.user_id == user.id)
    return file_links


def create_link(user: User, link: str):
    """ Создание ссылки для переданного пользователя """

    new_link = FileLinks(user_id=user.id, link=link)

    session.add(new_link)
    session.commit()

    return new_link


def delete_link(user: User, link_id: int):
    """ Удаление ссылки у переданного пользователя """

    session.query(FileLinks).filter(
        (FileLinks.id == link_id) & (FileLinks.user_id == user.id)
    ).delete()

    session.commit()
