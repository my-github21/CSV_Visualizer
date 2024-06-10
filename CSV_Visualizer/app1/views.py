from django.shortcuts import render
from tablib import Dataset
from app1.models import *
from django.shortcuts import render, get_object_or_404
import pandas as pd
import numpy as np
import os
from django.conf import settings
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import seaborn as sns

def upload(request):
    context = {}
    if 'myfile' in request.FILES:
        dataset = Dataset()
        file = request.FILES['myfile']
        
        # If you want to save the file then just uncomment this code and set the media path of your system directory in path2 variable
        
        # data=Data(file=file)
        # data.save()  
        # print('rrr',file,str(file))     

        # path2 = r'D:\ZappKode\MachineTest\CSV_Visualizer\media\csv_files\\' + str(file)
        df2 = pd.read_csv(file)
        print(df2.isna().sum())
        
        context = {
                'df2': df2.head(10).to_html(),
                'df2_describe':df2.describe().to_html(),
                'df2_missing': pd.DataFrame(df2.isna().sum()).rename(columns={0:'no of missing'}).to_html()
        }
        
        histograms = []
        numerical_columns = df2.select_dtypes(include=['number']).columns

        for column in numerical_columns:
            plt.figure()
            sns.histplot(df2[column].dropna(), kde=True)
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')

            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            image_base64 = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()
            plt.close()

            histograms.append(image_base64)

        context['histograms'] = histograms

        return render(request, 'upload.html', context)

    return render(request,'upload.html',context)


# def file_list(request):
#     files = Data.objects.all()
#     return render(request, 'file_list.html', {'files': files})

# def file_detail(request, pk):
#     file = get_object_or_404(Data, pk=pk)
#     return render(request, 'file_detail.html', {'file': file})

# path='media/csv_files'

