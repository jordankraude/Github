import urllib.request
from yes_no_validater_class import Yes_No_validater

validate = Yes_No_validater()

def main():
    yes_or_no = validate.validate_input("Would you like to test the connection of a website?")
    #while self.correct_input:
    #    yes_or_no = self.validate_input()

    if yes_or_no == "YES":
        print( 'connected' if connect() else 'no internet!' )

    else:
        print('Have a good day')


def connect ():
    try:
        host = input('What is the URL of the website you wish to check? ')
        urllib.request.urlopen(host)
        return True
    except:
        return False

main()