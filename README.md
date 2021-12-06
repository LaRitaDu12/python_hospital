# python_hospital

"dummied_full.csv"
- data is preprocessed (somewhat) (features one-hot encoded, dropped some columns...)
- target has 2 classes instead of 3 (fused >30 and <30 into "YES")


# Xgboost

"XgboostSKlearn.ipynb"
- Used an xgboost model with the pip package: pip install xgboost
- tuned parameters with Random grid search

# Results 

accuracy is 0.637902635431918 which is quite disappointing 

Confusion matrix :

![cf_matrix](https://user-images.githubusercontent.com/72661948/144829020-43de3c7d-5491-4e71-94d2-17a5cba4238d.png)


# EDIT 07/12/2021 :

"Preprocessed06_12.csv" and "Preprocessing only.ipynb"
- REpreprocessed the dataset according to https://www.hindawi.com/journals/bmri/2014/781670/

## Improved classification
"XgboostSKlearn.ipynb"
- accuracy is now 0.908669669149489

Confusion matrix :

![cf_matrix_90](https://user-images.githubusercontent.com/72661948/144938609-eb4f6de5-14a5-407e-8404-7a65a2682501.png)

