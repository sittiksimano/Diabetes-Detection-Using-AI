import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("C:\\Users\HP\Desktop\diabetes_data.csv")
X = df.drop('Outcome', axis=1)
y = df['Outcome']

imp = SimpleImputer()
X = imp.fit_transform(X)
scaler = StandardScaler()
X = scaler.fit_transform(X)

clf = LogisticRegression()
clf.fit(X, y)

preg = int(input("Enter the number of pregnancies: "))
gluc = int(input("Enter the glucose concentration: "))
bp = int(input("Enter the blood pressure: "))
skin = int(input("Enter the skin thickness: "))
insulin = int(input("Enter the insulin level: "))
bmi = float(input("Enter the BMI: "))
dpf = float(input("Enter the Diabetes Pedigree Function: "))
age = int(input("Enter the age: "))

user_data = [[preg, gluc, bp, skin, insulin, bmi, dpf, age]]
user_data = imp.transform(user_data)
user_data = scaler.transform(user_data)
prediction = clf.predict(user_data)[0]
if prediction == 0:
    output = "You do not have diabetes."
else:
    output = "You have diabetes."

print(output)
with open("output.txt", "w") as f:
    try:
        f.write(f"Number of pregnancies: {preg}\n")
        f.write(f"Glucose concentration: {gluc}\n")
        f.write(f"Blood pressure: {bp}\n")
        f.write(f"Skin thickness: {skin}\n")
        f.write(f"Insulin level: {insulin}\n")
        f.write(f"BMI: {bmi}\n")
        f.write(f"Diabetes Pedigree Function: {dpf}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Prediction: {output}\n")
    finally:
        f.close()