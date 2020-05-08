# forward-selection-MSE
Professer asked us to use MSE as a forwarding selection cretirion ... (aic、bic不香嘛……现在有人自己写方程用mse做的嘛……老师的要求实在是emmm）

First step:
- Write a for loop to select the best variable with the minimum MSE value.
- If the new MSE value is smaller than the previous one, we overwrite the new MSE value with the previous one. Otherwise, the minimun MSE calue doesn't change.

Second step:
- Write a for loop to select specific variables given m, which is the target number of variables.
- Return both the best model and best variables given m.

Third step:
- Write a for loop to record MSE values for m range using sample splitting( we can alos use cross-validation method here).
- Select the minimum MSE value and return its index.
