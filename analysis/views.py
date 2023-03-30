from django.shortcuts import render
from EStore import settings
import pandas as pd
import os.path
from analysis.utils import *


# Create your views here.
def work_with_chart(request):
    # Histogram
    data_seconds = pd.read_excel(os.path.join(settings.MEDIA_ROOT, 'analysis/dataset.xlsx'), sheet_name='Wait_times')
    hist = get_hist(data_seconds, 'seconds', 'Customer Wait Time')

    return render(request, 'analysis/work_with_chart.html', {
        'hist': hist,
    })
