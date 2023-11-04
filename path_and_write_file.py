import os
os.path.join("Users", "PycharmProjects", "pythonProject2", "Sam_Sebe_Prog", "test.txt")

test = open("test.txt", "w")
test.write("hello from Python!")
test.close()


"""
автоматическое закрытие с 'with':

with open("test.txt", "w") as f:
    f.write("hello from Python!") 
"""
