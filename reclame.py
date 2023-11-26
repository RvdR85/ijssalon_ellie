from algemene_functies import mijn_functie_2

from statistics import mean


def aanbieding_1(smaak, prijs, korting):
    korting = (prijs-(prijs*korting))
    return (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro.") 

print (aanbieding_1("aardbei", 4, 0.1))


def inkomsten_totaal (inkomsten, btw):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    bedrag = (totaal*btw)
    return (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden") 

inkomsten =[220,430,125,160,205,90,345]
print (inkomsten_totaal(inkomsten,0.09))

def laag_en_hoog(mijn_lijst):
    return (max(mijn_lijst), min(mijn_lijst))
mijn_lijst = [220,430,125,160,205,90,345]
print (laag_en_hoog(mijn_lijst))

def gemiddelde(mijn_lijst):
    return (f"De gemiddelde inkomsten deze week zijn {mean(mijn_lijst)} euro.")
print (gemiddelde(mijn_lijst))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
invoer_lijst = [10,5,3,2,1,2,9]
print (meervoudig(invoer_lijst))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],[1])
    return uitvoer
     
