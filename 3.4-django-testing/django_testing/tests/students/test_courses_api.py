from rest_framework.test import APIClient
import pytest
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


# проверка получения 1го курса (retrieve-логика)
@pytest.mark.django_db
def test_create_course(client, courses_factory):
    # создаем курс через фабрику
    course = courses_factory()
    count = Course.objects.count()
    # строим урл и делаем запрос через тестовый клиент
    response = client.get(f'/api/v1/courses/{count}/')
    assert response.status_code == 200
    data = response.json()
    # проверяем, что вернулся именно тот курс, который запрашивали
    assert data['name'] == course.name


# проверка получения списка курсов (list-логика)
@pytest.mark.django_db
def test_get_courses(client, courses_factory):
    # аналогично – сначала вызываем фабрики, затем делаем запрос и проверяем результат
    # Arrange
    courses = courses_factory(_quantity=10)
    # Act
    response = client.get('/api/v1/courses/')
    # Assert
    data = response.json()
    # Все тесты должны явно проверять код возврата.
    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


# проверка фильтрации списка курсов по id
# создаем курсы через фабрику, передать id одного курса в фильтр, проверить результат запроса с фильтром
@pytest.mark.django_db
def test_filter_id(client, courses_factory):
    courses = courses_factory(_quantity=10)
    c = 5
    response = client.get(f'/api/v1/courses/?id={c}')
    data = response.json()
    # Все тесты должны явно проверять код возврата.
    assert response.status_code == 200
    assert data[0]['name'] == courses[c - 1].name


# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_filter_id(client, courses_factory):
    course = courses_factory()
    response = client.get(f'/api/v1/courses/?name={course.name}')
    data = response.json()
    # Все тесты должны явно проверять код возврата.
    assert response.status_code == 200
    assert data[0]['name'] == course.name


# тест успешного создания курса
# здесь фабрика не нужна, готовим JSON-данные и создаем курс
@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()

    response = client.post('/courses/', data={'user': user.id, 'text': 'test text'})

    assert response.status_code == 201
    assert Message.objects.count() == count + 1

# тест успешного обновления курса
# сначала через фабрику создаем, потом обновляем JSON-данными

# тест успешного удаления курса
