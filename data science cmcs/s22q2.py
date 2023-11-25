import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer

df = pd.read_csv('Data.csv')

# Extract the features (columns other than 'quality')
features = df.drop('quality', axis=1)

# a. Rescaling (Min-Max Scaling)
min_max_scaler = MinMaxScaler()
rescaled_data = min_max_scaler.fit_transform(features)

# b. Standardizing Data (Z-score Standardization)
standard_scaler = StandardScaler()
standardized_data = standard_scaler.fit_transform(features)

# c. Normalizing Data (L2 Normalization)
normalizer = Normalizer()
normalized_data = normalizer.fit_transform(features)

# Print the first few rows of each transformed dataset
print("Rescaled Data:")
print(pd.DataFrame(rescaled_data, columns=features.columns).head())

print("\nStandardized Data:")
print(pd.DataFrame(standardized_data, columns=features.columns).head())

print("\nNormalized Data:")
print(pd.DataFrame(normalized_data, columns=features.columns).head())
