# 🧠 Linear Regression — Study Notes

## 1. Problem & Use Case
- What type of ML task is this model designed for?
    - Linear regression is defined as an algorithm that provides a linear relationship between an independent variable and a dependent variable to predict the outcome of future events. It is used for regression type prediction problems. 

- What real-world problems can this model solve?
    - Linear regression is often used on online applications as it is not computationally intensive and can be retrained to make predictions often. Linear regression is often used for forecasting future values and estimating relationships between variables. 

## 2. Data & Assumptions
- What type of data does the model expect? 
    - Linear regression expects continuous numerical values as input and outputs continuos numerical values as predictions. 

- What are the key assumptions behind the model?
    - Linear regression assumes that the features are not strongly correlated with each other; that is, the relationship between the features and the target are expected to be linear.

## 3. Mathematical Foundation
- What is the core mathematical intuition?
    - Linear regression finds the line of best fit through a plot of data points; that is, it tries to minimize the total squared difference between the actual values and the predicted values (error). If done in higher dimensions (more features are used to predict the target) then linear regression seeks to find the plane (3d) or hyperplane (nd) that minimzes the error.

- What equation(s) define the model?
    - Linear regression is defined by y = B0 + B1x1 + ... + Bnxn

- What loss/cost function does it optimize?
    - Linear regression minimizes the mean squared error between the predicted values and the actual target values. MSE is defined as the mean of the sum of the squared difference of the actual value and the predicted value. 

## 4. Learning & Training Process
- How does the model learn from training data?
    - Linear regression begins by assuming that some target variable y can be predicted by some combination of input features x; each input feature x has a weight B. The model begins by assigning random weights to the features and then using them to make a prediction of y. The model then calculates the MSE and sees how far off its prediction is. The model then adjusts the weights Bj to reduce the error. This process repeats iteratively until the error converges to a minimum error or meets a stopping criteria 

## 5. Prediction Logic
- How does the model make predictions on new data?
    - After training, the model now has an equation that is meant to represent the relationship between the feature(s) and the target. Given a new data point, it is plugged into the model to predict the new target. Prediction simply uses the learned parameters and the new input features—no need to refit or update the model during prediction.

## 6. Hyperparameters & Tuning
- What are the key hyperparameters of this model?
    - Basic linear regression does not have hyperparameters to tune; some alternative methods of regression might have some. 

## 7. Preprocessing Requirements
- What preprocessing is typically required?
    - Missing values must be removed or imputed; linear regression cannot handle null values. Categorical features must be converted to numerical ones using methods like one hot encoding; linear regression cannot handle categorical data. Linear regression does not require strict scaling but normalization may help if you use regularization or gradient descent for finding model parameters or avoiding overfitting. You should check for multicollinearity amongst the features, if 2 features are highly correlated it can destabilize estimates. Outliers might want to be removed if the model is perfroming unexpectedly. 

## 8. Evaluation
- What metrics are best for evaluating this model? 
    - For regression tasks we usually use metrics that measure how close the predicted numbers are to the actual values such as Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), or R-Squared (R2).

- How can you detect overfitting or underfitting?
    - Underfitting is when the model is too simple to capture patterns. Overfitting is when the model memorizes data as opposed to learning patterns and randomness. To detect these issues we can compute metrics such as MSE or R2 on both training and test/validation data sets and evaluate from there. 

## 9. Applications
- List at least 3 real-world use cases for this model.
    - Predicting housing prices, Sales forecasting, Risk assessment and credit scoring. 

## 10. Model Deployment
- How is this model typically deployed in production?
1) A model is usually trained offline using training data.
2) The trained model will be saved (serialized) or exported.
3) Wrap the saved model into an API that can receive input, pass it into the model, and return predictions. 
4) Host the prediction API on a server or cloud platform. 
5) The model would then be integrated with client systems. The system would send new data to the API, the API would process the input, use the model to predict, and return the result in real time or in batches. 
6) Engineers would track the model and adjust if performance goes down. 

## 11. Strengths & Weaknesses
- What are the key advantages of this model?
    - Linear regression is simple and easy to interpret. It is not computationally intensive to train and requires few resources. Similarly, it works very well with linearly separable data and serves as the basis for many other models .

- What are the common limitations or failure modes?
    - Linear regression assumes linearity so it fails when the relationship between features and target is nonlinear. Similarly, linear regression is very sensitive to outliers, a few extreme values can distort the regression line heavily and lead to poor predictions. Linear regression is poor with high dimensional and sparse data. 

- When should I use this model?
    - Linear regression is only appropriate when trying to predict a number. Given a new dataset, to determine if linear regression is appropritate, (depending on dimensionality) plot the data and see if there is a noticable trend line in the scatter plot. Similarly, check if the features are highly correlated.

- When should this model be avoided?
    - Linear regression should be avoided when the relationship between the featuers and target appears to be nonlinear. Similarly, if input features are highly correlated with each other then linear regression will not perform well. Linear regression might want to be avoided if a dataset contains many outliers. 

## 13. Additional Resources
    - https://www.spiceworks.com/tech/artificial-intelligence/articles/what-is-linear-regression/    
    - https://aws.amazon.com/what-is/linear-regression/
    - https://www.youtube.com/watch?v=4b4MUYve_U8&list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU&index=2
