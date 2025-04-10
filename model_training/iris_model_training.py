import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load the iris dataset
iris = load_iris()
x, y = iris.data, iris.target

# Train the data on the Random Forest Classifier
model = RandomForestClassifier()
model.fit(x,y)

# Save the trained model
joblib.dump(model, 'model.joblib')