class Student:
	def __init__(self,USN=None,name=None,age=None):
		self.USN=USN
		self.name=name
		self.age=age

	def getdata(self):
		self.USN=input("Enter USN")
		self.name=input("Enter Student name")
		self.age=int(input("Enter age"))

	def display(self):
		print("USN= ",self.USN)
		print("Name= ",self.name)
		print("Age= ",self.age)

class UGstudent(Student):
	def __init__(self,sem=0,fees=0,stipend=0):
		self.sem=sem
		self.fees=fees
		self.stipend=stipend

	def getData(self):
		self.sem=input("Enter Semester")
		self.fees=int(input("Enter Fees"))
		self.stipend=int(input("Enter Stipend"))

	def UGdisplay(self):
		print("Semester= ",self.sem)
		print("Fees= ",self.fees)
		print("stipend= ",self.stipend)

S1=UGstudent()
S1.getdata()
S1.getData()
S1.display()
S1.UGdisplay()
