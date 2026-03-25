import os
try:
    from CoolProp.CoolProp import PropsSI
except:
    os.system("pip install CoolProp")


while True:
    T=float(input("请输入温度（摄氏度）："))+273.15
    P =float(input("请输入压强（KPa）："))*1000+101325

    rho = PropsSI('D','T',T,'P',P,'Air')        #密度
    cp = PropsSI('C','T',T,'P',P,'Air')         #比热
    mu = PropsSI('V','T',T,'P',P,'Air')      # 黏度
    k  = PropsSI('L','T',T,'P',P,'Air')   # 导热系数


    print("Cp（kj/kg*K）:", cp/1000)
    print("密度（kg/m3）:", rho)
    print("粘度（Pa*s）",mu)
    print("导热系数（W/m*K）",k)
