import pandas as pd
from django.shortcuts import render
from .models import ImportedCSV

def home(request):
    columns = []  # Initialize an empty list for columns

    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')

        if not csv_file or not csv_file.name.endswith('.csv'):
            return render(request, 'csv_importer/home.html', {'error_message': 'Please upload a valid CSV file.'})

        try:
            df = pd.read_csv(csv_file)
            columns = df.columns.tolist()
        except pd.errors.ParserError:
            return render(request, 'csv_importer/home.html', {'error_message': 'Error parsing the CSV file.'})

    return render(request, 'csv_importer/home.html', {'columns': columns})
