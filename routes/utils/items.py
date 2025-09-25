from models.order import Order 
from models.user import User
from models.db import db
from routes.utils.auth import auth_info

def is_authorized(order_id):
    order = db.get_or_404(Order, order_id)
    user = auth_info()
    return user.get("role") == "admin" or order.user_id == user.get("id")