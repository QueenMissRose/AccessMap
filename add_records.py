from sqlalchemy.orm import sessionmaker
from models import Locations, engine


def add_new_rating_to_db(new_record):
    Session = sessionmaker(bind=engine)
    session = Session()

    # new_record = Locations(Name=location_name, Address=address, SensoryRating=sensory_rating,
    #                     MobilityRating=mobility_rating,
    #                     ServiceDogRelief=service_dog_relief_rating, WheelchairAccessible=wheelchair_rating,
    #                     CommonAllergenRisk=common_allergens_rating)
    session.add(new_record)
    session.commit()
