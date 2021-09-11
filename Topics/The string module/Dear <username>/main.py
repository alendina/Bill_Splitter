import string
my_templ = string.Template('Dear $username! It was really nice to meet you. Hopefully, you have a nice day! See you soon, $username!')
my_str = my_templ.substitute(username=input())
print(my_str)
