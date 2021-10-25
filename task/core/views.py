from django.shortcuts import render
from django.utils.translation import activate
from .forms import CsvModelForm
from .models import Csv, Data
import csv
from .utils import get_plot, get_boxplot
import numpy as np
import matplotlib.pyplot as plt
from django.http import HttpResponse, response
from django.core.paginator import EmptyPage, Paginator
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    print(row)  
                    date = row[0]
                    appl_open = row[1]
                    appl_high = row[2]
                    appl_low = row[3]
                    appl_close = row[4]
                    appl_volume = row[5]
                    appl_adjusted = row[6]
                    dn = row[7]
                    mavg = row[8]
                    up = row[9]
                    direction = row[10]

                    Data.objects.create(
                        date = date,
                        appl_open = appl_open,
                        appl_high = appl_high,
                        appl_low = appl_low,
                        appl_close = appl_close,
                        appl_volume = appl_volume,
                        appl_adjusted = appl_adjusted,
                        dn = dn,
                        mavg = mavg,
                        up = up,
                        direction = direction             
                    )
                   
            obj.activated = True
            obj.save()

    return render(request, 'core/task.html', {'form' : form})


def get_data(request):
    dataset = Data.objects.all()
    qs = Data.objects.get_queryset().order_by('id')
    x = [x.appl_low for x in dataset]
    y = [y.appl_high for y in dataset]
    z = [z.appl_open for z in dataset]
    area = 14
    colors = np.random.rand(len(x))
    chart = get_plot(x, y, area, colors)
    data_1 = np.random.normal(x)
    data_2 = np.random.normal(y)
    data_3 = np.random.normal(z)
    data = [data_1, data_2, data_3]
    chart2 = get_boxplot(data)
    p = Paginator(qs, 5)
    page_num = request.GET.get('page', 1)

    try :
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    return render(request, 'core/table.html', {'dataset': dataset, 'qs': page, 'chart': chart, 'chart2': chart2})


def d_csv(request):
    dataset = Data.objects.all()
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=data.csv'
    writer = csv.writer(response)

    writer.writerow(['Date', 'aapl_open', 'appl_high', 'appl_low', 'appl_close', 'appl_volume', 'appl_adjusted', 'dn', 'mavg', 'up', 'direction'])

    for data in dataset:
        writer.writerow([data.date, data.appl_open, data.appl_high, data.appl_low, data.appl_close, data.appl_volume, data.appl_adjusted, data.dn, data.mavg, data.up, data.direction ])
    return response


def some_view(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    x = 5
    p.drawString(100, 100, "{{x}}")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')