"""
En hashtabell skapar en lista som innehåller nycklar, där varje nyckel har ett motsvarande värde

Den är byggd med linjär probing vi kollision, så om två nycklar har samma hash index kommer den 
nya nyckeln att ta nästa lediga plats istället. 

Nycklarna får endast var stränger men value kan ha vilket värde som helst.
"""

class _Node:
    """
    En Node som sparar nyckel och dess motsvarande värde samt om den är borttagen eller inte
    """
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._previously_occupied = False

class HashTable:
    """
    En hashtabell som är byggd med hjälp av linjär probing vid kollision
    """
    def __init__(self):
        self._capacity = 2 #Initial value
        self._slots = [None] * self._capacity
        self._size = 0
       
    def _hash(self, key): # för att inte behöva gå igenom hela listan för att hitta nyckeln
        """
        Skapar ett index för nyckel strängen för att bestämma dess position
        
        Inparameter är nyckel för att vi ska kunna generera ett motsvarande index till nykeln
        
        Retunerar motsvarande index till nyckeln
        """

    def insert(self, key, value):
        """
        Sätter in en nyckel och motsvarande värde i vår hashtabell
        
        Inparameter är nyckel och värdet vi vill att nycken ska motssvara
        
        Retunerar inget om allt gick bra. 
        Returnerar ValueError om nyckeln inte är en sträng.
        Retunerar Exception om det inte går att sätta in nyckeln och värder eftersom hashtabellen är full
        """

    def find(self, key):
        """Tar fram det motsvarande värdet till nyckel
        
        Inparameter är nyckel för att vi ska kunna hitta den
        
        Retunerar motsvarande värde till nyckeln om nyckeln hittas.
        Returerar None om nyckeln inte hittas
        """

    def remove(self, key): 
        """
        Raderar nyckeln från hashtabellen och returnar den raderade nyckeln

        Inparameter är nyckel för att vi ska kunna hitta och ta bort nykeln samt dess värde
        
        Retunerar nyckeln om den lyckas radera nyckln och värdet.
        Retunerar None om nyckeln inte hittas
        """


# https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd

