from termcolor import cprint
from time import sleep
hackathon = int(input('How many hackathons you want to input to sort?\n'))


i = 0
n = 1
Hackathons_lists = []
while(hackathon > i):
    user = input('Name of ' f"{n}" ' hackathon?\n')
    Hackathons_lists.append(user)
    n += 1
    hackathon -= 1

print('\n')
sorted_list = sorted(Hackathons_lists)
cprint('Sorting list', 'yellow')
sleep(2)
print('\n')
cprint('Result:', 'yellow')
for i in sorted_list:
    cprint(i, 'magenta')
