# SQLite database create
from app import app, db
app.app_context().push()
db.create_all()
exit()
