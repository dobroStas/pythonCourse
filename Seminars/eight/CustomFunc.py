import os


def show_contacts(file_name) :
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()
        
        for contact in data:
            print(contact, end='')
    print('')
    input('press any kay')
            
def add_contact(file_name) :
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = ''
        res += input('Input a surname of contact: ') + ' '
        res += input('Input a name of contact: ') + ' '
        res += input('Input a phone number of contact: ')

        file.write('\n' + res)
    input('press any kay')
        
def find_contact(file_name) :
    os.system('CLS')
    target = input('Input name of contact: ')
    
    with open(file_name, 'r') as file :
        contacts = file.readlines()
        
        for contact in contacts:
            if target in contact :
                print(contact)
                break
        else : print('There is not contacts with this name.')
    input('press any kay')

def change_contact(file_name) :                                             #метод изменения(удаляем старое, добавдяем новое)
    os.system('CLS')
    target = input('Input name of contact: ')
    res = ''
    with open(file_name, 'r') as file:                      # открыл для чтения. нашел и заменил элемент
        contacts = file.readlines()
        for contact in contacts:
            if target in contact :
                print(contact)
                print('If U want change to "Surname" press 0')
                print('If U want change to "Name" press 1')
                print('If U want change to "Phone number" press 2')
                num = int(input('Input of num: '))
                contact = contact.split()
                contact[num] = input('Input data: ')
                contact_str = " ".join(contact)
                print(contact_str)
                
    with open(file_name, 'w') as file:                                          
                            
        for contact in contacts:
            if not target in contact :
                file.write(contact)
                
        file.write('\n' + contact_str)
      

    input('press any kay')

        
    
def deleted_contact(file_name) :
    os.system('CLS')
    delet = input('input name of contact for deleted: ')
    with open(file_name, 'r') as file :
        contacts = file.readlines()
        
    with open(file_name, 'w') as file:           
        for contact in contacts:
            if not delet in contact :
                file.write(contact)
                
    
      
        # print(contacts, file=file_name)
                
    
        
            
            

    
    


def drawing():
        print('1 - show contacts')
        print('2 - add contacts')
        print('3 - find contacts')
        print('4 - change contacts')
        print('5 - deleted contacts')
        print('6 - exit')

def main(file_name) :
    while True :
        os.system('CLS')
        drawing()
        user_choise = int(input('input a namber from 1 to 4.'))
        if user_choise == 1 :
            show_contacts(file_name)
        elif user_choise == 2 :
            add_contact(file_name)
        elif user_choise == 3 :
            find_contact(file_name)
        elif user_choise == 4 :
            change_contact(file_name)
        elif user_choise == 5 :
            deleted_contact(file_name)
        elif user_choise == 6 :
            print('have a nice day!')
            return



main('test.txt')

        
# show_contacts("test.txt")

