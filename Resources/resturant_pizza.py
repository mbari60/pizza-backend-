from flask_restful import Resource, reqparse, fields, marshal_with
from models import RestaurantPizza, Pizza, Restaurant , db

class ResourceRestaurantPizza(Resource):
    restaurant_pizza_parser = reqparse.RequestParser()
    restaurant_pizza_parser.add_argument('price', type=float, required=True, help='Price is required')
    restaurant_pizza_parser.add_argument('pizza_id', type=int, required=True, help='Pizza ID is required')
    restaurant_pizza_parser.add_argument('restaurant_id', type=int, required=True, help='Restaurant ID is required')

    pizza_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "ingredients": fields.String
    }

    @marshal_with(pizza_fields)
    def post(self):
        args = self.restaurant_pizza_parser.parse_args()

        pizza_id = args['pizza_id']
        restaurant_id = args['restaurant_id']

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not pizza or not restaurant:
            return {"messages": "Invalid pizza_id or restaurant_id"}, 400

        new_restaurant_pizza = RestaurantPizza(
            price=args['price'],
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )

        try:
            db.session.add(new_restaurant_pizza)
            db.session.commit()
            return pizza, 201 
        except:
            return {"message": "Validation errors"}, 400
        
# dont forget to validate the price to be between 1 and 30