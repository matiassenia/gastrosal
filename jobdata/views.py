from django.shortcuts import render, redirect
from .forms import JobDataForm  # Importa correctamente el formulario
from .models import JobData  # Corrige la importación del modelo JobData
from django.db.models import Count

def upload_data(request):
    if request.method == 'POST':
        form = JobDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_list')
    else:
        form = JobDataForm()
    return render(request, 'jobdata/upload_data.html', {'form': form})

def data_list(request):
    data = JobData.objects.all()
    category_counts = JobData.objects.values('position').annotate(count=Count('position'))
    return render(request, 'jobdata/data_list.html', {'data': data, 'category_counts': category_counts})