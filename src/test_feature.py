from src.data_loader import load_data
from src.feature_engineering import create_features


df = load_data()

print("Original:")
print(df.shape)


df = create_features(df)


print("\nAfter Feature Engineering:")
print(df.shape)


print("\nColumns:")
print(df.columns.tolist())