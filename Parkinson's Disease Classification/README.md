# Parkinson's Disease Classification

* **Team**: tp-21-june-py-3

* **Mentor**: Ms. Tabassum Chouhan <a href="https://www.linkedin.com/in/tabassum-chouhan-99b396182/"><img width=80px src="https://user-images.githubusercontent.com/50140975/124541137-6f34c500-de3e-11eb-86bb-38abcac5011e.png"></a> 

* **Team Members**: 
	1. Ms. Rashmi Patil - Performed Data preprocessing and Exploratory Data Analysis. <a href="https://www.linkedin.com/in/rashmi-patil-b1a26b18a/"><img width=80px src="https://user-images.githubusercontent.com/50140975/124541137-6f34c500-de3e-11eb-86bb-38abcac5011e.png"></a> 
	2. Mr. Kranti Kumar Choudhury - Performed Data preprocessing. <a href="#"><img width=80px src="https://user-images.githubusercontent.com/50140975/124541137-6f34c500-de3e-11eb-86bb-38abcac5011e.png"></a>
	3. Mr. Rohit Akilaysh Vanne - Performed Data preprocessing. <a href="https://www.linkedin.com/in/rohit-akilaysh-vanne/"><img width=80px src="https://user-images.githubusercontent.com/50140975/124541137-6f34c500-de3e-11eb-86bb-38abcac5011e.png"></a>
	4. Ms. Sivani Vemuri - Model Fitting and Prediction. <a href="https://www.linkedin.com/in/sivani-vemuri-5695aa14a/"><img width=80px src="https://user-images.githubusercontent.com/50140975/124541137-6f34c500-de3e-11eb-86bb-38abcac5011e.png"></a>
	5. Mr. Samnit Mehandiratta - Model Fitting and Prediction and GitHub Documentation. <a href="https://www.linkedin.com/in/lankabhedi"><img width=80px src="https://user-images.githubusercontent.com/50140975/124541137-6f34c500-de3e-11eb-86bb-38abcac5011e.png"></a> 

* **Problem statement**: To classify individuals on the basis of the features given in the dataset.

* **Libraries Used**: Sklearn, Seaborn, Matplotlib, Pandas, Numpy

<img width=100px src=https://user-images.githubusercontent.com/50140975/124541682-8e802200-de3f-11eb-9b8a-f78129c77a14.png><img width=100px src=https://user-images.githubusercontent.com/50140975/124541707-993ab700-de3f-11eb-8ff0-9270ba0a13ab.png><img width=100px src=https://user-images.githubusercontent.com/50140975/124541723-a48de280-de3f-11eb-901a-9db66df801bc.png><img width=100px src=https://user-images.githubusercontent.com/50140975/124541763-b8d1df80-de3f-11eb-8a0f-ddc34b4dc979.png><img width=100px src=https://user-images.githubusercontent.com/50140975/124541790-c4bda180-de3f-11eb-8755-abbd6246ae6b.png>




* **Important Insights derived from EDA**:
	1. There are total 24 columns and 195 rows.
	2. Target column is status with 1 for Parkinson's and 0 for not detected.
	3. The dataset is clean and has no null values.
	4.  The pairplots show that there are very less feature columns that can be used as classification basis.
	5. The value_counts() command shows that dataset is imbalanced.  
	6. The box plot show the presence of outliers.
	7. The heatmap shows that there is not much correlation between the features and the status.
	8. It was decided that all the features will be taken into consideration in model training.
	9. Principal Component Analysis along with standardization should be used for feature enhancement and to take in the consideration of the kurtosis and skewness in the data.

* **Different algorithms fitted**: 
```markdown
| Algorithm Name         | Accuracy Score (%) |
|------------------------|--------------------|
| SVC                    | 92.31              |
| kNN                    | 97.44              |
| Random Forest          | 97.44              |
```
![image](https://user-images.githubusercontent.com/50140975/124562614-dcefe980-de5c-11eb-92a4-f27001d3caa0.png)


* **Final Model**: Both kNN and Random Forest Classifier gave the same accuracy score of 97.44%.

![image](https://user-images.githubusercontent.com/50140975/124562648-e8431500-de5c-11eb-8a53-4b6168adaf01.png)



