import os
try:
    from CoolProp.CoolProp import PropsSI
except:
    print('缺少运行必需的依赖，开始安装...')
    os.system("pip install CoolProp")
    from CoolProp.CoolProp import PropSI


while True:
    T=float(input("请输入温度（℃）："))+273.15
    P =float(input("请输入压强（kPa）："))*1000+101325

    rho = PropsSI('D','T',T,'P',P,'Air')        #密度
    cp = PropsSI('C','T',T,'P',P,'Air')         #比热
    mu = PropsSI('V','T',T,'P',P,'Air')      # 黏度
    k  = PropsSI('L','T',T,'P',P,'Air')   # 导热系数


    print("Cp（kj/kg*℃）:", cp/1000)
    print("密度（kg/m^3）:", rho)
    print("粘度（Pa*s）",mu)
    print("导热系数（W/m*℃）",k)
