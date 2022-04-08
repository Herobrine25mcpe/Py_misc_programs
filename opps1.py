
class Student:
    college= "Chandigarh University"

    def __init__(self):
        self.name = 'abhay'
        self.age = 20
        self.marks = 90
    

    def CGPA(self):
        self.cgpa = self.marks*0.95
        print("CGPA:", self.cgpa)
      


if __name__ =="main":

    st= Student()
    print(st.name)
    print(st.age)

