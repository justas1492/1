a = float(input("Kuro kaina € už litra "))
b = float(input("Kuro sanaudos litrų 100km "))
c = float(input("Norimas nuvažiuoti atstumas km "))

d = b * c / 100
e = d * a

print("Jums šiai" , int(round(c, 2)) ,"km kelionei reikės", round(d, 2) , "L kuro ir tai kainuos",round(e, 2), "€")

("Jums šiai" , int(round(c, 2)) ,"km kelionei reikės", round(b * c, 2) , "L kuro ir tai kainuos",round(d * a, 2), "€")