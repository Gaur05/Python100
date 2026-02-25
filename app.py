import logging
import os
from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename='app_error_log.txt',  # all errors will be logged here
    level=logging.ERROR,           # log only errors
    format='[%(asctime)s] %(levelname)s: %(message)s'
)

# Updated: specify custom template folder if needed
app = Flask(
    __name__,
    template_folder="/Users/akshatgaur/Desktop/Akshat/Asset Management/templates"
)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_username:your_password@localhost/asset_mgmt_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://asset_management:qwer1234@localhost/Asset_Management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model
class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))
    purchase_date = db.Column(db.Date)
    cost = db.Column(db.Numeric)
    owner = db.Column(db.String(50))
    status = db.Column(db.String(20), default='Available')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        logging.error(f"Error creating tables: {e}")

# Routes
@app.route('/')
def index():
    try:
        assets = Asset.query.all()
        # Removed absolute path; just use template filename
        return render_template('index.html', assets=assets)
    except Exception as e:
        logging.error(f"Error in index route: {e}")
        return "Something went wrong. Check log file."

@app.route('/add', methods=['POST'])
def add_asset():
    try:
        data = request.form
        asset = Asset(
            name=data['name'],
            type=data['type'],
            purchase_date=data['purchase_date'],
            cost=data['cost'],
            owner=data['owner'],
            status=data.get('status', 'Available')
        )
        db.session.add(asset)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        logging.error(f"Error in add_asset route: {e}")
        return "Something went wrong. Check log file."

@app.route('/delete/<int:id>')
def delete_asset(id):
    try:
        asset = Asset.query.get(id)
        if asset:
            db.session.delete(asset)
            db.session.commit()
        return redirect('/')
    except Exception as e:
        logging.error(f"Error in delete_asset route: {e}")
        return "Something went wrong. Check log file."

@app.route('/update/<int:id>', methods=['POST'])
def update_asset(id):
    try:
        asset = Asset.query.get(id)
        if asset:
            data = request.form
            asset.name = data['name']
            asset.type = data['type']
            asset.purchase_date = data['purchase_date']
            asset.cost = data['cost']
            asset.owner = data['owner']
            asset.status = data.get('status', asset.status)
            db.session.commit()
        return redirect('/')
    except Exception as e:
        logging.error(f"Error in update_asset route: {e}")
        return "Something went wrong. Check log file."

# Run the app with logging
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        logging.error(f"Flask app failed to start: {e}")

        