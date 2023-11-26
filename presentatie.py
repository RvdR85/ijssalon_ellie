mijn_dict = {"vis": 10, 
             "vlees": 25, 
             "overig": 15}
totaal = 50

#global mijn_dict en global totaal verwijderd voor hwo 10.
def presenteer(dict,tot):
    for key, value in dict.items():
        print (f"{key} : {value} Euro")
        
    print ("=======================")
    print (f"totaal : {tot} Euro")
    
