import os
from config import db
from models import Avocado

# Data to initialize database with
AVOCADO = [

    {'regionid':1,
    'avgprice':50000,
    'totalvol':50, 
    'avo_a':10 ,
    'avo_b':20 , 
    'avo_c':30 , 
    'type':1,}
    
]

# Delete database file if it exists currently
if os.path.exists('task.db'):
    os.remove('task.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for avocado in AVOCADO:
    
    av = Avocado(
        regionid = avocado['regionid'],
        avgprice=avocado['avgprice'], 
                totalvol=avocado['totalvol'],
                avo_a=avocado['avo_a'], 
                avo_b=avocado['avo_b'], 
                avo_c=avocado['avo_c'], 
                type=avocado['type'])
    db.session.add(av)

db.session.commit()