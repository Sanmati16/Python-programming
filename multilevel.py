class Student:
	def __init__(self,USN=None,name=None,age=None):
		self.USN=USN
		self.name=name
		self.age=age

	def getdata(self):
		self.USN=input("Enter USN= ")
		self.name=input("Enter student name= ")
		self.age=int(input("Enter Age of the student "))

	def display(self):
		print("USN = ",self.USN)
		print("Name of the Student = ",self.name)
		print("Age of the student = ",self.age)


class Subject(Student):
	def __init__(self,sem=0,sub1=0,sub2=0,sub3=0,sub4=0,sub5=0):
		self.sem=sem
		self.sub1=sub1
		self.sub2=sub2
		self.sub3=sub3
		self.sub4=sub4
		self.sub5=sub5

	def sub_getdata(self):
		self.sem=input("Enter Semester= ")
		self.sub1=int(input("Enter Subject-1 marks= "))
		self.sub2=int(input("Enter Subject-2 marks= "))
		self.sub3=int(input("Enter Subject-3 marks= "))
		self.sub4=int(input("Enter Subject-4 marks= "))
		self.sub5=int(input("Enter Subject-5 marks= "))
	def sub_display(self):
		print("Semester= ",self.sem)
		print("Subject-1 marks= ",self.sub1)
		print("Subject-2 marks= ",self.sub2)
		print("Subject-3 marks= ",self.sub3)
		print("Subject-4 marks= ",self.sub4)
                print("Subject-5 marks= ",self.sub5)

class Result(Subject):
	def res(self):
		self.tot=int(self.sub1+self.sub2+self.sub3+self.sub4+self.sub5)
		self.result=int((self.tot/500)*100)
		print("Total= ",self.tot)
		print("Result=",self.result,"%")


print("Student Result Information")
print("-"*60)
S=Result()
S.getdata()
S.sub_getdata()
print("*"*60)
S.display()
S.sub_display()
print("*"*60)
S.res()
print("-"*60)
