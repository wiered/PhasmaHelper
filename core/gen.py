import lists
import json

print("MainWindow.checkers = {")
for evd in lists.evidences:
    evds = evd.replace(" ", "_")
    print(f'    "{evds}": False')
print("}")