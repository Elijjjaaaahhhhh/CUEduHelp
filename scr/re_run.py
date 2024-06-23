import random
import joblib
import pandas as pd

# Load the trained VotingClassifier model
voting_clf = joblib.load(r'C:\Users\elich\Documents\PROJECT\CUEduHelp\model\Recommender\voting_classifier_model.pkl')
label_encoder = joblib.load(r'C:\Users\elich\Documents\PROJECT\CUEduHelp\model\Recommender\label_encoder.pkl')
feature_names = joblib.load(r'C:\Users\elich\Documents\PROJECT\CUEduHelp\model\Recommender\feature_names.pkl')


# Define the course requirements
course_requirements = {
    "Chemical Engineering": {
        "jamb_min_score": 240,
        "jamb_subjects": {"English", "Math", "Physics", "Chemistry"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Technical Drawing": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
        },
        "personality": {"openness_min": 23, "conscientiousness_min": 35}
    },
    "Civil Engineering": {
        "jamb_min_score": 250,
        "jamb_subjects": {"English", "Math", "Physics", "Chemistry"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Technical Drawing": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
        },
        "personality": {"openness_min": 25, "conscientiousness_min": 35}
    },
    "Computer Engineering": {
        "jamb_min_score": 250,
        "jamb_subjects": {"English", "Math", "Physics", "Chemistry"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Economics": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Technical Drawing": ["A1", "B2", "B3", "C4", "C5", "C6"]
        },
        "personality": {"openness_min": 30, "conscientiousness_min": 30}
    },
    "Electrical and Electronics Engineering": {
        "jamb_min_score": 240,
        "jamb_subjects": {"English", "Math", "Physics", "Chemistry"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Technical Drawing": ["A1", "B2", "B3", "C4", "C5", "C6"]
        },
        "personality": {"openness_min": 30, "conscientiousness_min": 35}
    },
    "Information and Communication Engineering": {
        "jamb_min_score": 200,
        "jamb_subjects": {"English", "Math", "Physics", "Chemistry"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Technical Drawing": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Geography": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
        },
        "personality": {"openness_min": 30, "conscientiousness_min": 30}
    },
    "Mechanical Engineering": {
        "jamb_min_score": 240,
        "jamb_subjects": {"English", "Math", "Physics", "Chemistry"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Technical Drawing": ["A1", "B2", "B3", "C4", "C5", "C6"]
        },
        "personality": {"openness_min": 30, "conscientiousness_min": 30}
    },
    "Petroleum Engineering": {
        "jamb_min_score": 210,
        "jamb_subjects": {"English", "Math", "Physics", "Chemistry"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Technical Drawing": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Geography": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],

        },
        "personality": {"openness_min": 30, "conscientiousness_min": 30}
    },
    "Architecture": {
        "jamb_min_score": 240,
        "jamb_subjects": {"English", "Math", "Physics", "Chemistry", "Biology", "Economics"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Technical Drawing": ["A1", "B2", "B3", "C4"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Geography": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6" "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Economics": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
        },
        "personality": {"openness_min": 30, "conscientiousness_min": 30}
    },
    "Biochemistry": {
        "jamb_min_score": 190,
        "jamb_subjects": {"English", "Biology", "Chemistry", "Physics", "Math"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4",],
            "Chemistry": ["A1", "B2", "B3", "C4"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Geography": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Economics ": ["A1", "B2", "B3", "C4", "C5", "C6" "D7", "E8", "F9"],

        },
        "personality": {"openness_min": 30, "conscientiousness_min": 23}
    },
    "Biology (Applied Biology and Biotechnology)": {
        "jamb_min_score": 190,
        "jamb_subjects": {"English", "Biology", "Chemistry", "Physics", "Math"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6" "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6" "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Economics ": ["A1", "B2", "B3", "C4", "C5", "C6" "D7", "E8", "F9"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Geography": ["A1", "B2", "B3", "C4", "C5", "C6" "D7", "E8", "F9"],
        },
        "personality": {"openness_min": 30, "conscientiousness_min": 23}
    },
    "Building Technology": {
        "jamb_min_score": 180,
        "jamb_subjects": {"English", "Math", "Physics", "Chemistry"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Economics": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Geography": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Technical Drawing": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],

        },
        "personality": {"openness_min": 27, "conscientiousness_min": 25}
    },
    "Computer Science": {
        "jamb_min_score": 240,
        "jamb_subjects": {"English", "Math", "Physics", "Biology", "Chemistry", "Agric Science", "Economics", "Geography", "Further Math"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Technical Drawing": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Geography": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Economics ": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Agricultural Science" : ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"]
        },
        "personality": {"openness_min": 27, "conscientiousness_min": 25}
    },
    "Estate Management": {
        "jamb_min_score": 180,
        "jamb_subjects": {"English", "Math", "Economics", "Geography", "Physics", "Chemistry", "Biology" },
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Economics": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Geography": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Technical Drawing": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Agricultural Science": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
        },
        "personality": {"openness_min": 20, "conscientiousness_min": 25}
    },
    "Industrial Chemistry": {
        "jamb_min_score": 180,
        "jamb_subjects": {"English", "Chemistry", "Math", "Physics", "Biology", "Agric Science", "Geography"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Agricultural Science": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Geography": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Economics ": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Technical Drawing": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
        },
        "personality": {"openness_min": 30, "conscientiousness_min": 25}
    },

    "Industrial Mathematics": {
        "jamb_min_score": 180,
        "jamb_subjects": {"English", "Math", "Physics", "Chemistry", "Economics", "Biology",  "Geography"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Economics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Geography": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
        },
        "personality": {"openness_min": 30, "conscientiousness_min": 20}
    },
    "Industrial Physics": {
        "jamb_min_score": 180,
        "jamb_subjects": {"English", "Math", "Physics", "Biology", "Chemistry", "Geography"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Computer Science": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Geography": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Economics ": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"]

        },
        "personality": {"openness_min": 30, "conscientiousness_min": 20}
    },
    "Management Information Systems": {
        "jamb_min_score": 200,
        "jamb_subjects": {"English", "Math", "Economics", "Biology", "Chemistry", "Agricultural Science" "Economics" "Geography"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Economics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4"],
            "Further Maths": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Technical Drawing": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Geography": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Agricultural Science": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
        },

        "personality": {"openness_min": 20, "conscientiousness_min": 25}
    },
    "Microbiology": {
        "jamb_min_score": 180,
        "jamb_subjects": {"English", "Biology", "Chemistry", "Physics”, “Math"},
        "waec_subjects": {
            "Maths": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8"],
            "English": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Biology": ["A1", "B2", "B3", "C4"],
            "Chemistry": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Physics": ["A1", "B2", "B3", "C4", "C5", "C6"],
            "Geography": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Economics ": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Trade": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Civic Education": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],
            "Computer Studies": ["A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"],


        },
        "personality": {"openness_min": 25, "conscientiousness_min": 22}
    }

}

# Define course similarities
course_similarity = {
    "Computer Science": ["Computer Engineering", "Management Information Systems", "Industrial Mathematics", "Industrial Physics"],
    "Computer Engineering": ["Computer Science", "Electrical and Electronics Engineering", "Information and Communication Engineering"],
    "Management Information Systems": ["Computer Science", "Industrial Mathematics", "Industrial Physics"],
    "Industrial Mathematics": ["Computer Science", "Management Information Systems", "Industrial Physics", "Mechanical Engineering", "Building Technology"],
    "Industrial Physics": ["Computer Science", "Management Information Systems", "Industrial Mathematics", "Mechanical Engineering"],
    "Petroleum Engineering": ["Chemical Engineering", "Biochemistry", "Industrial Chemistry"],
    "Biochemistry": ["Petroleum Engineering", "Microbiology", "Biology (Applied Biology and Biotechnology)", "Chemical Engineering"],
    "Microbiology": ["Biochemistry", "Biology (Applied Biology and Biotechnology)"],
    "Biology (Applied Biology and Biotechnology)": ["Biochemistry", "Microbiology"],
    "Chemical Engineering": ["Petroleum Engineering", "Biochemistry", "Industrial Chemistry"],
    "Industrial Chemistry": ["Chemical Engineering", "Petroleum Engineering"],
    "Civil Engineering": ["Building Technology", "Estate Management"],
    "Building Technology": ["Civil Engineering", "Estate Management", "Architecture", "Mechanical Engineering"],
    "Estate Management": ["Civil Engineering", "Building Technology", "Architecture"],
    "Electrical and Electronics Engineering": ["Information and Communication Engineering", "Computer Engineering"],
    "Information and Communication Engineering": ["Electrical and Electronics Engineering", "Computer Engineering"],
    "Architecture": ["Building Technology", "Estate Management"]
}

course_mapping = {
    0: "Chemical Engineering",
    1: "Civil Engineering",
    2: "Computer Engineering",
    3: "Electrical and Electronics Engineering",
    4: "Information and Communication Engineering",
    5: "Mechanical Engineering",
    6: "Petroleum Engineering",
    7: "Architecture",
    8: "Biochemistry",
    9: "Biology (Applied Biology and Biotechnology)",
    10: "Building Technology",
    11: "Estate Management",
    12: "Computer Science",
    13: "Industrial Chemistry",
    14: "Industrial Mathematics",
    15: "Industrial Physics",
    16: "Management Information Systems",
    17: "Microbiology"
}


# Define courses by college
courses_by_college = {
    "CoE": ["Chemical Engineering", "Civil Engineering", "Computer Engineering", "Electrical and Electronics Engineering", "Information and Communication Engineering", "Mechanical Engineering", "Petroleum Engineering"],
    "CST": ["Architecture", "Biochemistry", "Biology (Applied Biology and Biotechnology)", "Building Technology", "Computer Science", "Estate Management", "Industrial Chemistry", "Industrial Mathematics", "Industrial Physics", "Management Information Systems", "Microbiology"]
}

def create_student_profile(waec_data, jamb_score, jamb_subjects, openness, conscientiousness):
    student_profile = {
        'JAMB_SCORE': jamb_score,
        'JAMB_SUBJECTS': set(jamb_subjects),
        'Openness Score': openness,
        'Conscientiousness Score': conscientiousness
    }
    for subject, grade in waec_data.items():
        student_profile[f'Waec_{subject}'] = grade
    return student_profile

def check_qualification(student, course):
    req = course_requirements[course]
    if student['JAMB_SCORE'] < req['jamb_min_score']:
        return False
    if len(student['JAMB_SUBJECTS']) != 4 or not req['jamb_subjects'].issubset(student['JAMB_SUBJECTS']):
        return False
    waec_subject_count = sum(1 for subject, grades in req['waec_subjects'].items() if f'Waec_{subject}' in student and student[f'Waec_{subject}'] in grades)
    if waec_subject_count < 8 or waec_subject_count > 9:
        return False
    if student['Openness Score'] < req['personality']['openness_min']:
        return False
    if student['Conscientiousness Score'] < req['personality']['conscientiousness_min']:
        return False
    return True

def determine_qualifications(student, preferred_course):
    qualified_courses = set()
    all_checked_courses = set()
    
    def check_and_add(course):
        if course not in all_checked_courses:
            if check_qualification(student, course):
                qualified_courses.add(course)
            all_checked_courses.add(course)
    
    check_and_add(preferred_course)
    if preferred_course in qualified_courses:
        if preferred_course in course_similarity:
            for similar_course in course_similarity[preferred_course]:
                check_and_add(similar_course)
    else:
        college = next((col for col, courses in courses_by_college.items() if preferred_course in courses), None)
        if college:
            for course in courses_by_college[college]:
                check_and_add(course)
            additional_qualified_courses = set(qualified_courses)
            for course in additional_qualified_courses:
                if course in course_similarity:
                    for similar_course in course_similarity[course]:
                        check_and_add(similar_course)
    
    return qualified_courses

def content_based_filtering(student_profile):
    waec_grade_mapping = {'A1': 7, 'B2': 6, 'B3': 5, 'C4': 4, 'C5': 3, 'C6': 2, 'D7': 1, 'E8': 1, 'F9': 1}
    feature_vector = [waec_grade_mapping.get(student_profile.get(col, 'F9'), 1) for col in feature_names[:11]]
    feature_vector += [student_profile['Openness Score'], student_profile['Conscientiousness Score'], student_profile['JAMB_SCORE']]
    feature_vector = pd.DataFrame([feature_vector], columns=feature_names)
    prediction = voting_clf.predict(feature_vector)
    course_label = label_encoder.inverse_transform(prediction)[0]
    return course_mapping.get(course_label, "Unknown Course")

def get_recommendations(preferred_course, waec_data, jamb_score, jamb_subjects, openness, conscientiousness):
    student_profile = create_student_profile(waec_data, jamb_score, jamb_subjects, openness, conscientiousness)
    recommended_program = content_based_filtering(student_profile)
    qualified_courses = determine_qualifications(student_profile, preferred_course)
    hybrid_recommendations = list(qualified_courses)
    if recommended_program not in hybrid_recommendations:
        hybrid_recommendations.append(recommended_program)
    hybrid_recommendations = hybrid_recommendations[:3]  # Ensure only 3 recommendations
    return student_profile, hybrid_recommendations