base_hours=40
ot_multiple=1.5

hours=float(input("enter the value of hours"))
pay_rate=float(input("enter the value of pay_rate"))

if hours > base_hours:
    overtime_hours = hours - base_hours
    overtime_pay=overtime_hours*pay_rate*ot_multiple
    gross_pay=base_hours*pay_rate+overtime_pay
    print("the gross pay is $ ", gross_pay)

else:
    gross_pay = hours*pay_rate 
    print("the gross pay is $ ", gross_pay)   
