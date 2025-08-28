import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

data = pd.read_csv("gesture_dataset_clean.csv", header=None)

X = data.iloc[:, 1:]  
y = data.iloc[:, 0]   

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

accuracy = knn.score(X_test, y_test)
print(f"Model trained. Test accuracy: {accuracy*100:.2f}%")

joblib.dump(knn, "gesture_model(final).pkl")
print("Trained model saved as 'gesture_model(final).pkl'")
