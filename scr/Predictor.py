# src/predictor.py
import joblib
import pandas as pd

# Load the trained model, label encoder, and feature names
model = joblib.load(r"C:\Users\elich\Documents\PROJECT\CUEduHelp\model\Predictive\trained_model_combined.pkl")
label_encoder = joblib.load(r"C:\Users\elich\Documents\PROJECT\CUEduHelp\model\Predictive\label_encoder.pkl")
feature_names = joblib.load(r"C:\Users\elich\Documents\PROJECT\CUEduHelp\model\Predictive\feature_names.pkl")

def preprocess_input(gender, college, level, openness, conscientiousness):
    gender_dict = {'Male': 'GENDER_MALE', 'Female': 'GENDER_FEMALE'}
    college_dict = {'CST': 'COLLEGE_CST', 'COE': 'COLLEGE_COE'}
    
    gender_num = gender_dict.get(gender, 'UNKNOWN')
    college_num = college_dict.get(college, 'UNKNOWN')
    
    if gender_num == 'UNKNOWN' or college_num == 'UNKNOWN':
        raise ValueError("Invalid input for gender or college")
    
    input_df = pd.DataFrame([[openness, conscientiousness, level, college_num, gender_num]], 
                            columns=['Openness Score', 'Conscientiousness Score', 'LEVEL', 'COLLEGE', 'GENDER'])
    
    # Convert LEVEL to a category type
    input_df['LEVEL'] = input_df['LEVEL'].astype('category')
    
    input_df = pd.get_dummies(input_df, columns=['COLLEGE', 'GENDER'])
    for col in feature_names:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[feature_names]
    
    return input_df

def predict_cgpa_class(gender, college, level, openness, conscientiousness):
    try:
        input_data = preprocess_input(gender, college, level, openness, conscientiousness)
        prediction = model.predict(input_data)
        predicted_class = label_encoder.inverse_transform(prediction)[0]
        return predicted_class
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An error occurred: {e}"
