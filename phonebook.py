class Phonebook:


  def __init__(self):
    self.d = {}
    self.menu(self.d)

  def add(self, d):
    name = input("Enter the name")
    for key in d.keys():
      if key == name:
        print("Contact with the same name already exists")
        self.menu()
  
    number = int(input("Enter the number"))
    val = {}
    self.d[name] = val
    val['Number'] = number
    email = input("Enter an the email id")
    val['Email'] = email
    print(d)
    self.menu(self.d)
    
  def mod(self, d):
    print("\n1. Number\n2. Email id") 
    change = int(input("Enter the field that you want to change"))
    if change == 1:
      name = input("Enter the name")
      new_number = int(input("Enter the new number"))
      d[name]['Number'] = new_number
    elif change == 2:
      name = input("Enter the name")
      new_email = input("Enter the new Email id")
      d[name]['Email'] = new_email
    print(d)
    self.menu(self.d)

  def delete(self, d):
    name = input("Enter the name of the contact to be deleted")
    if name in self.d.keys():
      self.d.pop(name)
      print("Contact deleted")
    else:
      print("Enter an already existing name")
    print(d)
    self.menu(self.d)


  def search(self, d):
    name = input("Enter the name of the contact you want to search")
    if name in d.keys():
      print(name, d[name])
    else:
      print("Contact not available")
      
    

  def menu(self, d):
    print("\n1. Add a contact\n2. Modify\n3. Delete\n4. Search\n5. Exit")
    op = int(input("Choose an option"))
    if op == 1:
      self.add(self.d)
    elif op == 2:
      self.mod(self.d)
    elif op == 3:
      self.delete(self.d)
    elif op == 4:
      self.search(self.d)
    elif op == 5:
      exit()
    else:
      print('Enter a proper choice')
      self.menu(self.d)

Phonebook()
        
