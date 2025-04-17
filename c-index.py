

# Step 2: Import necessary libraries
import pandas as pd
from lifelines.utils import concordance_index

# Step 3: Create example data
# duration: time of follow-up
# event: 1 if event occurred (death/failure), 0 if censored
# predicted_risk: output from a model (e.g., risk score; higher = higher risk)
data = pd.DataFrame({
    'duration': [5, 6, 6, 2.5, 4, 4, 3, 2, 8, 10],
    'event': [1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    'predicted_risk': [0.7, 0.3, 0.4, 0.8, 0.6, 0.65, 0.2, 0.9, 0.5, 0.1]
})

# Step 4: Calculate the Concordance Index (C-Index)
c_index = concordance_index(
    data['duration'],             # actual survival times
    -data['predicted_risk'],      # lower predicted value = longer survival (invert if higher = higher risk)
    data['event']                 # event observed flag
)

# Step 5: Display the result
print(f"C-Index: {c_index:.4f}")