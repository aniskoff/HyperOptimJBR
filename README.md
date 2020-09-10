# Hyperparameter analyzer


This repository contains the solution of the second test problem for **Data-driven hyper-optimization**
 *JetBrains Research* autumn internship.  

####<ins>**Important**</ins>: You should run this application on *Python 3.5+* 
####(because code is using new features of Python AST Library).

 
### Description of how the app works:  

- File `src/main/python/hyperparams_extractor/hyperparams_extractor.py` contains class
 `HyperparamsExtractor` which has the functionality to bypass AST and treat
 keyword arguments inside constructor of ML model as model hyperparameters.
 
- The collected data about the hyperparameters is written to the JSON file located at the following
path: `src/main/resources/result/result.json`.  
- The result will be written in JSON in the following format:
```json
[
  {
    "XGBRegressor": {"objective": "reg:linear", "colsample_bytree": 0.5, "learning_rate": 0.0001, "n_estimators": 10}
  },
  {
    "SVR": {"kernel": "poly", "C": 100, "gamma": "auto", "degree": 3, "epsilon": 0.1, "coef0": 1}
  },
  {
    "XGBRegressor": {"objective": "reg:linear", "colsample_bytree": 0.3, "learning_rate": 0.1, "max_depth": 5, "alpha": 10, "n_estimators": 10}
  }
]
```

- File `src/main/python/hyperparams_analyzer/hyperparams_analyzer.py` contains class
 `HyperparamsAnalyzer` which has the functionality to read the JSON file of the format 
shown above, calculate the required statistics (*mean*, *std*, *min*, *max*) using the [Pandas](https://pandas.pydata.org/) library 
and then output the result to the console as table.

- The result will be output to the console in the following format:
```text
------------------------- Stats for XGBRegressor model -------------------------
      colsample_bytree  learning_rate  n_estimators  max_depth  alpha
mean          0.400000        0.05005          10.0        5.0   10.0
std           0.141421        0.07064           0.0        NaN    NaN
min           0.300000        0.00010          10.0        5.0   10.0
max           0.500000        0.10000          10.0        5.0   10.0

```

### Installation
  
    `pip3 install -r requirements.txt`  
 

### Run Hyperparameters Extractor as script from the repository root
    `python3 -m src.main.python.hyperparams_extractor.hyperparams_extractor`

### Run Hyperparameters Analyzer as script from the repository root
    `python3 -m src.main.python.hyperparams_extractor.hyperparams_extractor`

### Run tests for Hyperparameters Extractor:

`python3 -m pytest`
