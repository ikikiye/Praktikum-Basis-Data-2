def volume_kubus(x):
    vol=x*x*x
    print("Luas kubus:",vol,"meter kubik")
    return vol

def volume_balok(p,l,t):
    vol=p*l*t
    print("Luas balok:",vol, "meter kubik")
    return vol

p=int(input("x : "))
l=int(input("y : "))
t=int(input("z : "))

lk = volume_kubus(p)
lb = volume_balok(p,l,t)

if lb > lk:
    print("luas balok lebih besar dari luas kubus")
elif lb < lk:
    print("luas balok lebih kecil dari luas kubus")
else:
    print("luas balok sama dengan luas kubus")