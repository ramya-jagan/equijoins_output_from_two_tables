from django.shortcuts import render

# Create your views here.

from app.models import *
def equijoin(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gt=1500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dloc='chicago')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dloc='chicago',mgr=7839)
    
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoin.html',d)

  
