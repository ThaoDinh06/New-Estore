from django.shortcuts import render, HttpResponse
from datetime import datetime
from store.models import Product
from django.db.models import Count
from django.template.loader import render_to_string
import pdfkit
import os


# Create your views here.
def html_to_pdf(request):
    today = datetime.now()
    d = today.strftime("%d-%m-%Y")
    product_list = Product.objects.values('subcategory', 'subcategory__name') \
        .annotate(total=Count('subcategory')) \
        .order_by('subcategory')
    html_string = render_to_string('storereport/report.html', {
        'product_list': product_list,
        'day': d,
    })

    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    filename = 'report_' + today.strftime('%Y%m%d%H%M%S') + '.pdf'
    pdfkit.from_string(html_string, os.path.join(
        os.path.expanduser('~'), 'Documents', filename), configuration=config)
    html = '<div class="text-center">' + html_string + \
           '<h5>Thống kê đã được lưu vào tập tin ' + filename + \
           ' trong thư mục Documents.</h5></div>'
    return HttpResponse(html)
