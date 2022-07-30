import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "555-555-5555",
            "email": "  @gmail.com"
        },
        {
            "name": "Jane Doe",
            "phone": "555-555-5555",
            "email": "  @gmail.com"
        }
    ]
}
'''

data = json.loads(people_string)

for person in data['people']:
    print(person['name'])