from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://goo.gl/mu5x9p')
session.add(User1)
session.commit()

# RESTAURANT BEING CREATED

restaurant1 = Restaurant(user_id=1, name="Urban Burger")

# Menu for UrbanBurger

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Veggie Burger",
                     description="Veggie patty with tomato mayo and lettuce",
                     price="$7.50", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1, name="French Fries",
                     description="with garlic and parmesan",
                     price="$2.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Chicken Burger",
                     description="Chicken patty with tomato mayo and lettuce",
                     price="$5.50", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

# RESTAURANT BEING CREATED

restaurant2 = Restaurant(user_id=1, name="Super Stir Fry")

session.add(restaurant2)
session.commit()

# Menu items for Super Stir Fry

menuItem4 = MenuItem(user_id=1, name="Chicken Stir Fry",
                     description="Choice of noodles, vegetables and sauces",
                     price="$7.99", course="Entree", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Peking Duck",
                     description=" A famous duck dish from Beijing.",
                     price="$25", course="Entree", restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Spicy Tuna Roll",
                     description="Seared rare ahi, avocado, edamame, cucumber",
                     price="15", course="Entree", restaurant=restaurant2)

session.add(menuItem6)
session.commit()


# RESTAURANT BEING CREATED

restaurant3 = Restaurant(user_id=1, name="Asian Studio")

session.add(restaurant3)
session.commit()

# Menu Items for Asian Studio

menuItem7 = MenuItem(user_id=1, name="Pho",
                     description="Vietnamese noodle soup consisting of broth.",
                     price="$8.99", course="Entree", restaurant=restaurant3)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Chinese Dumplings",
                     description="a common Chinese dumpling.",
                     price="$6.99", course="Appetizer", restaurant=restaurant3)

session.add(menuItem8)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Gyoza",
                     description="light seasoning of Japanese gyoza",
                     price="$9.95", course="Entree", restaurant=restaurant3)

session.add(menuItem9)
session.commit()


print "added menu items!"
