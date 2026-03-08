from conftest import Student

# 1. Тест на добавление
def test_add_student(db_session):
    new_student = Student(name="Elena", subject="Math")
    db_session.add(new_student)
    db_session.commit()

    student = db_session.query(Student).filter_by(name="Elena").first()
    assert student is not None
    assert student.subject == "Math"

# 2. Тест на изменение
def test_update_student(db_session):
    # Сначала создаем
    student = Student(name="Oleg", subject="History")
    db_session.add(student)
    db_session.commit()

    # Меняем предмет
    student.subject = "Physics"
    db_session.commit()

    updated_student = db_session.query(Student).filter_by(name="Oleg").first()
    assert updated_student.subject == "Physics"

# 3. Тест на удаление
def test_delete_student(db_session):
    # Сначала создаем
    student = Student(name="Dmitry", subject="Art")
    db_session.add(student)
    db_session.commit()

    # Удаляем
    db_session.delete(student)
    db_session.commit()

    result = db_session.query(Student).filter_by(name="Dmitry").first()
    assert result is None
