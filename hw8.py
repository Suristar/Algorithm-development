import pandas as pd
#Data 1
df = pd.read_csv("c:/users/surajit/desktop/data-1.csv")
df.head()


df[1] = ((df['var1'] - (-10))**2) + ((df['var2'] - (-4.25))**2)
df[2] = ((df['var1'] - (-6.3))**2) + ((df['var2'] - (-8.6))**2)
df[3] = ((df['var1'] - (-1.14))**2) + ((df['var2'] - (4.23))**2)

df['class'] = df[[1, 2, 3]].idxmin(axis=1)

from matplotlib import pyplot as plt

plt.scatter(df['var1'], df['var2'], c=df['class'])
plt.show()


#Data 2
df = pd.read_csv("c:/users/surajit/desktop/data-2.csv")
df.head()

df[1] = ((df['var1'] - (20))**2) + ((df['var2'] - (1))**2)
df[2] = ((df['var1'] - (21.4))**2) + ((df['var2'] - (17.5))**2)
df[3] = ((df['var1'] - (28.5))**2) + ((df['var2'] - (22.2))**2)

df['class'] = df[[1, 2, 3]].idxmin(axis=1)

plt.scatter(df['var1'], df['var2'], c=df['class'])
plt.show()


#Data 3
df = pd.read_csv("c:/users/surajit/desktop/data-3.csv")
df.head()

from matplotlib import pyplot as plt

df[1] = ((df['var1'] - (90.2))**2) + ((df['var2'] - (128.7))**2)
df[2] = ((df['var1'] - (130.5))**2) + ((df['var2'] - (156.8))**2)
df[3] = ((df['var1'] - (186.7))**2) + ((df['var2'] - (185))**2)

df['class'] = df[[1, 2, 3]].idxmin(axis=1)

plt.scatter(df['var1'], df['var2'], c=df['class'])
plt.show()