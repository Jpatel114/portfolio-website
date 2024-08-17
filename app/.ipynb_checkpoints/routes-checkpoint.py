# app/routes.py
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/projects')
def projects():
    projects = {
        'group_projects': [
            {
                'title': 'Profit Prediction for Fortune 500 Companies',
                'date': 'February 2024 - April 2024',
                'description': 'Our project aims to provide precise predictive analysis tailored to Fortune 500 companies in the United States for 2024 based on the data from 2019 to 2023. We aim to predict the profit using financial data such as stock price, revenue, industry, sector, etc. With our analysis, we aim to help investors make informed decisions and allow companies to allocate resources efficiently to optimize profit. Also, these predictions play a big role in navigating the risks of an unpredictable market and economic crisis. This is important to all of us as these predictions affect employment, the economy, and our cost of living. Increased spending is correlated with a larger employment market and more opportunities. These companies are of great interest to investors, which makes precise prediction crucial.',
                'link': 'https://github.com/ppate460/Profit_Prediction_Fortune500_Companies'
            },
            # Add more group projects here
        ],
        'class_projects': [
            {
                'title': 'Iterative Dichotomiser 3 (ID3)',
                'date': 'September 2023',
                'description': 'This project involves implementing the ID3 decision tree algorithm for classification tasks. It includes reading data from CSV files, manipulating and exploring the data using pandas, and building the decision tree in a top-down manner by selecting the best attributes to split based on information gain. The project provides functions for calculating entropy, selecting attributes, and recursively constructing the decision tree. Additionally, it evaluates the performance of the built model on training, validation, and test datasets, and calculates the accuracy of the decision tree model.',
                'link': 'https://github.com/Jpatel114/CS-412-Intro-to-Machine-Learning/blob/main/Janki_patel_id3.ipynb'
            },
            {
                'title': 'Bias Variance',
                'date': 'October 2023',
                'description': 'This project involves implementing the ID3 decision tree algorithm for classification tasks. It includes reading data from CSV files, manipulating and exploring the data using pandas, and building the decision tree in a top-down manner by selecting the best attributes to split based on information gain. The project provides functions for calculating entropy, selecting attributes, and recursively constructing the decision tree. Additionally, it evaluates the performance of the built model on training, validation, and test datasets, and calculates the accuracy of the decision tree model.',
                'link': 'https://github.com/Jpatel114/CS-412-Intro-to-Machine-Learning/blob/main/Janki_patel_id3.ipynb'
            },
            # Add more class projects here
        ],
        'personal_projects': [
            # Add personal/practice projects here
        ]
    }
    return render_template('projects.html', projects=projects)

@main.route('/in_progress')
def in_progress():
    return render_template('in_progress.html')
