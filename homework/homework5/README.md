## Data Storage

This project follows a structured approach to data storage to ensure reproducibility and clarity.

### Folder Structure

-   `data/raw/`: Contains original, immutable data as downloaded or received. In this project, it's used for storing data in CSV format, which is human-readable and a common exchange format.
-   `data/processed/`: Contains cleaned, transformed, and feature-engineered data ready for analysis or modeling. Data here is stored in Parquet format for efficiency.

### File Formats

-   **CSV (.csv)**: Used for raw data in `data/raw/`. It's a universal and human-readable format.
-   **Parquet (.parquet)**: Used for processed data in `data/processed/`. This columnar format is highly efficient for storage and analytical queries, as it offers excellent compression and preserves data types (e.g., dates, numbers), which prevents errors during loading.