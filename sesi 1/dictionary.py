print("\nDefining and Accessing Dictionary")
MLB_team = { 
    'Colorado': 'Rockies', 
    'Boston': ['Red Sox', 'White Fox'], 
    'Minnesota': 'Twins', 
    'Seattle': 'Mariners', 
    'Kansas City': 'Royals'
}

#Adding an entry to an existing dictionary
print(MLB_team['Seattle'])

#Modify
MLB_team['Boston'][0] = 'Red Fox'
print(MLB_team['Boston'])


#Building a dictionary incrementally
print("\nBuilding a dictionary incrementally")
person = {}
person['fname'] = 'Hack'
person['lname'] = '8'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
print(person)
print(person['children'][1])
print(person['pets']['dog'])
person['pets']['cat'] = 'Renamed Sox'
print(person['pets']['cat'])