import pandas as pd

print (pd.__version__)

data = ["A", 100, "B"]

series = pd.Series(data)

print(series)

df1 = pd.DataFrame({
    "name": ["Alice", "Bob"]
})

df2 = pd.DataFrame({
    "age": [25, 30]
})

result = pd.concat([df1, df2])

print(result)