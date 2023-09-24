import pandas as pd
import os
import pickle
from datetime import datetime

def to_dataframe(obj):
    """Attempt to convert an object to a DataFrame, returning None if not possible."""
    if isinstance(obj, pd.DataFrame):
        return obj
    try:
        return pd.DataFrame(obj)
    except:
        return None

def save_objects(*objects, directory="."):
    """
    Save multiple objects. All objects are saved as .pkl. If convertible to DataFrame, also save as .csv.

    Parameters:
    - *objects: One or more Python objects.
    - directory: The directory in which to save the files (default is current directory).
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    for i, obj in enumerate(objects):
        base_filename = os.path.join(directory, f"object_{i}_{timestamp}")

        # Save as PKL
        with open(f"{base_filename}.pkl", 'wb') as file:
            pickle.dump(obj, file)
        
        # Try to save as CSV
        df = to_dataframe(obj)
        if df is not None:
            df.to_csv(f"{base_filename}.csv", index=False)

# Example usage:
# data = [1, 2, 3]
# array = [[1, 2], [3, 4]]
# save_objects(data, array)
