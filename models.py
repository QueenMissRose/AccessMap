from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

db_url = "sqlite:///database.db"
engine = create_engine(db_url)

base = declarative_base()



class Locations(base):
    __tablename__ = "ratings"
    LocationID = Column('LocationID', Integer, primary_key=True)
    Name = Column('Name', String)
    Address = Column('Address', String)
    SensoryRating = Column('SensoryRating', Integer)
    MobilityRating = Column('MobilityRating', Integer)
    ServiceDogRelief = Column('ServiceDogRelief', Integer)
    WheelchairAccessible = Column('WheelchairAccessible', Integer)
    CommonAllergenRisk = Column('CommonAllergenRisk', Integer)


base.metadata.create_all(engine)