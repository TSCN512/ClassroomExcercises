"Follows from list comprehension, note syntax"

sample = {"dog" : "Trace", "food" : "wet", "clothes": "coats"}
TraceList = {key.upper():value.upper() for key,value in sample.items()}
                                    #remember to use an iterable ^^^
                #(key,value) should also be valid^^
                                        
print(TraceList)
import random
students = ["Trace", "Aunn", "Momiji"]
studentScores = {name:random.randint(0,100) for name in students}
passedStudents = {name:score for name,score in studentScores.items() if score>60}
print(studentScores)
print(passedStudents)