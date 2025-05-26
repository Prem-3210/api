from django.shortcuts import render, redirect, get_object_or_404
from .models import Fields

# List all records with optional filtering
def field_list(request):
    fields = Fields.objects.all()

    # Apply filters based on query parameters
    if 'name' in request.GET:
        fields = fields.filter(name__icontains=request.GET['name'])
    if 'age' in request.GET:
        fields = fields.filter(age=request.GET['age'])
    if 'classname' in request.GET:
        fields = fields.filter(classname__icontains=request.GET['classname'])
    if 'marks' in request.GET:
        fields = fields.filter(marks=request.GET['marks'])

    return render(request, 'fields/field_list.html', {'fields': fields})

# Create new record
def field_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        classname = request.POST.get('classname')
        marks = request.POST.get('marks')
        Fields.objects.create(name=name, age=age, classname=classname, marks=marks)
        return redirect('fields:field_list')
    return render(request, 'fields/field_create.html')

# Update existing record
def field_update(request, field_id):
    field = get_object_or_404(Fields, id=field_id)
    if request.method == 'POST':
        field.name = request.POST.get('name')
        field.age = request.POST.get('age')
        field.classname = request.POST.get('classname')
        field.marks = request.POST.get('marks')
        field.save()
        return redirect('fields:field_list')
    return render(request, 'fields/field_update.html', {'field': field})

# Delete record
def field_delete(request, field_id):
    field = get_object_or_404(Fields, id=field_id)
    if request.method == 'POST':
        field.delete()
        return redirect('fields:field_list')
    return render(request, 'fields/field_delete.html', {'field': field})
