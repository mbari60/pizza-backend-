from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address=db.Column(db.String, nullable=False)
    pizzas =  db.relationship("Pizza", secondary="restaurant_pizza", backref="restaurants")

class Pizza(db.Model):
    __tablename__ = "pizzas"

    id =  db.Column( db.Integer, primary_key=True)
    name =  db.Column( db.String, nullable=False)
    ingridients = db.Column(db.String, nullable=False)
    restaurants =  db.relationship("Restaurant", secondary="restaurant_pizza", backref="pizzas")

class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizza"
    
    price = db.Column(db.String, nullable = False)
    restaurant_id =  db.Column( db.Integer,  db.ForeignKey("restaurants.id"), primary_key=True)
    pizza_id =  db.Column( db.Integer,  db.ForeignKey("pizzas.id"), primary_key=True)