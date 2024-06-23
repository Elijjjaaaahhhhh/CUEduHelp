# CUEduHelp

CUEduHelp is a Python-based application that helps prospective and enrolled students in predicting their CGPA class and recommending courses based on their WAEC and JAMB scores, as well as their personality traits.

## Features

- Predict CGPA class for enrolled students based on their gender, college, level, and personality traits.
- Recommend suitable courses for prospective students based on their WAEC and JAMB scores, and personality traits.

## Project Structure

- `src/`
  - `main.py`: Main GUI application code using PyQt5.
  - `predictor.py`: Code for predicting CGPA class.
  - `rerun.py`: Code for recommending courses.
  - `db_operations.py`: Database operations for inserting student records.
  - `initialize_db.py`: Code for initializing the database schema.
- `model/`
  - `Predictive/`
    - `trained_model_combined.pkl`: Trained model for predicting CGPA class.
    - `label_encoder.pkl`: Label encoder for CGPA classes.
    - `feature_names.pkl`: Feature names used in the predictive model.
  - `Recommender/`
    - `voting_classifier_model.pkl`: Trained voting classifier model for recommending courses.
    - `label_encoder.pkl`: Label encoder for courses.
    - `feature_names.pkl`: Feature names used in the recommender model.
- `database/`
  - `students.db`: SQLite database file storing student records.

## Requirements

- Python 3.8 or higher
- PyQt5
- scikit-learn
- pandas
- joblib
- sqlite3

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CUEduHelp.git
   cd CUEduHelp
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   python src/initialize_db.py
   ```

## Usage

1. Run the main application:
   ```bash
   python src/main.py
   ```

2. Follow the on-screen instructions to input student information and get predictions/recommendations.

## Troubleshooting

If you encounter any issues while running the application, ensure that:

- All required dependencies are installed.
- The database is initialized properly.
- The model files are located in the correct directory (`model/`).


## Contributing

We welcome contributions! Please fork the repository and submit pull requests.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



