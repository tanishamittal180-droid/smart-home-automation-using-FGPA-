import pandas as pd
import random
import time
import os

os.makedirs("simulation",exist_ok=True)

file="simulation/status.csv"

if not os.path.exists(file):

    df=pd.DataFrame({
        "Time":[0],
        "Light":[0],
        "Fan":[0],
        "AC":[0],
        "Alarm":[0],
        "Energy":[0]
    })

    df.to_csv(file,index=False)

counter=0

while True:

    counter+=1

    motion=random.randint(0,1)
    temp=random.randint(0,1)
    door=random.randint(0,1)

    light=1 if motion else 0
    fan=1 if temp else 0
    ac=1 if temp else 0
    alarm=1 if door else 0
    energy=0 if motion else 1

    row=pd.DataFrame({

        "Time":[counter],
        "Light":[light],
        "Fan":[fan],
        "AC":[ac],
        "Alarm":[alarm],
        "Energy":[energy]

    })

    old=pd.read_csv(file)

    updated=pd.concat(
        [old,row],
        ignore_index=True
    )

    if len(updated)>50:
        updated=updated.tail(50)

    updated.to_csv(
        file,
        index=False
    )

    time.sleep(1)