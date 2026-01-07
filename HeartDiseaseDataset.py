# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
# Source: https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "heart_failure_clinical_records_dataset.csv"


# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "andrewmvd/heart-failure-clinical-data",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

# Create csv file from dataframe
df.to_csv("HeartDisease/heart_failure_clinical_records_dataset.csv", index=False)