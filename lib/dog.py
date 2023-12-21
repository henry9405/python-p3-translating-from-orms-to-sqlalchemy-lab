from models import Dog

def create_table(base):
    Dog.__table__.create(bind=base.engine, checkfirst=True)

def save(session, dog):
    try:
        session.add(dog)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

def find_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).all()

def find_by_id(session, dog_id):
    return session.query(Dog).filter_by(id=dog_id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).all()

def delete(session, dog):
    try:
        session.delete(dog)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


