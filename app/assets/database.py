# coding: utf-8
import datetime
import os

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')
engine = create_engine('sqlite:///' + databese_file, convert_unicode=True, echo=False)
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from . import models  # 外すとエラーになる？
    Base.metadata.create_all(bind=engine)


def insert_from_csv(csv_path='assets/data.csv'):
    from .models import Data
    df = pd.read_csv(csv_path)
    to_date = (lambda x: datetime.datetime.strptime(x, '%Y/%m/%d').date())
    db_session.add_all(
        [Data(date=to_date(row.date), subscribers=row.subscribers, reviews=row.reviews) for i, row in df.iterrows()])
    db_session.commit()
