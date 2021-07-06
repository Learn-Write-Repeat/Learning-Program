# Breast Cancer Classification using Supervised Machine Learning  

* **Team**: tp-june-ml-3

* **Mentor**: Ms. Samiksha Bhavsar <a href="https://www.linkedin.com/in/samiksha-bhavsar-33837417a"><img width=80px src="https://user-images.githubusercontent.com/50140975/124541137-6f34c500-de3e-11eb-86bb-38abcac5011e.png"></a> 

* **Team Members**: 
	1. Ms. Jyotsana Kumari Gupta - Performed Data preprocessing and Exploratory Data Analysis. <a href="https://www.linkedin.com/in/jyotsana-kumari-gupta-404814196"><img width=80px src="https://user-images.githubusercontent.com/50140975/124541137-6f34c500-de3e-11eb-86bb-38abcac5011e.png"></a> 
	2. Mr. Samnit Mehandiratta - Model Fitting and Prediction and GitHub Documentation. <a href="https://www.linkedin.com/in/lankabhedi"><img width=80px src="https://user-images.githubusercontent.com/50140975/124541137-6f34c500-de3e-11eb-86bb-38abcac5011e.png"></a> 

* **Problem statement**: To classify tumors into Malignant and Benign based on the given features.

* **Libraries Used**: Sklearn, Seaborn, Matplotlib, Pandas, Numpy

<img width=100px src=https://user-images.githubusercontent.com/50140975/124541682-8e802200-de3f-11eb-9b8a-f78129c77a14.png><img width=100px src=https://user-images.githubusercontent.com/50140975/124541707-993ab700-de3f-11eb-8ff0-9270ba0a13ab.png><img width=100px src=https://user-images.githubusercontent.com/50140975/124541723-a48de280-de3f-11eb-901a-9db66df801bc.png><img width=100px src=https://user-images.githubusercontent.com/50140975/124541763-b8d1df80-de3f-11eb-8a0f-ddc34b4dc979.png><img width=100px src=https://user-images.githubusercontent.com/50140975/124541790-c4bda180-de3f-11eb-8755-abbd6246ae6b.png>





* **Important Insights derived from EDA**:
	1. There are total 31 columns and 569 rows.
	2. Target column is diagnosis which is 0 for benign and 1 for a malign tumor.
	3. The dataset is clean and has no null values.
	4.  The pairplot shows that malignant and benign tumors are easily discernable based on the given features. Although there were some scattergraphs in which there was not any distinguishability, they are still kept as is in the model training.
	5. The countplot showed that the data set is imbalanced.  
	6. The heatmap showed high correlation of mean-radius and the diagnosis.
	7. Similar correlation was shown with other features.
	8. It was decided that all the features will be taken into consideration in model training.

* **Different algorithms fitted**: 
```markdown
| Algorithm Name         | Accuracy Score (%) |
|------------------------|--------------------|
| Logistic Regression    | 98.25              |
| kNN                    | 97.37              |
| Decision Tree          | 96.49              |
| Hist Gradient Boosting | 98.25              |
| Random Forest          | 98.25              |
| Ada Boost              | 99.12              |
| XGBoost                | 98.25              |
| LightGBM               | 99.12              |
```
![image](https://user-images.githubusercontent.com/50140975/124541524-39dca700-de3f-11eb-8152-718dd08f9367.png)


* **Final Model**: The final model chosen is Adaboost or LightGBM because of the highest accuracy i.e. 99.12%

![image](https://user-images.githubusercontent.com/50140975/124541507-2fbaa880-de3f-11eb-9bba-14721104d1a3.png)



