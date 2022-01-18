import math
# I realized that we have code to find molar mass so why not
# import it. I figured that's why we create functions so I thought
# it would be cool if I utilized some functions we created in the past
from chemistry import get_name, get_atomic_mass, \
        parse_formula, molar_mass, FormulaError
import cgitb 
cgitb.enable()

# The main thing I got from this is how to create a input that is unbreakable
# from the user. We learned kind of how to do that with a boolean loop and with try:
# but the try wasn't in a loop letting the user type again and the boolean was only good
# if you wanted your input to be a positive integer number. I tried stacking boolean loops
# to do what I wanted but that would always cause problems (creating never ending loops,
# or somehow stopping the loop when it wasn't supposed to be stopped). It took me forever
# find the solution of putting a try: in a loop and then to parameter that input with another
# boolean loop. Either way I am proud that I figured that out because I have been trying
# to do that all semester.
        

chemistry_list = ["1. V = nRT/P",
"2. P = nRT/V",
"3. n = PV/RT",
"4. D = (P*mm)/RT",
"5. Ke = 3/2*RT",
"6. Urnm = Squareroot(3RT/mm)",
"7. D = M/V",
"8. En = 2.31*10^-19(z/n)^2",
"9. E = hc/v",
"10. v = hc/|E|",
"11. v = h/mc",
"12. m = h/vc",
"13. M = n/V",
"14. Find molar mass",
"15. Find moles"]


def main():
    #Print list
    for item in chemistry_list:
        print(item)
    print('')

    # Ensure input is a valid input
    valid = False
    while not valid:
        #Input
        user_choice = input("Please enter the number of the desired formula: ")
        if user_choice.isdecimal():
            integer = int(user_choice)
            if integer >= 1:
                if integer <= 16:
                    valid = True
                else:
                    print('The integer is not found in the given choices. Please choose again: ')
            else:
                print('The integer is not found in the given choices. Please choose again: ')
        else:
            print('Your input was not a integer. Please enter a valid integer: ')

    # Different paths based on input
## Option 1
    if integer == 1:
        while True:
            try:
                valid = False
                while not valid:
                    n = float(input('What is the amount of moles? '))
                    if n > 0:
                        valid = True
                    else:
                        print('Please enter a valid number of moles')
                break
            except:
                print('That is not a valid number. Please try again. ')

        while True:
            try:
                Temperature = float(input('What is the temperature of the gas? '))
                break                
            except:
                print('That is not a valid input, please try again. ')

        valid = False
        while not valid:
            F_or_C = input('Is this is Celius of Farenheit? Please type "C" or "F": ').upper()
            if F_or_C == "C":
                T = Temperature + 273.15
                valid = True
            elif F_or_C == "F":
                T = ((Temperature - 32) * 5/9) + 273.15
                valid = True
            else:
                print('Please enter a valid response')

        while True:
            try:
                valid = False
                while not valid:
                    P = float(input('What is the pressure in ATM\'s? '))
                    if P > 0:
                        valid = True
                    else:
                        print('The input for "ATM\'s" needs to be a positive number. Please try again. ')
                break
            except:
                print('That is not a valid input, please try again. ')

        volume = volume_of_gas(n, T, P)
        print(f'The volume from the values given is {volume} ')


## Option 2
    elif integer == 2:
        while True:
            try:
                valid = False
                while not valid:
                    n = float(input('What is the amount of moles? '))
                    if n > 0:
                        valid = True
                    else:
                        print('Please enter a valid number of moles')
                break
            except:
                print('That is not a valid number. Please try again. ')

        while True:
            try:
                valid = False
                while not valid:
                    V = float(input('What is the given volume in liters? '))
                    if V > 0:
                        valid = True
                    else:
                        print('Please enter a valid number for the volume')
                break
            except:
                print('That is not a valid number. Please try again.')
        
        while True:
            try:
                Temperature = float(input('What is the temperature of the gas? '))
                break                
            except:
                print('That is not a valid input, please try again. ')

        valid = False
        while not valid:
            F_or_C = input('Is this is Celius of Farenheit? Please type "C" or "F": ').upper()
            if F_or_C == "C":
                T = Temperature + 273.15
                valid = True
            elif F_or_C == "F":
                T = ((Temperature - 32) * 5/9) + 273.15
                valid = True
            else:
                print('Please enter a valid response')

        pressure = pressure_of_gas(n, T, V)
        print(f'The pressure from the values given is {pressure}')

## Option 3
    elif integer == 3:
        while True:
            try:
                valid = False
                while not valid:
                    V = float(input('What is the given volume in liters? '))
                    if V > 0:
                        valid = True
                    else:
                        print('Please enter a valid number for the volume')
                break
            except:
                print('That is not a valid number. Please try again.')

        while True:
            try:
                Temperature = float(input('What is the temperature of the gas? '))
                break                
            except:
                print('That is not a valid input, please try again. ')

        valid = False
        while not valid:
            F_or_C = input('Is this is Celius of Farenheit? Please type "C" or "F": ').upper()
            if F_or_C == "C":
                T = Temperature + 273.15
                valid = True
            elif F_or_C == "F":
                T = ((Temperature - 32) * 5/9) + 273.15
                valid = True
            else:
                print('Please enter a valid response')

        while True:
            try:
                valid = False
                while not valid:
                    P = float(input('What is the pressure in ATM\'s? '))
                    if P > 0:
                        valid = True
                    else:
                        print('The input for "ATM\'s" needs to be a positive number. Please try again. ')
                break
            except:
                print('That is not a valid input, please try again. ')

        moles = moles_of_gas(P, V, T)
        print(f'The number of moles from the values given is {moles}')


## Option 4
    elif integer == 4:
        
        while True:
            try:
                valid = False
                while not valid:
                    molar_mass = float(input('What is the molar mass of the compound? '))
                    if molar_mass > 0:
                        valid = True
                    else:
                        print('The molar mass needs to be a positive integer, please try again.')
                break            
            except:
                print('That is not a valid input, please try again. ')

        while True:
            try:
                Temperature = float(input('What is the temperature of the gas? '))
                break                
            except:
                print('That is not a valid input, please try again. ')

        valid = False
        while not valid:
            F_or_C = input('Is this is Celius of Farenheit? Please type "C" or "F": ').upper()
            if F_or_C == "C":
                T = Temperature + 273.15
                valid = True
            elif F_or_C == "F":
                T = ((Temperature - 32) * 5/9) + 273.15
                valid = True
            else:
                print('Please enter a valid response')

        while True:
            try:
                valid = False
                while not valid:
                    pressure = float(input('What is the pressure in ATM\'s? '))
                    if pressure > 0:
                        valid = True
                    else:
                        print('The input for "ATM\'s" needs to be a positive number. Please try again. ')
                break
            except:
                print('That is not a valid input, please try again. ')

        density = round(density_of_gas(pressure, molar_mass, T), 5)

        print(f'The answer to your given values is {density}')

## Option 5
    elif integer == 5:
        while True:
            try:
                Temperature = float(input('What is the temperature of the gas? '))
                break                
            except:
                print('That is not a valid input, please try again. ')

        valid = False
        while not valid:
            F_or_C = input('Is this is Celius of Farenheit? Please type "C" or "F": ').upper()
            if F_or_C == "C":
                T = Temperature + 273.15
                valid = True
            elif F_or_C == "F":
                T = ((Temperature - 32) * 5/9) + 273.15
                valid = True
            else:
                print('Please enter a valid response')
        kinetic_energy = kinetic_energy_of_gas(T)
        print(f'The kinetic energy of gas at the given temperature is {kinetic_energy}')

## Option 6  
    elif integer == 6:
        while True:
            try:
                valid = False
                while not valid:
                    mm = float(input('What is the molar mass of the compound? '))
                    if mm > 0:
                        valid = True
                    else:
                        print('The molar mass needs to be a positive integer, please try again.')
                break            
            except:
                print('That is not a valid input, please try again. ')

        while True:
            try:
                Temperature = float(input('What is the temperature of the gas? '))
                break                
            except:
                print('That is not a valid input, please try again. ')

        valid = False
        while not valid:
            F_or_C = input('Is this is Celius of Farenheit? Please type "C" or "F": ').upper()
            if F_or_C == "C":
                T = Temperature + 273.15
                valid = True
            elif F_or_C == "F":
                T = ((Temperature - 32) * 5/9) + 273.15
                valid = True
            else:
                print('Please enter a valid response')


        final_effusion_rate = effusion_rate(T, mm)
        print(f'The effusion rate from the values given is {final_effusion_rate}')

## Option 7
    elif integer == 7:
        while True:              
            try:
                valid = False
                while not valid:
                    mass = float(input('What is the given mass in grams? '))
                    if mass > 0:
                        valid = True
                    else:
                        print('There can be no negative numbers, please type a positive number. ')
                break
            except:
                print('That is not a valid number. Please try again.')

        while True:
            try:
                valid = False
                while not valid:
                    volume = float(input('What is the given volume in liters? '))
                    if volume > 0:
                        valid = True
                    else:
                        print('Please enter a valid number for the volume')
                break
            except:
                print('That is not a valid number. Please try again.')
        density = round(density_from_mass_and_volume(mass, volume), 5)
        print(f'The density from the values given is {density}')


## Option 8
    elif integer == 8:
        while True:
            try:
                valid = False
                while not valid:
                    atomic_number = int(input('What is the atomic number of the atom from which the photon comes? '))
                    if atomic_number <= 0:
                        print('The atomic number should be between a range of 1-118. Please enter a valid number: ')
                    elif atomic_number > 118:
                        print('The atomic number should be between a range of 1-118. Please enter a valid number: ')
                    elif atomic_number > 0 and atomic_number < 119:
                        valid = True
                break
            except:
                print('That is not a valid number. Please enter a single digit number: ')
        
        while True:
            try:
                valid = False
                while not valid:
                    orbital = int(input('What is the orbital number which was hit by the photon? '))
                    if orbital > 0 and orbital < 8:
                        valid = True
                    else:
                        print('The orbital number should be between the range 1-7. Please enter a valid number: ')
                break
            except:
                print('That is not a valid number. Please enter a single digit number: ')
                        
        energy = energy_of_photon_from_orbitals(atomic_number, orbital)
        print(f'The energy of the photon absorbed is {energy}.' )


## Option 9
    elif integer == 9:
        while True:
            try:
                valid = False
                while not valid:
                    wavelength = float(input('What is the wavelength of the photon? '))
                    if wavelength > 0:
                        valid = True
                    else:
                        print('That is not a valid input for the wavelength of a photon. Please try again. ')
                break
            except:
                print('That is not a valid input. Please enter a number. ')

        energy = energy_of_photon(wavelength)
        print(f'The energy for a photon with the given wavelength is {energy}.')


## Option 10
    elif integer == 10:
        while True:
            try:
                E = float(input('What is the energy of the photon given? '))
                if E < 0:
                    E = E * -1
                else:
                    E = E

                break
            except:
                print('That is not a valid input. Please enter all numbers. ')

        wavelength = wavelength_of_photon(E)
        print(f'The wavelength of the photon with the given energy is {wavelength}')



## Option 11
    elif integer == 11:
        while True:
            try:
                valid = False
                while not valid:
                    speed = float(input('What is speed of the energy? '))
                    if speed > 0:
                        valid = True
                    else:
                        print('That is not a valid speed. Please enter a positive speed. ')
                break
            except:
                print('That is not a valid input. Please enter number. ')

        while True:
            try:
                valid = False
                while not valid:
                    M = float(input('What is the given mass in grams? '))
                    if M > 0:
                        valid = True
                    else:
                        print('There can be no negative numbers, please type a positive number. ')
                break
            except:
                print('That is not a valid number. Please try again.')
        wavelength = wavelength_from_mass(M, speed)
        print(f'The wavelength from the given inputs is {wavelength}.')

## Option 12
    elif integer == 12:
        while True:
            try:
                valid = False
                while not valid:
                    wavelength = float(input('What is the wavelength of the photon? '))
                    if wavelength > 0:
                        valid = True
                    else:
                        print('That is not a valid input for the wavelength of a photon. Please try again. ')
                break
            except:
                print('That is not a valid input. Please enter a number. ')

        while True:
            try:
                valid = False
                while not valid:
                    speed = float(input('What is speed of the energy? '))
                    if speed > 0:
                        valid = True
                    else:
                        print('That is not a valid speed. Please enter a positive speed. ')
                break
            except:
                print('That is not a valid input. Please enter number. ')

        mass = mass_from_wavelength(wavelength, speed)
        print(f'The mass of the wave from the given values is {mass}.')

## Option 13
    elif integer == 13:
        while True:
            try:
                valid = False
                while not valid:
                    volume = float(input('What is the given volume in liters? '))
                    if volume > 0:
                        valid = True
                    else:
                        print('Please enter a valid number for the volume')

                break
            except:
                print('That is not a valid number. Please try again.')

        while True:
            try:
                valid = False
                while not valid:
                    moles = float(input('What is the given moles? '))
                    if moles > 0:
                        valid = True
                    else:
                        print('Please enter a valid number of moles')
                break
            except:
                print('That is not a valid number. Please try again. ')
        M = molarity(moles, volume)
        print('')
        print(f'The molarity from the given values is {M}')

## Option 14
    elif integer == 14:
        main_2()
        

## Option 15
    elif integer == 15:
        molar_mass = None
        grams = None
        molar_mass = float(input('What is the molar mass of the compound? '))
        # Recieve grams from user
        grams = float(input('How many grams of the existing formula is there? '))

        moles_rounded = molesformula(grams, molar_mass)
        print('')
        print(f'There are {moles_rounded} moles of your molecule')





# Functions for each formula needed
def volume_of_gas(n,T,P):
    #-V = nRT/P
    volume = round((n * T * 0.08206) / P, 5)
    return volume

def pressure_of_gas(n,T,V):
    #-P = nRT/V
    P = round((n * 0.08206 * T) / V, 5)

    return P

def moles_of_gas(P,V,T):
    #-n = PV/RT
    n = round((P * V) / (0.08206 * T), 5)

    return n

def density_of_gas(P,mm,T):
    #-D = (P*mm)/RT
    top_half = P * mm
    bottom_half = 0.08206 * T
    density = round(top_half/bottom_half, 5)
    return density

def kinetic_energy_of_gas(T):
    #-Ke = 3/2*RT
    Kinetic_energy = round((3 * 8.3145 * T) / 2, 5)

    return Kinetic_energy

def effusion_rate(T,mm):
    #-Urnm = Squareroot(3RT/mm)
    Urnm = math.sqrt((3 * 8.3145 * T)/(mm / 1000))
    rounded_Urnm = round(Urnm, 5)

    return rounded_Urnm

def density_from_mass_and_volume(M,V):
    #-D = M/V
    Density = round(M/V, 5)

    return Density

def energy_of_photon_from_orbitals(z,n):
    #-En = 2.31*10^-19(z/n)^2
    En = (2.31 * (10**-19)) * (z/n)**2
    return En

def energy_of_photon(wavelength):
    #-E = hc/v
    E = (6.626 * (10**-34)) * (3 * (10**8)) / wavelength

    return E

def wavelength_of_photon(E):
    #-v = hc/|E|
    v = (6.626 * (10**-34)) * (3 * (10**8)) / E

    return v

def wavelength_from_mass(M, c):
    #-v = h/mc
    v = (6.626 * (10**-34)) / (M * c)

    return v

def mass_from_wavelength(v, c):
    #-m = h/vc
    Mass = (6.626 * (10**-34)) / (v * (3 * (10**8)))

    return Mass

def molarity(n,V):
    #-M = n/V
    M = round(n/V, 5)

    return M

def main_2():
    while True:
        try:
            # Get Formula from user
            formula_from_user = input('Type the formula of a molecule in this format: '
            '(Element symbol#, H2O) ')

            # Functions to get the molar mass
            parsed_formula = parse_formula(formula_from_user)
            molar_mass_of_formula = molar_mass(parsed_formula)
            molar_mass_rounded = round(molar_mass_of_formula, 5)

            print(f'The molar mass from the given formula {formula_from_user} is {molar_mass_rounded}.')

            break
        # The exceptions for FormulaError and ValueError
        except FormulaError as ex:
            print(f'There is an error in the formula given: {ex.args[1]}')
            spacer = '                                        '
            for i in range(0,ex.args[2]):
                spacer += ' '
            print(f'{spacer}^')
        except ValueError as ex:
            print(f'You entered an invalid value.')

            return molar_mass_rounded
        

def molesformula(g, mm):
    x = g/mm
    moles_rounded = round(x, 5)

    # Print Statement showing moles
    return moles_rounded


# Calling the function
yes_no = input('Welcome to the Chemisty Calculator! To exit type "Q" to continue type anything else: ').upper()
while yes_no != "Q":
    main()
    yes_no = input('To exit type "Q" to run the calculator again type anything else: ').upper()
    print()
    print()
    print()
    print()