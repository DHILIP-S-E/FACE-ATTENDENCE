import pickle
import numpy as np

# Load face data and labels
with open('data/names.pkl', 'rb') as w:
    LABELS = pickle.load(w)
with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

print('Shape of Faces matrix --> ', FACES.shape)
print('Number of labels --> ', len(LABELS))

# Ensure consistency between FACES and LABELS
num_samples = FACES.shape[0]
num_labels = len(LABELS)

if num_samples != num_labels:
    print(f"Mismatch in number of samples: FACES has {num_samples} samples but LABELS has {num_labels} labels.")
    
    # Synchronize data
    if num_samples < num_labels:
        LABELS = LABELS[:num_samples]
    else:
        FACES = FACES[:num_labels]
    
    # Save synchronized data
    with open('data/names.pkl', 'wb') as w:
        pickle.dump(LABELS, w)
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(FACES, f)
    
    print("Data synchronized.")
else:
    print("Data is already synchronized.")
