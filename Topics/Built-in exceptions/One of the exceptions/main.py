list_of_exceptions = dir(locals()['__builtins__'])
# print(len(list_of_exceptions), list_of_exceptions)
num = int(input())
print(list_of_exceptions[num])
