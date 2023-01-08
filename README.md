# Diabetes-Detection-Using-AI (logistic-regression)

Before using change the csv file path in the program. Otherwise the model won't work.

# Introduction

Diabetes, one of the most common illnesses in the world, can be prevented from progressing and causing secondary problems if discovered early. In this project, we develop a prediction model that predicts if a patient has diabetes based on certain diagnostic parameters in the dataset, and we investigate several ways to improve the model's performance and accuracy.


# Project Goal:


The model is trained on a dataset that contains various features such as the number of pregnancies, glucose concentration, blood pressure, skin thickness, insulin level, BMI, DPF, and age, as well as a target column indicating whether the person has diabetes or not. The model uses this training data to learn how to make predictions on new data. The goal of the model is to accurately predict whether a person has diabetes or not based on the input features provided.


# Algorithm:

Logistic regression is a data analysis technique that uses mathematics to find the relationships between two data factors. It then uses this relationship to predict the value of one of those factors based on the other. The prediction usually has a finite number of outcomes, like yes or no. 

It makes predictions based on historical data. This involves identifying a business question and collecting relevant data, training a regression analysis model using the data, and making predictions for unknown values using the trained model. Use an equation to connect different data points and make predictions for unknown values.


#T ools & Technologies :



For simulation Environment: Pycharm
Language : Python
Libraries Used:  A)  Sklearn:  for Logistic Regression and scaling data for training the model.  
		    B) Pandas:  for reading and manipulate data inside the csv file and user data input.

# How it work? 
1. The pandas library is imported and used to read in the diabetes data from a CSV file.
2. The data is split into the feature variables (X) and the target variable (y).
3. The SimpleImputer class from the sklearn library is imported and used to replace any missing values in the feature variables with the mean value.
4. The StandardScaler class from sklearn is imported and used to scale the feature variables so that they have a mean of 0 and a standard deviation of 1.
5. The LogisticRegression class from sklearn is imported and used to fit a logistic regression model to the scaled feature variables and target variable.This means that the model is being trained to learn the relationship between the input feature variables (scaled X) and the target variable in order to make predictions about whether a patient has diabetes or not.
6. The user is prompted to input their own values for the feature variables.
7. The user's input is transformed using the SimpleImputer and StandardScaler objects to ensure it is in the same format as the training data.
8. The logistic regression model is used to predict the outcome (diabetes or no diabetes) based on the user's input.
9. The prediction is output to the user and also written to a text file along with the user's input values.

# Program Output
![image](https://user-images.githubusercontent.com/24763414/211219709-cc942f33-e395-4e9f-8ca5-1b3c4cb0af0b.png)
![image](https://user-images.githubusercontent.com/24763414/211219720-4781dad9-65c2-422e-bd9b-08ec94ab8aa2.png)
![image](https://user-images.githubusercontent.com/24763414/211219731-18f0b483-5fd3-4d46-87e6-d01c0d88f6ee.png)

