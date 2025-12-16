from fastapi import FastAPI
from sqladmin import Admin, ModelView
from app.database import engine, Base
from app.routers import users
from app.models import Product

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Assignment")

# Include routers
app.include_router(users.router)

# Admin setup
admin = Admin(app, engine)

# Admin view for Product model
class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.name, Product.price, Product.stock]
    name = "Product"
    name_plural = "Products"
    icon = "fa-solid fa-box"

admin.add_view(ProductAdmin)

@app.get("/hello")
def hello():
    return {"message": "Hello FastAPI!"}

@app.get("/")
def root():
    return {
        "message": "Welcome to FastAPI Assignment",
        "endpoints": {
            "hello": "/hello",
            "create_user": "/users (POST)",
            "get_users": "/users (GET)",
            "admin_dashboard": "/admin"
        }
    }