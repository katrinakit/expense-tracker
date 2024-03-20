#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#
import json

expenses_file = open ('expenses.json')
expenses = json.load(expenses_file)
expenses_file.close()
# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
expenses_comp=expenses.copy()
def sort_price(expenses):
    return int(expenses["sum"])

while True:
    command = input("\nChoose command:")
    if command == "1":
        expenses_write={}
        expenses_write['name']=input("please write the expenses name: ")
        expenses_write['sum']=int(input("please write the full sum: "))
        expenses_write['category']=input("please write the expenses category: ")
        expenses.append(expenses_write)
        print(expenses)
    if command == "2":
        print(expenses)
    if command == "3":
        expenses_comp.sort(key = sort_price, reverse = True)
        print(expenses_comp[0:10])
    if command == "4":
        expenses.sort(key = sort_price)
        print(expenses[0:10])
    if command == "5":
       print(expenses)
    if command == "e":
        with open ("expenses.json", "w") as outfiles:
            json.dump(expenses, outfiles)
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass

