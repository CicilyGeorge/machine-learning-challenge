import pandas as pd


df = pd.read_csv("exoplanet_data.csv")
# Drop columns with column name having err
df = df[df.columns.drop(list(df.filter(regex='err\d$')))].reset_index(drop=True)


# Set features. This will also be used as your x values.
data = df.values
X = data[:, 1:21]
y = data[:, 0]


# # Create a Train Test Split
# Use `koi_disposition` for the y values
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)


# # Pre-processing
# Scale the data using the MinMaxScaler and perform some feature selection
from sklearn.preprocessing import StandardScaler
# Create a StandardScater model and fit it to the training data
X_scaler = StandardScaler().fit(X_train)
# Transform the training and testing data using the X_scaler
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)