import json

from app import app

post_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


# тесты для всех постов
def test_all_posts_are_list():
    """Тест типа файла с данными всех постов"""
    with app.test_client() as client:
        res = client.get('/api/posts/')
        assert res.status_code == 200
        data = json.loads(res.get_data(as_text=True))
        assert len(data) > 0, "Пустой список"
        assert type(data) == list, "Неправильный тип файла, должен быть list"


def test_all_posts_have_keys():
    """Тест ключей списка всех постов"""
    with app.test_client() as client:
        res = client.get('/api/posts/')
        list_of_posts = res.get_json()

    for post in list_of_posts:
        one_post_keys = set(post.keys())
        assert one_post_keys == post_keys, "Неправильный ключ у полученного словаря"


# тесты для одного поста
def test_post_is_dict():
    """Тест типа файла с данными одного поста"""
    with app.test_client() as client:
        res = client.get('/api/posts/1')
        assert res.status_code == 200
        data = json.loads(res.get_data(as_text=True))
        assert len(data) > 0, "Пустой список"
        assert type(data) == dict, "Неправильный тип файла, должен быть dict"


def test_post_has_keys():
    """Тест ключей одного поста"""
    with app.test_client() as client:
        res = client.get('/api/posts/1')
        post = res.get_json()
        single_post_keys = set(post.keys())
        assert single_post_keys == post_keys, "Неправильный ключ у полученного словаря одного поста"
