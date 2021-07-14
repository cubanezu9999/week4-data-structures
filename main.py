list = ['John','Peter','Paul','Paul']

def menu():
  choice = ''
  while(choice !=4):
    print('**************************')
    print('*** Welcome to SOL Student register ***')
    print('****************************')
    print('1.Register Students')
    print('2.List all students')
    print('3.Remove Student')
    print('4.Exit')
    choice = int(input('Please enter option: '))
    if(choice == 1):
     register()
    elif(choice == 2):
     list_all()
    elif(choice == 3):
     remove()


def register():
  global list
  name = input('Please enter first name: ')
  list.append(name)

def list_all():
  global list
  print(list)

def remove():
  name = input('Please enter name: ')
  
  #list.clear
   #print(list.pop(index)) pop out a name from index argument
  try:
   print(list.remove(name))
   #del list[0] take only index as argument
  except Exception:
    print('No student with such name:',name)
    remove()
  

