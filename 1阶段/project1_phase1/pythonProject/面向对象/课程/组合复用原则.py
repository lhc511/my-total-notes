# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Employee(Person):
#     def __init__(self, name, age, employee_id):
#         super().__init__(name, age)
#         self.employee_id = employee_id
#
#
# # 使用合成复用原则
# person = Person("Alice", 25)
# employee = Employee("Bob", 30, "E123")
#
#
# # 使用继承关系 继承过程当中要重写
# class Employee(Person):
#     def __init__(self, name, age, employee_id):
#         self.name = name
#         self.age = age
#         self.employee_id = employee_id
