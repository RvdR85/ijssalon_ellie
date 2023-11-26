def decoreer (tekst=""):
    lengte = len(tekst) + 4
    print ()
    print (lengte * "*")
    print (f"* {tekst} *")
    print (lengte * "*")
    print ()

def fooi_pp(bedrag,personen):
    bedrag_pp = bedrag/personen
    return (f"het bedrag per persoon is {bedrag_pp} euro.") 

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit  

def som(dict1):
    totaal = 0
    for values in dict1.values():
        totaal += values
    return (totaal)
