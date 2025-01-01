import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()
DB_PASSWORD = os.getenv('DB_PASSWORD')
print(DB_PASSWORD)

engine = create_engine(f'postgresql://postgres:{DB_PASSWORD}@localhost/pizza_delivery', echo=True)

Base = declarative_base()
Session = sessionmaker()
