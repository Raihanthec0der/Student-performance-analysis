import pandas as pd 
df = pd.read_csv('students.csv')
df.head()
df.describe()
df["Total"]= df["Math"] + df["Physics"] + df["Programming"]
df["Average"]= df["Total"]/3
top_student =df.loc[df["Average"].idxmax()]
print("Top Student:")
print(top_student)
department_avg = df.groupby("Department")["Average"].mean()
print("\nAverage Score by Department:") 
print(department_avg)
df_sorted = df.sort_values(by="Average", ascending=False)
print(df_sorted[["Name", "Average"]])
import matplotlib.pyplot as plt
df.plot(x="Name", y="Average", kind="bar", color="skyblue")
plt.show()