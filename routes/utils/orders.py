from models.order import Order
from models.user import User
from sqlalchemy import or_
from routes.utils.auth import auth_info

def get_orders_query(query):
    user = auth_info()
    if user.get("role") == "user":
        query = query.filter(Order.user_id == user.get("id"))
    return query    
    
def get_orders_query_admin(query, q):
    user = auth_info()
    if user.get("role") == "admin":
        if q:
            query = query.filter(or_(User.name.ilike(f"%{q}%") , User.email.ilike(f"%{q}%")))    
    return query    