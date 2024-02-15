from flask import Flask

from src.modules.tag.http.routes.tags_routes import tags_bp

# Create a flask instance
app = Flask(__name__)

# Register all routers
app.register_blueprint(tags_bp)
