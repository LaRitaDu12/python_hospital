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

Confusion matrix : ![cf_matrix](https://user-images.githubusercontent.com/72661948/144827288-0046fb0e-ff3f-4b94-b0b9-fbbca6803b67.png)
