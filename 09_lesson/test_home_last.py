import pytest
from test_new_1 import Student

def test_create_student(db_session):
    """Тест на добавление студента."""
    student = Student(name="Иван Иванов")
    db_session.add(student)
    db_session.flush()  # Получаем id без коммита

    assert student.id is not None, "ID не присвоен"
    assert student.name == "Иван Иванов", "Имя не сохранено"

def test_update_student(db_session):
    """Тест на изменение данных студента."""
    student = Student(name="Петр Петров")
    db_session.add(student)
    db_session.flush()

    # Изменяем имя
    student.name = "Петр Петров (обновлено)"
    db_session.commit()  # Коммитим изменения

    # Проверяем, что изменения сохранились
    updated = db_session.query(Student).get(student.id)
    assert updated.name == "Петр Петров (обновлено)", "Имя не обновлено"

def test_delete_student(db_session):
    """Тест на удаление студента."""
    student = Student(name="Анна Смирнова")
    db_session.add(student)
    db_session.flush()

    db_session.delete(student)
    db_session.commit()

    deleted = db_session.query(Student).get(student.id)
    assert deleted is None, "Студент не удалён из БД"