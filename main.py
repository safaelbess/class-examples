class Employee:
  def __init__(self, name, age, salary, degree, specialise):
    self.name=name
    self.age=age
    self.salary=salary
    self.degree=degree
    self.specialise=specialise

  def __str__(self):
    return f'the employee name is {self.name} , age is {self.age} , salary is {self.salary} ,degree is {self.degree} , and specialisation is {self.specialise}'

  def promotion(self,salary):
    if salary<=500:
     salary==salary + salary*20/100
    else :
      salary= salary +salary*10/100

    return f'the new salary is {salary}'

name=input('enter the employee name :')
age =int(input('enter the employee age :'))
salary=int(input('enter the salary :'))
degree=int(input('enter the employee degree :'))
specialise=input('enter the employee specialise :')



Employee1=Employee(name,age, salary, degree, specialise)
print(Employee1)

print(Employee1.promotion(salary))



class Patient:
  def __init__(self, name ,age, disease,medicines, insurance,discount):
    name=self.name
    age=self.age
    disease=self.disease=[]
    medicines=self.medicines=[]
    insurance=self.insurance
    discount=self.discount
    
    

  def patient_info(name,age,disease,medicines,insurance):
    return f'the patient name is {name} , age is {age} ,diseases are {disease} ,medicines are {medicines} and inurance is {insurance} '

  def check_age (discount,age):
    if age<60:
      return f'the patient have to pay all the treatment costs'

    else :

      return f'the patient has a discount {discount} JD'

name=input ('enter the patient name : ')
age=int(input('enter the patient age :'))
disease=[]
nofdisease=int(input('enter the number of diseases:'))
for i in range(nofdisease):
  dis_name =input('enter the disease name')
  disease.append(dis_name)
medicines=[]
nofmedicines=int(input('enter the number of medicines:'))
for i in range(nofmedicines):
  med_name =input('enter the medicine name')
  medicines.append(med_name)
insurance=input('enter the insurance name :')  
discount=50
Patient1=Patient(name,age,disease,medicines,insurance,discount)
print(Patient1.patient_info(name,age,disease,medicines,insurance))
print(Patient1.check_age(age,discount))


