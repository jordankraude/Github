import urllib.request
def main():
    connectivity()
    valid = False
    while not valid:
        again = input('Would you like to test the connectivity of another website? Please type YES or NO: ').upper()
        if again != 'yes' or 'no':
            print('Please type "YES" or "NO": ')
            valid = False   
        else:
            valid = True

def connectivity():
    valid = False
    while not valid:
        again = input('Would you like to find the connectivity of a website? Please type YES or NO: ')
        if again != 'yes' or 'no':
            print('Please type "YES" or "NO": ')
            valid = False   
        else:
            def connect ():
                try:
                    host = input('What is the URL of the website you wish to check? ')
                    urllib.request.urlopen(host)
                    return True
                except:
                    return False

                print( 'connected' if connect () else 'no internet!' )
            valid = True
        break    


main()