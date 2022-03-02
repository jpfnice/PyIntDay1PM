
'''
Given a file with the following format:
    
    City name;time;date;temperature
    Geneva;12:34;2003/12/23;2.34;
    Lausanne;12:36;2003/12/23;3.34;
    Bern;12:36;2003/12/23;-3.34;
    ....
    
Write a python script to parse this file and store it's content into a "custom
object".

You could define a class "Record" that will represent a line of this file and
a class "ListOfRecord" to represent a list of "Record".
This class "ListOfRecord" should offer a way to construct an instance of it
with the help of a text file like the one above.
It should also offers ways to save/restore the list easily.
And a method to compute the average of the temperature recorded for a given city name.

with open("data.txt") as fic:
    first=fic.readline()
    for line in fic:
        print(line)
        
class Record:
    a constructor (__init__())
    a way to convert a Record into a String (__str__(), __repr__())
    4 attributes: city, time, date, temperature for instance
    
class ListOfRecord:
    a constructor (__init__())
    a class method to transform a text file into a ListOfRecord (parseFile())
    a method to compute the average of the temperature recorded for a given
    city (average())
    a method to save a ListOfRecord into a file (using pickle) (save())
    a class method to load a ListOfRecord from a file (using pickle) (load())
    the method(s) needed to iterate trough a ListOfRecord (__iter__())
    1 attribute: a list to store the Record
    Optionally: 
            method to add/remove Record from the ListOfRecord (append(), remove(), ...)
            method to compute the length of a ListOfRecord (__len__())
            method to compare 2 ListOfRecords with == (__eq__())
            ...

'''
