from flask import Flask 
from flask_migrate import Migrate
from models import db
from flask_restful import Api
from Resources.pizzas import ResourcePizza
from Resources.resturant_pizza import ResourceRestaurantPizza

from Resources.resturant import ResourceResturant # ,ResourceResturantById

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

migrations = Migrate(app , db)
db.init_app(app)

api.add_resource(ResourceResturant, '/resturants/<int:id>')
api.add_resource(ResourcePizza , '/pizzas')
api.add_resource(ResourceRestaurantPizza, '/restaurant_pizzas')
#  api.add_resource(ResourceResturantById ,'/resturants/<int:id>')

if __name__ == '__main__':
    app.run(port=5000 , debug=True)