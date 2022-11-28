from flask import Blueprint, render_template, request
from constants import JSON
from functions import posts_json
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="utf8")

"""Начните работу над блюпринтом main, создайте, импортируйте, зарегистрируйте его"""
main_blueprint = Blueprint('main_blueprint', __name__)

"""Реализуйте вывод формы на главной странице при обращении к `/' """
"""Используйте шаблон `index.html`"""

@main_blueprint.route("/")
def page_main():
    return render_template('index.html')

"""Реализуйте поиск и вывод постов при обращении на `/search/?s=<ключ поиска>` """
"""Используйте шаблон `post_list.html`"""

@main_blueprint.route("/search/")
def search():
    page_search = request.args.get('s') #request.args возвращает вам объект "словарь".
    logging.info(f"Выполняется поиск по слову {page_search}")
    found_posts = posts_json(page_search, JSON)
    return render_template('post_list.html', posts=found_posts, key_search=page_search)

#получить ( ключ, по умолчанию = нет, тип = нет )


