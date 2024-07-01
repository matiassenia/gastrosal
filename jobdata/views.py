from django.shortcuts import render, redirect
from .forms import JobDataForm, JobDataFilterForm
from .models import JobData
from django.db.models import Count
from django.utils import timezone

def upload_data(request):
    now = timezone.now()
    data_count = JobData.objects.count()
    context = {
        'date': now.strftime("%d/%m/%Y"),
        'time': now.strftime("%H:%M:%S"),
        'data_count': data_count,
    }
    
    if request.method == 'POST':
        form = JobDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_list')
    else:
        form = JobDataForm()
    
    context['form'] = form
    return render(request, 'jobdata/upload_data.html', context)

def data_list(request):
    data = JobData.objects.all()
    category_counts = JobData.objects.values('position').annotate(count=Count('position'))
    data_count = data.count()
    
    # Procesar el formulario de filtro si se envía
    if request.method == 'GET':
        form = JobDataFilterForm(request.GET)
        
        if form.is_valid():
            position = form.cleaned_data.get('position')
            currency = form.cleaned_data.get('currency')
            contract_type = form.cleaned_data.get('contract_type')

            # Aplicar filtros si los campos no están vacíos
            if position:
                data = data.filter(position=position)
            if currency:
                data = data.filter(currency=currency)
            if contract_type:
                data = data.filter(contract_type=contract_type)
    else:
        form = JobDataFilterForm()

    now = timezone.now()
    context = {
        'data': data,
        'data_count': data_count,
        'form': form,
        'date': now.strftime("%d/%m/%Y"),
        'time': now.strftime("%H:%M:%S")
    }
    return render(request, 'jobdata/data_list.html', context)
