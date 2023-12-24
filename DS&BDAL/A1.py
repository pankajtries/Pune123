import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

missing_values = titanic.isnull().sum()
data_description = titanic.describe()
variable_descriptions = titanic.dtypes
data_dimensions = titanic.shape

print("Step 4: Data Preprocessing - Missing Values:\n", missing_values)
print("\nData Description:\n", data_description)
print("\nVariable Descriptions:\n", variable_descriptions)
print("\nData Dimensions:\n", data_dimensions)

variable_types_before_conversion = titanic.dtypes
titanic['age'] = pd.to_numeric(titanic['age'], errors='coerce')

titanic['sex'] = pd.Categorical(titanic['sex']).codes

print("\nStep 5: Variable Types before Type Conversion:\n", variable_types_before_conversion)
print("\nDataFrame after Type Conversion:\n", titanic.sample(5))