from django.shortcuts import render
from django.utils.translation import activate
from .forms import CsvModelForm
from .models import Csv, Data
import csv


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
                    # row = "".join(row)
                    # row = row.replace(",", " ")
                    # row = row.split()
                    print(row)  
                    date = row[0]
                    aapl_open = row[1]
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
                        aapl_open = aapl_open,
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
    qs = Data.objects.all()
    return render(request, 'core/table.html', {'dataset': dataset, 'qs' : qs})
