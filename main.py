from src.preprocess import load_data, preprocess
from src.features import split_features
from src.train_model import train
from src.detect import load_model, predict
from src.alert import send_alert

# -----------------------------
# STEP 1: Load Data
# -----------------------------
df = load_data("data/raw/nsl_kdd_sample.csv")

# -----------------------------
# STEP 2: Preprocess Data
# -----------------------------
df = preprocess(df)

# -----------------------------
# STEP 3: Split Features & Labels
# -----------------------------
X, y = split_features(df)

# -----------------------------
# STEP 4: Train Model
# -----------------------------
model = train(X, y)

# -----------------------------
# STEP 5: Load Model (from file)
# -----------------------------
model = load_model()

# -----------------------------
# STEP 6: TEST BOTH CASES
# -----------------------------

print("\n--- Testing NORMAL sample ---")
normal_sample = X[y == 0].iloc[[0]]
result_normal = predict(model, normal_sample)
send_alert(result_normal)
print("Detection Result:", result_normal)

print("\n--- Testing THREAT sample ---")
threat_sample = X[y == 1].iloc[[0]]
result_threat = predict(model, threat_sample)
send_alert(result_threat)
print("Detection Result:", result_threat)