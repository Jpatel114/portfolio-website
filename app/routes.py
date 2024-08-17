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
                'title': 'CTA Transit',
                'date': 'February 2023',
                'description': 'I developed a console-based Python program that interacts with a CTA2 daily ridership database, utilizing SQL queries to retrieve and compute data. The program calculates and displays various statistics, including general ridership stats and percentages, and presents these findings in both text and visual formats. I employed the matplotlib library to create a graphical representation of rider trends over time, enhancing the analysis with clear visual insights.',
                'link': 'https://github.com/Jpatel114/Homework-01'
            },
            {
                'title': 'Iterative Dichotomiser 3 (ID3)',
                'date': 'September 2023',
                'description': 'This project involves implementing the ID3 decision tree algorithm for classification tasks. It includes reading data from CSV files, manipulating and exploring the data using pandas, and building the decision tree in a top-down manner by selecting the best attributes to split based on information gain. The project provides functions for calculating entropy, selecting attributes, and recursively constructing the decision tree. Additionally, it evaluates the performance of the built model on training, validation, and test datasets, and calculates the accuracy of the decision tree model.',
                'link': 'https://github.com/Jpatel114/CS-412-Intro-to-Machine-Learning/blob/main/Janki_patel_id3.ipynb'
            },
            {
                'title': 'Bias Variance',
                'date': 'October 2023',
                'description': 'This project explores the concepts of bias and variance in machine learning models. It includes implementation and evaluation of different models to understand how bias and variance affect model performance. The project demonstrates techniques to balance bias and variance for better predictive accuracy.',
                'link': 'https://github.com/Jpatel114/CS-412-Intro-to-Machine-Learning/blob/main/Janki_patel_id3.ipynb'
            },
            # Add more class projects here
        ],
        'personal_projects': [
            {
                'title': 'Market News',
                'date': 'June 2024',
                'description': 'I developed a news application that fetches live stock news using the Finhub API, providing real-time updates on top stocks. The app allows users to view news by company symbol, filter by specific dates or years, and presents the information in both JSON and HTML formats. Although the app was not deployed publicly, the code is available in the news app for review and use.',
                'link': 'https://github.com/Jpatel114/Market-News'
            },
            # Add more personal/practice projects here
        ]
    }
    return render_template('projects.html', projects=projects)

@main.route('/in_progress')
def in_progress():
    in_progress_projects = [
        {
            'title': 'Retail Store Sales Analyzing',
            'date': 'August 2024 - Ongoing',
            'description': 'This project focuses on analyzing predicted sales using machine learning models. It involves using a dataset to predict sales and developing an interactive dashboard using Python and Tableau. The goal is to provide insights into sales trends and help in making data-driven decisions for retail stores. The link to the project will be provided once it is completed.',
            'link': 'Link will be provided when the project is done'
        },
        {
            'title': 'Serious Crime Analyzing',
            'date': 'August 2024 - Ongoing',
            'description': 'This project involves exploring and analyzing global crime data, specifically focusing on rape and murder cases. The analysis utilizes data from sources such as UNODC, WHO, and national crime databases to provide insights into prevalence, trends, and regional disparities. Python libraries like Pandas, NumPy, Matplotlib, and Seaborn will be used for data cleaning, analysis, and visualization. The findings will be presented through interactive dashboards and detailed reports to inform policy and public awareness.',
            'link': 'Link will be provided when the project is done'
        }
    ]
    return render_template('in_progress.html', projects=in_progress_projects)
