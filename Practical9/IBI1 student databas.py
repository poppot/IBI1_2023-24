class students():                                                           #create a class
    def __init__(self,name,major,code,group,exam):                          #the initiate function
        self.name=name
        self.major=major
        self.code=code
        self.group=group
        self.exam=exam
    def information(self,name,major,code,group,exam):                       #the reading function
        print(name,major,code,group,exam)
name=input(":")
major=input(':')
code=input(':')
group=input(':')
exam=input(':')
b=students(name,major,code,group,exam)
b.information(name,major,code,group,exam)
