
#Introduction
print("Welcome to my Temperature Converter! \n")

def converter(fahrenheit_or_celsius):

#(32°F − 32) × 5/9 = 0°C for fahrenheit to celsius

    if fahrenheit_or_celsius == 'F':
        fnum = int(input("How many degrees F to C?: "))
        f_equation = (fnum - 32) * 5/9 
        print(f'That number Fahrenheit to Celsius is {f_equation} !')
    
#(0°C × 9/5) + 32 = 32 for celsius to fahrenheit

    elif fahrenheit_or_celsius == 'C':
        cnum = int(input("How many degrees C to F?: "))
        c_equation = (cnum * 9/5) + 32
        print(f'That number Celsius to Fahrenheit is {c_equation} ! \n')
    
    else:
        print("Error, invalid option or something went wrong, try again! :/")
    


#Setting While Loop

again = 'Y'

while again == 'Y':
    fahrenheit_or_celsius = input("Fahrenheit or Celsius Conversion? (F/C): ").upper()
    converter(fahrenheit_or_celsius)
    
    re_convert = input("Would you like to convert again? (Y/N): ").upper()
    if re_convert == 'N':
        break



  
    
  
    

    



