import json
import logging
logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="utf8")
def load_json(file_name):
    """Загружает посты из файла в список."""
    """Если файл не найден или в неподходящем формате, происходит логирование ошибки и
    возвращается пустой список"""
    try:

        with open(file_name,  encoding='UTF-8') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f'ошибка при загрузке файла: {e}')
        return []

"""Добавьте список постов в файл posts.json"""
def posts_json(search_key, file_name):
    posts = load_json(file_name)
    found_posts = []
    for post in posts:
        if search_key in post['content']:
            found_posts.append(post)
    return found_posts

def save_json(file_name, post):
    posts = load_json(file_name)
    posts.append(post)
    save_file(file_name, posts)

"""Запись в файл"""
def save_file(file_name, post):
    with open(file_name,'w' ,encoding='UTF-8') as file:
        json.dump(post, file)