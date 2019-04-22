# Logistic Regression

## Diabetes.csv File을 이용한 로지스틱 회귀분석

### 1. 필요한 Packages를 Import한다.

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
```

### 2. Data를 호출한다.

```python
df = pd.read_csv("Diabetes.csv",header=0)
df.head()
```

![image](https://user-images.githubusercontent.com/46669551/55401827-d9d66680-558c-11e9-887c-e783f98d1256.png)

### 3. Columns의 요인들이 Outcome과 의 관계를 알아보는 것임으로 8개의 항목을 data set으로 만든다.

```python
select_cols =['Pregnancies','Insulin','BMI','Age','Glucose','BloodPressure','DiabetesPedigreeFunction','SkinThickness']
```

### 4. outcome을 종속변수로 나머지 변수를 독립변수로 지정한다.

```python
x = df[select_cols].values
y = df['Outcome'].values.reshape(-1,1)
# 1:1 독립변수의 형태로 만들기 위해 y는 reshape를 수행 한다.
```

### 5. 두변수의 형태를 본다

```python
x.shape, y.shape
```

```
((768, 8), (768, 1))
```

### 6.  교차검증을 수행한다.

```python
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.25, random_state=0)
```

### 7. Logistic 회귀함수에 학습 Data인 xtrain과 ytrain을 넣어준다.

```python
logRegTest = LogisticRegression()
logRegTest.fit(xtrain, ytrain)
```

```
# 출력
C:\Users\Administrator\Anaconda3\lib\site-packages\sklearn\linear_model\logistic.py:433: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.
  FutureWarning)
C:\Users\Administrator\Anaconda3\lib\site-packages\sklearn\utils\validation.py:761: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
  y = column_or_1d(y, warn=True)
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='warn',
          n_jobs=None, penalty='l2', random_state=None, solver='warn',
          tol=0.0001, verbose=0, warm_start=False)
```

### 8. 검증데이터를 통해 예측값(Predict)을 구한다.

```python
preResult = logRegTest.predict(xtest)
print(xtest), print(preResult)
```

```
[[  1.      0.     42.9   ...  76.      1.394  43.   ]
 [  2.    100.     33.6   ...  74.      0.404  30.   ]
 [  4.      0.     34.    ...  62.      0.391   0.   ]
 ...
 [  1.    182.     25.4   ...  60.      0.947   8.   ]
 [  3.      0.     21.1   ...  78.      0.268   0.   ]
 [  5.      0.     27.6   ...  78.      0.258  30.   ]]
[1 0 0 1 0 0 1 1 0 0 1 1 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0
 0 0 1 0 0 0 1 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 1 1 1 1 0 0 0 0 1 0 1
 1 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 1 0 0 0 0 1 0
 0 1 0 1 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 0 0
 0 0 0 1 0 0 1 0 1 0 1 1 1 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0
 0 1 0 0 0 0 0]
(None, None)
```

### 9. 학습데이터와 검증데이터를 비교하기 위해 DataFrame의 형태로 바꾸어 준다.

```python
df2 = pd.DataFrame({'ytest':ytest.flatten(),"pre":preResult.flatten()})
df2.head(10)
```

![image](https://user-images.githubusercontent.com/46669551/55402301-19ea1900-558e-11e9-9cc9-6bdb9cb56c5a.png)

### 10. 예측모델의 성능을 측정한다.

```python
np.sqrt(mean_squared_error(ytest, preResult))
```

```
0.4389855730355308
```

