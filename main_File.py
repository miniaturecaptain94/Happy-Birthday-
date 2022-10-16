import pyfiglet
from colorama import Fore
import time

time.sleep(5)
Happy = pyfiglet.figlet_format("Happy", font = "banner3-D"  )
Birthday = pyfiglet.figlet_format("Birthday", font = "banner3-D",width = 200 )
Farhan = pyfiglet.figlet_format("Farhan", font = "banner3-D",width = 200 )

print(Fore.GREEN + Happy)
time.sleep(1)
print(Fore.RED + Birthday)
time.sleep(1)
print(Fore.BLUE + Farhan)
time.sleep(30)
