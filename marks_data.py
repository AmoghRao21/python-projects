class Tenth():
    
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        
    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"Your Average score is : ",sum/3)
        
s1 = Tenth("Tony Stark", [98,94,89])

s1.avg()