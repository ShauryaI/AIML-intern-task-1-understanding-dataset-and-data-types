# AIML-intern-task-1-understanding-dataset-and-data-types
Data structure, types, and ML readiness of datasets.

1. Titanic dataset is downloaded from Kaggle. Filename: Titanic-Dataset.csv
2. Students Performance Dataset Filename: Student_performance_data _.csv

## Actions Performed ##
1. Load the dataset using Pandas and display first and last few records to understand the
structure of rows and columns.
 - print(pd.__version__) to check pandas installed or not or install using >>> pip install pandas
 - Series=Column, DataFrame=Entire table with rows and columns
 - Functions used - head(), tail()
2. Identify numerical, categorical, ordinal, and binary features manually by inspecting
column names and values.
  - The columns are - PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked
  - Numerical - PassengerId, Age, Fare
  - Categorial - Name, Sex, Ticket, Cabin, Embarked
  - Ordinal (Categorical with order) - Pclass, SibSp (siblings/spouses), Parch (parents/children)
  - Binary (A type of categorical feature with only two outcomes) - Survived
3. Use df.info() and df.describe() to understand data types, null values, and statistical
summaries.
  - [5 rows x 12 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    object 
 4   Sex          891 non-null    object 
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    object 
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    object 
 11  Embarked     889 non-null    object 
dtypes: float64(2), int64(5), object(5)
  - PassengerId numeric column, output contains - count, mean, std, min, 25%, 50%, 75%, max
4. Check unique values in categorical columns to understand data distribution.
 - for Name, Sex, Ticket, Cabin, Embarked - all with data type object
 - Output data contains count, unique, top and freq
5. Identify target variable and input features for ML suitability.
 - Input features (or independent variables) are the data points or attributes used to make a prediction, while the target variable (or dependent variable/label) is the specific outcome or value the model is trying to predict, providing the "answer" for training.
 - Input features - Pclass, Sex, Age, Fare, SibSp, Parch, and Embarked
 - Target variable is Survived 
6. Analyze dataset size and discuss whether it is suitable for machine learning.
 - It needs data cleaning for 
 - Age for null values
 - Cabin with just 204 non-null values from 891, better not to consider this column
 - The dataset is relatively small, containing 891 samples in the training set and about 12 features which will further reduce after data cleaning.
 - This is suitable only for data handling/cleaning using df.dropna(), df.fillna(), df.drop_duplicates() etc.
 - For plotting, use matplotlib
7.Write clear observations about data quality issues like missing values or imbalance.


## For Dataset Student_performance_data _.csv ##

1. The columns are - StudentID, Age, Gender, Ethnicity, ParentalEducation, StudyTimeWeekly, Absences, Tutoring, ParentalSupport, Extracurricular, Sports, Music, Volunteering, GPA, GradeClass
  - Numerical - StudentID, Age, GPA, Absences
  - Categorial - Gender
  - Ordinal (Categorical with order) - Ethnicity, GradeClass, ParentalEducation, ParentalSupport, StudyTimeWeekly
  - Binary (A type of categorical feature with only two outcomes) - Gender, Tutoring, Extracurricular, Sports, Music, Volunteering

2. Input features - GPA, Absences, Gender, Ethnicity, ParentalEducation, ParentalSupport, StudyTimeWeekly, Tutoring, Extracurricular, Sports, Music, Volunteering
 - Target variable is GradeClass 

3. Analysis
 - The data does not contain any null value.
 - Probability for duplicates is less.
 - Analysing 2392 entries manually is time-consuming and hence it is a good start for Machine Learning.

## Deliverables ##
For Titanic Dataset
 - Jupyter Notebook: titanic.ipynb
 - HTML file : titanic.html (Command: jupyter nbconvert titanic.ipynb --to html)
 - Dataset Analysis Report: titanic-dataset-analysis-report.docx
