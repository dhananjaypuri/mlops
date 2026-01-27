## Create 3 groups of customer Small Buyers , Medium buyers and Premium Buyers
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score


customer_data = {
    "customer_name": [
        "Alice Chen", "Marcus Wright", "Sarah Jenkins", "Leo Tanaka", "Elena Rodriguez",
        "David Smith", "Priya Sharma", "Gary Wilson", "Isabella Rossi", "James O'Connor"
    ],
    "age": [28, 45, 32, 21, 38, 54, 29, 61, 35, 42],
    "spending": [150.50, 1200.00, 430.25, 85.00, 920.10, 55.40, 310.00, 15.20, 740.00, 510.75]
};

df = pd.DataFrame(customer_data);

X = df[['age', 'spending']];

scaler = StandardScaler();

X_scaled = scaler.fit_transform(X);

model = KMeans(n_clusters=3, random_state=42, n_init=10);

df['Group'] = model.fit_predict(X_scaled);
print(df);
result = model.predict(scaler.transform([[28, 800]]));

print(result[0]);

sil_score = silhouette_score(X_scaled, df['Group'])

centers = scaler.inverse_transform(model.cluster_centers_);

df_center = pd.DataFrame(centers, columns=['avg_age', 'avg_spending'])
df_center['cluster'] = df_center.index;

df_center = df_center.sort_values('avg_spending');

df_center = df_center.reset_index();

cluster_map = {df_center.iloc[0,3]: "Small Buyer",
               df_center.iloc[1,3]: "Medium Buyer",
               df_center.iloc[2,3]: "Premium Buyer"};

print(f"User is {cluster_map[result[0]]}");
print(f'Silhouette Score: {sil_score}')