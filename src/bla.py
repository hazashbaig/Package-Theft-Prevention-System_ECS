import json

while choice != 0:
    choice = int(input("Enter choice: "))
    if (choice == 1):
        with open('data.json', 'r') as f:
            data = json.load(f)
            print(data)
    if (choice == 2):
        json_data = {"Student": "21bce6969",
        "phone":"123456789",
        "Orders": ["hahahhaahhahahahahah"]}
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        data.append(json_data)

        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)