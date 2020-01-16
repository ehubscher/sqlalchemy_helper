import logging
from contextlib import contextmanager
from sqlalchemy import event
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import SQLAlchemyError

"""
Implements session handling functionality for the SQLAlchemy ORM
solution provided for the CLI application.
"""


@contextmanager
def scoped_session_transaction(session: Session):
    """
    This function provides a transactional scope around a series of operations.
    """

    try:
        yield session
        session.commit()
    except SQLAlchemyError as e:
        logging.error(e)
        session.rollback()
    finally:
        session.close()


def strong_reference_session(session: Session):
    @event.listens_for(session, 'transient_to_pending')
    @event.listens_for(session, 'pending_to_persistent')
    @event.listens_for(session, 'deleted_to_persistent')
    @event.listens_for(session, 'detached_to_persistent')
    @event.listens_for(session, 'loaded_as_persistent')
    def strong_ref_object(sess, instance):
        if 'refs' not in sess.info:
            sess.info['refs'] = refs = set()
        else:
            refs = sess.info['refs']

        refs.add(instance)

    @event.listens_for(session, 'persistent_to_detached')
    @event.listens_for(session, 'persistent_to_deleted')
    @event.listens_for(session, 'persistent_to_transient')
    def deref_object(sess, instance):
        sess.info['refs'].discard(instance)
