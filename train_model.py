import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("data/cbc_sample.csv")

X = data[['Hb','RBC','MCV','MCH','MCHC','RDW','Age']]
y = data['Anemia']

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("models/anemia_model.pkl","wb"))
pickle.dump(scaler, open("models/scaler.pkl","wb"))

print("Model Trained & Saved Successfully")
