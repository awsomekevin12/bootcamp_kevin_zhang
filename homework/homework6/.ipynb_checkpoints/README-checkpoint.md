## Stage 6: Data Preprocessing Strategy

This project includes a data preprocessing pipeline to clean the raw sample dataset located in `data/raw/`. The cleaning logic is encapsulated in modular functions within `src/cleaning.py` and applied in the `stage06_data-preprocessing_homework-starter.ipynb` notebook.

### Cleaning Steps

The pipeline performs the following actions in order:

1.  **Impute Missing Values:** Missing values in the numeric columns (`age`, `income`, `score`) are filled using the **median** of each respective column. The median is used to minimize the effect of potential outliers.
2.  **Remove Sparse Rows:** Rows with less than 70% non-missing data are dropped. This step handles rows that are too incomplete to be reliable for analysis.
3.  **Normalize Numeric Features:** The `age`, `income`, and `score` columns are scaled to a range of [0, 1] using Min-Max normalization. This ensures that all features are on a common scale, which is crucial for many machine learning algorithms.

The final, cleaned dataset is saved to `data/processed/sample_data_cleaned.csv`.