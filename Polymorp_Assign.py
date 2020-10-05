

# Parent class
class User:
    def __init__(self, name='None', email='None', password='None'):
        self.name = name
        self.email = email
        self.password = password

    
    
    def set_name(self, name):
        self.name = name


    def set_email(self, email):
        self.email = email


    def set_password(self, password):
        self.password = password
        

    def LoginNfo(self):
        entry_name = input('Enter your name: ')
        entry_email = input('Enter your email:')
        entry_password = input('Enter your password:')
        if (entry_email == self.email and entry_password == self.password):
            print('\nYou\'re back, {}!\n'.format(entry_name))
        else:
            print('\nSomething went wrong with your login creds\n')


# Child classes
class Cook(User):
    hours = 40
    station = 'Grill'
    

    def information(self):
        cooknfo = "\nHours: {}\nStation: {}\n".format(self.hours,self.station)
        return cooknfo
    
    def __init__(self, name='None', userID='None', password='None'):
        self.name = name
        self.userID = userID
        self.password = password

    def LoginNfo(self):
        entry_name = input('Enter your name: ')
        entry_userID = input('Enter your ID #: ')
        entry_password = input('Enter your password: ')
        if (entry_userID == self.userID and entry_password == self.password):
            print('\nWelcome to work, {}!\n'.format(entry_name))
        else:
            print('\nSomething went wrong with your login creds\n')



class Manager(User):
    staff = 6
    section = 'Patio'

    def info(self):
        bossnfo = "\nStaff under you this shift: {}\nSection: {}\n".format(self.staff,self.section)
        return bossnfo
    
    
    def __init__(self, name='None', userID='None', pin='None'):
        self.name = name
        self.userID = userID
        self.pin = pin

    def LoginNfo(self):
        entry_name = input('Enter your name: ')
        entry_userID = input('Enter your ID #: ')
        entry_pin = input('Enter your pin #: ')
        if (entry_userID == self.userID and entry_pin == self.pin):
            print('\nLet\'s make this shift great, {}!\n'.format(entry_name))
        else:
            print('\nSomething went wrong with your login creds\n')
    
    











if __name__ == "__main__":
    worker = User('Nick', 'nick@gmail.com', 'pass')
    worker.LoginNfo()

    lineworker = Cook('Tim', 'tim1234', 'pass')
    lineworker.LoginNfo()
    print(lineworker.information())

    manager = Manager('Sara', 'sara0987', 'pass')
    manager.LoginNfo()
    print(manager.info())
