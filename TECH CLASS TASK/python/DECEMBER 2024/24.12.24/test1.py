def calculate_fare(mile,min):
    basefare=2.50
    milefare=1.50
    minfare=0.25
    surgeprice=1.5
    try:
        if mile>0 and min>0:
            mile*=milefare
            min*=minfare
            totalfare=(basefare+mile+min)*surgeprice
            print(f"the calculated fare is ${totalfare}")
        else:
            raise ValueError("invalid")
    except ValueError as e:
        print(e)
mile=float(input())
min=float(input())
calculate_fare(mile,min)