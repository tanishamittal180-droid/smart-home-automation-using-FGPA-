import pandas as pd
from sklearn.linear_model import LinearRegression

df=pd.read_csv("simulation/status.csv")

df["Power"]=(df["Light"]*20)+(df["Fan"]*60)+(df["AC"]*120)

X=df[["Time"]]
Y=df["Power"]

model=LinearRegression()

model.fit(X,Y)

future=[[10],[11],[12],[13],[14]]

prediction=model.predict(future)

print("\nPredicted Energy Usage:\n")

for i,p in enumerate(prediction):

    print(
        f"Time {future[i][0]} : {round(p,2)} Watts"
    )