import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
 'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
 'a','b','c','d','e','f','g','h','i','j','k','l','m',
 'n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '@', '$', '%', '^', '&', '*', '(',')', '+','#']

print("welcome to password generators")

nr_ltr = int(input("how many ltr you want in password?/n"))
nr_num = int(input("how many numbers you want?/n"))
nr_symb = int(input("how many symbols is required?/n"))

password =[]

for pswrd in range(1,nr_ltr+1):
    password += random.choice(letters)
    
for pswrd in range(1,nr_num+1):
    password += random.choice(numbers)
    
for pswrd in range(1,nr_symb+1):
    password += random.choice(symbols)

random_password = random.shuffle(password)

final_random_password=''
for fnl_pass in password:
    final_random_password += fnl_pass
    
print(final_random_password)


    

             
        

