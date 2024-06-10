# CSV_Visualizer
A Django-based web application for uploading CSV files and visualizing the data. The application provides a user-friendly interface to upload CSV files and displays various insights including the first 10 rows of the data, a descriptive summary, missing value counts, and histograms for numerical columns.

## Features
- Upload CSV files through a web interface.
- Display the first 10 rows of the uploaded CSV file.
- Show descriptive statistics of the data.
- Display the number of missing values for each column.
- Generate histograms for numerical columns.

## Technologies Used
- Django
- Pandas
- Matplotlib
- Seaborn
- Bootstrap (for front-end styling)

## Installation
### 1. Clone the repository:
```
git clone https://github.com/yourusername/csv-visualizer.git
cd csv-visualizer
```
### 3. Install the required packages:
```
pip install matplotlib tablib pandas seaborn  numpy base64
 
```
### Run the development server:
```
python manage.py runserver

```
### Open your web browser and go to:
```
http://127.0.0.1:8000/
```
## Usage
1. Upload CSV File:

  - Navigate to the upload page.
  - Select a CSV file from your local machine and click the upload button.
    
2. View Data:

  - After uploading, the application will display:
  - The first 10 rows of the data.
  - Descriptive statistics of the data.
  - The count of missing values for each column.
  - Histograms for numerical columns.
## Project Structure
```
csv-visualizer/
├── app1/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
|
├── templates/
    └── upload.html
├── csv_visualizer/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── media/
│   └── csv_files/
├── manage.py
├── requirements.txt
└── README.md

```
## Code Explanation
### views.py
Contains the main logic for handling file uploads and data visualization.

- upload: Handles file upload, reads the CSV file using Pandas, and prepares the data for display including generating histograms for numerical columns.

### upload.html
- The main HTML template for the upload page, utilizing Bootstrap for styling and responsive design.

### settings.py
Configuration for the Django project, including settings for media files.

## Dependencies
- Django
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Tablib

## Contributing
- Fork the repository
- Create your feature branch (git checkout -b feature/AmazingFeature)
- Commit your changes (git commit -m 'Add some AmazingFeature')
- Push to the branch (git push origin feature/AmazingFeature)
- Open a Pull Request
  
## Acknowledgements
Inspired by various data visualization tools and projects.
Thanks to the contributors and the community for their support.
