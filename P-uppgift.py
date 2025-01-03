import unittest

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
        self._capacity = 2 
        self._slots = [None] * self._capacity
        self._size = 0
       

    def _hash(self, key): # för att inte behöva gå igenom hela listan för att hitta nyckeln
        """
        Skapar ett index för nyckel strängen för att bestämma dess position
        
        Inparameter är nyckel för att vi ska kunna generera ett motsvarande index till nykeln
        
        Retunerar motsvarande index till nyckeln
        """
        hashsum = 0

        for i, c in enumerate(key): # i representerar positionen för tecknet i strängen och c är själva tecknet.
            hashsum += (i + len(key)) ** ord(c) # ord(c) = motsvarande unikod punkt för c
	
        hashsum = hashsum % self._capacity

        return hashsum
    
     
    def insert(self, key, value):
        """
        Sätter in en nyckel och motsvarande värde i vår hashtabell
        
        Inparameter är nyckel och värdet vi vill att nycken ska motssvara
        
        Retunerar inget om allt gick bra. 
        Returnerar ValueError om nyckeln inte är en sträng.
        Retunerar Exception om det inte går att sätta in nyckeln och värder eftersom hashtabellen är full
        """
        if not isinstance(key, str):
            raise ValueError("Key has to be a string")
        
        if self._size >= self._capacity:
            raise Exception("Can not insert element, hash table is already full")
        
        index = self._hash(key)
        start_index = index

        while self._slots[index] is not None:
            if self._slots[index]._key == key:
                self._slots[index]._value = value

                if self._slots[index]._previously_occupied == True:
                    self._slots[index]._previously_occupied = False
                    self._size += 1

                return
            
            if self._slots[index]._previously_occupied == True:
                self._slots[index] = _Node(key,value)
                self._size += 1
                
                return
            
            index = (index + 1) % self._capacity #Går till nästa plats
            
            if start_index == index:
                break

        self._slots[index] = _Node(key,value)
        self._size += 1


    def find(self, key):
        """Tar fram det motsvarande värdet till nyckel
        
        Inparameter är nyckel för att vi ska kunna hitta den
        
        Retunerar motsvarande värde till nyckeln om nyckeln hittas.
        Returerar None om nyckeln inte hittas
        """
        index = self._hash(key)
        start_index = index

        while self._slots[index] is not None:
            if self._slots[index]._key == key and self._slots[index]._previously_occupied == False:
                return self._slots[index]._value
            
            index = (index + 1) % self._capacity
            
            if start_index == index:
                break

        return None


    def remove(self, key): # Genom att ge den värdet False
        """
        Raderar nyckeln från hashtabellen och returnar den raderade nyckeln

        Inparameter är nyckel för att vi ska kunna hitta och ta bort nykeln samt dess värde
        
        Retunerar nyckeln om den lyckas radera nyckln och värdet.
        Retunerar None om nyckeln inte hittas
        """
        index = self._hash(key)
        start_index = index

        while self._slots[index] is not None:
            if self._slots[index]._key == key and self._slots[index]._previously_occupied == False:
                self._slots[index]._previously_occupied = True
                self._size -= 1
                return self._slots[index]._key
            
            index = (index + 1) % self._capacity

            if start_index == index:
                break

        return None


class TestHashTable(unittest.TestCase):
    """"Testing the hash table"""

    def setUp(self): 
        self.H = HashTable()

    def test_insert_element(self):
        self.H.insert('Bob', 15)
        self.assertEqual(self.H.find('Bob'), 15)

    def test_insert_int_key(self):
        with self.assertRaises(ValueError):
            self.H.insert(2, 17)
    
    def test_change_value(self):
        self.H.insert('Bob', 15)
        self.H.insert('Bob', 19)
        self.assertEqual(self.H.find('Bob'), 19)

    def test_insert_in_full_hashtable(self):
        self.H.insert('Bob', 15)
        self.H.insert('572', '10')
        with self.assertRaises(Exception):
            self.H.insert('Ali', 20)
        self.assertEqual(self.H._size, 2)
        self.assertEqual(self.H.find('Ali'), None)

    def test_remove_element(self):
        self.H.insert('Bob', 15)
        self.assertEqual(self.H.remove('Bob'), 'Bob')
        self.assertEqual(self.H._size, 0)
        self.assertEqual(self.H.find('Bob'), None)
     
    def test_remove_non_existing_element(self):
        self.H.insert('Bob', 15)
        self.assertEqual(self.H.remove('Ali'), None)
        self.assertEqual(self.H._size, 1)
        self.assertEqual(self.H.find('Bob'), 15)

    def test_reuse_a_slot(self): # För att testa kollision ändra hashsum = len(key) % self._capacity
        self.H.insert('Bob', 15)
        self.H.insert('572', '10')
        self.assertEqual(self.H.remove('572'), '572')
        self.H.insert('Ali', 20)
        self.assertEqual(self.H._size, 2)
        self.assertEqual(self.H.find('Ali'), 20)
        self.assertEqual(self.H.find('Bob'), 15)
        self.assertEqual(self.H.find('572'), None)


if __name__ == '__main__':
    unittest.main()

    
# https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd
# https://prepinsta.com/data-structures-and-algorithms-in-python/linear-probing-in-hashing/

