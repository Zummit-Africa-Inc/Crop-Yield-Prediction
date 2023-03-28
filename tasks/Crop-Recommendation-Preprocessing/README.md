## Crop Recommendation Cleaning & Preprocessing

Cleaning and preprocessing of crop historical data to prepare the dataset for building multiclassification models that can predict what crop type as the target variable based on the inputed conditions as the independent variable.

Cleaning and preprocessing workflow involves checking out the properities of the features and the target variables, the distibutions of the features, checking for missing values and outliers and treating them and dealing with other preprocessing techniques that applies to the dataset.

For the dataset there are 2200 observations and 8 features in all. 7 independent features and 1 target features. The target feature as 21 crops to be predicted, which include rice, maize, jute, cotton, coconut, papaya, orange, apple, muskmelon, watermelon, grapes, mango, banana, pomegranate, lentil, blackgram, mungbean, 
mothbeans, pigeonpeas, kidneybeans, chickpea, coffee, e.t.c.

These independent features include:

- `N`
- `P`
- `K`
- `temperature` 
- `humidity` 
- `ph`
- `rainfall`