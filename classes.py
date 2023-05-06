"""Person (superclass) that has name , place_of_residence , display_attributes()
  Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
  Uncle (subclass of Persom)  that has additionally business , display_attributes()
  Bill(subclass of Sister and Uncle) that has additionally bill_amount, display_attributes()
main method:
create a sister class object and display its attributes 
create a Uncle class object and display its attributes 
create a Bill class object and display its attributes"""

class Person:
    def __init__(self,name,place_of_residence) -> None:
        self.name = name
        self.place_of_residence = place_of_residence
    
    def display_attributes(self):
        print(f"name : {self.name} \t place : {self.place_of_residence}")
        
class Sister(Person):
    def __init__(self,name,place_of_residence,exam_subjects) -> None:
        super().__init__(name,place_of_residence)
        self.exam_subjects = exam_subjects    
    
    def display_attributes(self):
        super().display_attributes()
        print(f"exam subjects are : {self.exam_subjects}")
        
class Uncle(Person):
    def __init__(self, name, place_of_residence,business) -> None:
        super().__init__(name, place_of_residence)
        self.business = business
        
    def display_attributes(self):
        super().display_attributes()
        print(f"business is : {self.business}")
        
# class Bill(Sister,Uncle):
#     def __init__(self,name,place_of_residence,exam_subjects,business,bill_amount):
#         Sister.__init__(self,name,place_of_residence,exam_subjects)
#         Uncle.__init__(self,name,place_of_residence,business)
#         self.bill_amount = bill_amount
        
#     def display_attributes(self):
#         super().display_attributes()
#         print(f"Bill amount : {self.bill_amount} ")
class Bill(Sister, Uncle):
    def __init__(self, name, place_of_residence, exam_subjects, business, bill_amount):
        Sister.__init__(self, name, place_of_residence, exam_subjects)
        Uncle.__init__(self, name, place_of_residence, business)
        self.bill_amount = bill_amount
        
    def display_attributes(self):
        super().display_attributes()
        print(f"Bill amount: {self.bill_amount}")

def main():
    sister = Sister("sanika","Washington DC",["python","java","aws","hadoop"])
    uncle = Uncle("gayatri","purandar","Teaching")
    bill = Bill("kalika","Bihar",["marathi","hindi","sanskrit"],"teaching and research",100)
    print("----------------------------------")
    print("Sister: ")
    sister.display_attributes()
    print("--------------------------------")
    print("Uncle: ")
    uncle.display_attributes()
    print("-------------------------------") 
    print("bill: ")
    bill.display_attributes()   
    
main()