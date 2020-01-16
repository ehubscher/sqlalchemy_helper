from sqlalchemy import Column, create_engine, Integer,  MetaData
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import mapper, scoped_session, sessionmaker

"""
Implements the SQLAlchemy object-relational schema for Telenav and Garmin POI
category data as well as the SINFO data.
"""


def example_init_db(db_url: str) -> scoped_session:
    """
    Implements the SQLAlchemy object-relational schema for a db.

    :param db_url: URL to desired database.
    :return: The relevant SQLAlchemy scoped_session.
    """

    # Import all modules here that might define models so that they will be
    # registered properly on the metadata. Otherwise, you will have to
    # import them first before calling init_*_db().

    from sqlalchemy_helper.models import ExampleClass

    engine: Engine = create_engine(db_url, echo=True)

    db_session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db_session = scoped_session(session_factory=db_session_factory)

    metadata = MetaData(bind=engine)

    ExampleClass.query = db_session.query_property()
    mapper(class_=ExampleClass, local_table=ExampleClass.make_table(metadata))

    metadata.create_all()

    return db_session
