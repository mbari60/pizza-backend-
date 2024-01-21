from models import Pizza
from flask_restful import Resource , fields ,marshal_with


class ResourcePizza(Resource):

    response_fields = {
    "id":fields.Integer ,
    "name": fields.String,
    "ingredients": fields.String
  }
    
    @marshal_with(response_fields)
    def get(self):
        pizzas = Pizza.query.all()
        if pizzas:
            return pizzas
        else:
            return {"message":"pizzas not found"}