# NO2 Reproducibility Dataset
This repository provides a dataset and code to reproduce the NO2 time-series prediction results for Tai Po, Hong Kong (2017–2019).

## Data
File: `data/NO2_demoDataset.csv`
The dataset includes:
- Observed NO2 concentrations  
- Model predictions from:
  - SARIMAX  
  - LSTM  
  - Prophet  
  - ARIMA-GARCH  

## Variables
- `date` — observation date  
- `NO2` — measured NO2 concentration (μg/m³)  
- `sarimax` — SARIMAX model prediction  
- `lstm` — LSTM model prediction  
- `prophet` — Prophet model prediction  
- `arima_garch` — ARIMA-GARCH model prediction  

## Data Processing
- A **30-day rolling mean** was applied to smooth the time series  

## Reproducibility
To reproduce the figure:
1. Open the dataset in Python  
2. Run the script in `code/NO2_demoCode.py`  
3. The generated figure will be saved in the `figure/` folder  

## Output
- `figure/example_plot.png` — reproduced time-series plot  

## Note
This dataset is provided for **demonstration and reproducibility purposes only** and may represent a simplified version of the original research data.

## Author
Prepared as part of a research data management and reproducibility exercise.
