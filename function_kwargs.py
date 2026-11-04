
# program for function variable length keyword arguments 
def student(**details):
    for key, value in details.items():
        print(key, ":", value)

student(name="Reshma", age=19, branch="AI & ML", year=2)
