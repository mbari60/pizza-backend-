from flask_restful import Resource, fields, marshal_with
from models import  Restaurant,db

class ResourceResturant(Resource):

   response_fields ={
      "id":fields.Integer,
      "name":fields.String,
      "address":fields.String
   }

   @marshal_with(response_fields)
   def get(self , id = None):
      if id:
         resturant = Restaurant.query.get(id)
         if resturant:
            return resturant 
         else:
            return {"error": "Restaurant not found"}, 404
      
      else:
         resturants = Restaurant.query.all()
         return resturants
    
   def delete(self , id):
      restaurant_to_be_deleted = Restaurant.query.get(id)
      if restaurant_to_be_deleted:
         try:
            db.session.delete(restaurant_to_be_deleted)
            db.session.commit()
            return {"message":f"Resturant of id={id} deleted succesfully", "status":"success"}, 200
         except:
            return {"message":f"failled to delete resturant of id={id}"}
         
      else: 
         return {"message":"resturant not found"}

      