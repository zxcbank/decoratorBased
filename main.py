def smthProcess():
    print("WORKING MOTHERFU***")

def decorator(func):

     def subdecorator():
         print('start subdecorator')
         func()
         print('start subdecorator')

     return subdecorator

print('WAS-------------')
smthProcess()
print('COME------------')
smthProcess = decorator(smthProcess)
smthProcess()
