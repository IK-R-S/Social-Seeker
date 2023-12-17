from app import Application
from components import *
from time import sleep

# Starting app
app = Application()
option = None

while True:
    Components.clearConsole()
    print('Social Seeker - alpha\n')
    sleep(0.5)
    print('[1] Standard search')
    sleep(0.1)
    print('[2] Keyword search')
    sleep(0.1)
    print('[3] Info')
    sleep(0.1)
    print('[0] Exit')
    sleep(0.5)
    option = int(input('\n» '))
    if option == 0:
        Components.clearConsole()
        break
    elif option == 1:
        Components.clearConsole()
        #print(f'Searching for {person} on the web...')
        print(app.start_STANDARD()['websites'])
        break
    elif option == 2:
        Components.clearConsole()
        print(app.start_ADVANCED())
        break    
