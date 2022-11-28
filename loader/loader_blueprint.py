from flask import Blueprint, render_template, request
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="utf8")
"""Продолжите работу в блупринте loader, создайте, импортируйте, зарегистрируйте его."""
loader_blueprint = Blueprint('loader_blueprint', __name__)

"""Реализуйте страничку "добавить пост" при обращении к GET /post"""
@loader_blueprint.route('/post/')
def add_post():
    return render_template('post_form.html')

"""Обработайте запрос при обращении к POST /post"""
@loader_blueprint.route('/post/', methods=['POST'])
def save_data():
    content = request.form.get('content')
    file_object = request.files.get('picture')
    """Если не была отправлена, выведите сообщение "ошибка загрузки" без шаблона"""
    if not content or not file_object:
        return 'Ошибка  загрузки'

    file_name = file_object.filename
    file_type = file_name.split('.')[-1]
    if file_name not in ['png',  'jpeg']:
        logging.info(f"Загруженный файл {file_name} не картинка")
        return "Это не изображение"
    """Положите загруженный файл в папку uploads"""
    file_object.save(f'uploads/images/{file_name}')
    save_content = {'pic': f'/uploads/{file_name}',
                    'content': content}
    return render_template('post_uploaded.html', save_post=save_content)