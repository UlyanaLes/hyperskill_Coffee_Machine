class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id_student = name[:1] + last_name + str(birth_year)


st_name = input()
st_last_name = input()
st_birth_year = input()

current_st = Student(st_name, st_last_name, st_birth_year)
print(current_st.id_student)
