from django.shortcuts import render
from django.db.models import Q
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


def selfjoin(request):
    EMPOBJECTS=Emp.objects.select_related('mgr').all()
    EMPOBJECTS=Emp.objects.select_related('mgr').filter(mgr__ename='king')
    
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'selfjoin.html',d)   

def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='king')
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__lt=3000)
    emd=Emp.objects.select_related('deptno','mgr').filter(ename__startswith='b',ename__endswith='e')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(job='salesman') | Q(deptno__dloc='new york'))
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='accounting')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(ename__startswith='a')|Q(deptno=10))
    emd=Emp.objects.select_related('deptno','mgr').all()[:5:]
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gt=1000,sal__lt=2500)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(sal__gt=1000,sal__lt=2500)|Q(deptno__dname='sales'))
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno=10)|Q(deptno__dloc='new york'))
    # emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__gt='01/01/2023',hiredate__lt='10/12/2023')
    emd=Emp.objects.select_related('deptno','mgr').all()[2:5:]
    
    
    
    

    
    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)


  
