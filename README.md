# U.S. Automotive Trade Analysis

This project explores trends and patterns in U.S. automotive trade, focusing on exports, imports, tariffs, and key economic indicators. It integrates multiple datasets and applies end-to-end data cleaning, transformation, and exploratory analysis. The unified dataset supports both exploratory data analysis (EDA) and visualization, helping to reveal how trade relationships evolve over time and across trading partners.

---

## Project Structure
```
.
├── data/
│ ├── raw/ # Original unmodified datasets
│ │ ├── primary/ # Core trade data (exports/imports)
│ │ └── secondary/ # Economic indicators (GDP, tariffs)
│ └── processed/ # Cleaned and combined datasets
│
├── deepnote/
│ └── notebooks/
│ ├── Init.ipynb # Environment setup (dependencies)
│ ├── data_cleaning_primary.ipynb # Cleaning primary trade data
│ ├── data_cleaning_secondary.ipynb # Cleaning GDP and tariff data
│ ├── combine_primary_secondary.ipynb # Merge cleaned datasets
│ ├── data_analysis.ipynb # Exploratory Data Analysis (EDA)
│ └── data_visualizations.py # Reusable visualization functions
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

## Workflow Overview

The project follows a pipeline that transforms raw trade and economic data into insights through cleaning, merging, exploration, and visualization.  

### 1. Environment Setup

Install required Python packages:

`pip install -r requirements.txt`

Alternatively, run `Init.ipynb`, which installs all dependencies automatically when working in Deepnote.

---

### 2. Data Cleaning

Raw datasets are organized into:  
- Primary data: Automotive export/import data by region and country (`data/raw/primary/`)  
- Secondary data: Macroeconomic indicators including GDP and MFN tariffs (`data/raw/secondary/`)  

Run the following notebooks:  
- `data_cleaning_primary.ipynb` — cleans trade data  
- `data_cleaning_secondary.ipynb` — cleans GDP and tariff data  

Cleaned datasets are saved to `data/processed/`.

---

### 3. Combine Datasets

Merge trade and economic indicators into a unified dataset with:

- `combine_primary_secondary.ipynb`

This dataset is the foundation for downstream analysis.

---

### 4. Exploratory Data Analysis (EDA)

Perform in-depth trade and economic analysis with:

- `data_analysis.ipynb`  

Key questions explored include:  
- How have U.S. exports and imports evolved over time?  
- Which trading partners dominate U.S. automotive trade?  
- How do tariffs and macroeconomic shifts (GDP) affect trade patterns?  

---

### 5. Visualization & Reporting

Visualizations are generated using:  
- `data_visualizations.py` — reusable plotting utilities  
- Jupyter notebooks — for interactive exploration  

Key visualizations include:  
- U.S. export and import time series  
- Category-level comparisons (e.g., vehicle types)  
- Top trading partner analysis  
- Tariff and GDP impact charts
