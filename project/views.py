from flask import Blueprint, render_template, request, jsonify
import pandas as pd

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')


@views.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@views.route('/api/data')
def get_csv_data():
    data = pd.read_csv('project/data/hirc_pm_report_cleaned.csv')
    if len(data) == 0:
        return jsonify([])
    data = data.where(pd.notnull(data), None)
    return jsonify(data.to_dict(orient='records'))

