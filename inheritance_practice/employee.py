class Employee:
    def __init__(self, name, job_title, salary, years_of_experience):
        self.name = name
        self.job = job_title
        self.salary = salary
        self.experience = years_of_experience
    
    def change_job_title(self):
        print("Employee has become a Supervisor")
        self.job = "Supervisor"
    
    def increase_salary(self, percentage):
        self.salary = self.salary * (1 + int(percentage))
        print("Employee's salary is now " + self.salary)
    
    def increase_yoe(self):
        self.experience += 1
        print("Employee now has " + str(self.experience) + " Years of Experience.")
    
    def calclate_hourly_rate(self):
        hourly = self.salary / 8
        print("Employee's hourly rate is " + str(hourly))
    
class Manager(Employee):
    def __init__(self, name, job_title, salary, years_of_experience):
        super().__init__(self, name, job_title, salary, years_of_experience)
        self.bonus = 0
    
    def calculate_bonus(self):
        rate = self.salary * self.experience
        bonus = rate / 10
        self.bonus = bonus

