afstandkm = eval(input("voer de afstand in: "))
weekendrit = input("is het weekend? ")
leeftijd = eval(input("voer je leeftijd in: "))

def standaardtarief(afstandkm):
    a=0
    if afstandkm >= 50:
        a=((afstandkm * 0.60)+15)
    elif afstandkm >=0.1:
        a=(afstandkm * 0.80)
    return a


def ritprijs (leeftijd,weekendrit,afstandkm):
    a=standaardtarief(afstandkm)
    if (leeftijd <12 or leeftijd >= 60) and weekendrit == "nee":
        a=a*0.70
    elif (leeftijd <12 or leeftijd>=60) and weekendrit == "ja":
        a=a*0.65
    elif (leeftijd >12) and weekendrit == "ja":
        a=a*0.60
    return a

a=ritprijs(leeftijd,weekendrit,afstandkm)
print(a, "euro")

