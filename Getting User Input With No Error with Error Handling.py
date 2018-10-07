def getnameandage():
    
    try:
        name=input('Enter Your Name : ')
        
        if not name:
            raise ValueError('Please Enter Something')
            
        print(type(name))
        
        if (name.isdigit()):
            raise(ValueError('Please Enter String'))        
                    
        if isinstance(name,str):
            pass
        else:
            raise(ValueError('Please Enter String'))
            
        age=int(input('Enter Your Age : '))
        
        name.strip()
        
        return name,age
    
    except ValueError as e:
        print('Wrong Input. Please Try Again')
        getnameandage()
    

name,age = getnameandage()

print('Your name is ' ,name, 'and Age is ', age)
print('Your name is {} and age is {}'.format(name,age))
print('You Name is %s and Age is %d' %(name,age))



