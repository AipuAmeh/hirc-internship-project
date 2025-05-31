from flask import Blueprint, render_template, request, jsonify
import pandas as pd
from pandasql import sqldf
from project.chart_classes import Charts

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')


@views.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@views.route('/api/data')
def get_csv_data():
    chart_type = request.args.get("chart_type", "pm_vs_category")
    data = pd.read_csv('project/data/hirc_pm_report_cleaned.csv')

    if len(data) == 0:
        return jsonify([])
    
    data = data.where(pd.notnull(data), None)

    if chart_type == 'pm_vs_category':
        query = Charts().bar_chart_query()
    else:
        print('no chart specified')
        return jsonify({'error': 'Invalid chart_type specified'}), 400
    chart_data = sqldf(query, locals())
    return jsonify(chart_data.to_dict(orient='records'))

