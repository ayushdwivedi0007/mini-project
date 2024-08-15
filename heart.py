import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import tkinter as tk
from tkinter import messagebox

# Define the path to the data file
data_file = 'C:/Users/DELL/Documents/data.csv'

# Load and process the dataset
if not os.path.exists(data_file):
    print(f"Error: {data_file} file not found.")
else:
    heart_data = pd.read_csv(data_file)
    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    # Train the logistic regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)

    # Define the GUI application
    class HeartDiseasePredictor(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title("Heart Disease Predictor")
            self.geometry("400x400")

            # Create input fields for each feature
            self.entries = {}
            feature_names = X.columns
            for idx, feature in enumerate(feature_names):
                label = tk.Label(self, text=feature)
                label.grid(row=idx, column=0, padx=10, pady=5)
                entry = tk.Entry(self)
                entry.grid(row=idx, column=1, padx=10, pady=5)
                self.entries[feature] = entry

            # Create predict button
            self.predict_button = tk.Button(self, text="Predict", command=self.predict)
            self.predict_button.grid(row=len(feature_names), column=0, columnspan=2, pady=20)

        def predict(self):
            # Get input data from entries
            input_data = []
            try:
                for feature in X.columns:
                    value = float(self.entries[feature].get())
                    input_data.append(value)

                # Convert input data to numpy array
                input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)

                # Make prediction
                prediction = model.predict(input_data_as_numpy_array)
                if prediction[0] == 0:
                    messagebox.showinfo("Result", "The person does not have heart disease.")
                else:
                    messagebox.showinfo("Result", "The person has heart disease.")
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numerical values for all fields.")

    # Create and run the GUI application
    app = HeartDiseasePredictor()
    app.mainloop()
