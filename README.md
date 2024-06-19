## main

### data/
Contains scripts for loading and preprocessing your dataset(s).

### notebooks/
Holds Jupyter notebooks for exploratory data analysis (EDA) and various experiments.

### features/
Includes scripts dedicated to feature engineering, transforming raw data into features suitable for model training.

### models/
This directory contains scripts for model training and evaluation.
- **static/**: Subdirectory to store serialized models and model parameters, typically in .pkl format.

### reports/
Stores generated reports in various formats (HTML, PDF, LaTeX, etc.).
- **figures/**: Subdirectory for storing generated graphics and figures to be included in reports.

### requirements.txt
Lists all the dependencies required to run the project.

### README.md
Provides an overview of the project, setup instructions, and other relevant information.

### app.py
A Flask application file to serve your machine learning model as an API.

### result.py
Script to collect and format the results to be sent via the Flask API.
