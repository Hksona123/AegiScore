
import os
import sys
# Add Server to path
sys.path.append(os.path.join(os.getcwd(), 'Server'))

from app.main import create_app
from app.models.db import db, User

app = create_app()
with app.app_context():
    admin = User.query.filter_by(username='admin').first()
    if admin:
        print("Resetting admin password...")
        admin.set_password('AegisCore@2025!')
        db.session.commit()
        print("Done.")
    else:
        print("Admin user not found.")
