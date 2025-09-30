import os
from datetime import date

# ------------------ MongoDB ------------------

DATABASE_NAME="Proj1"
COLLECTION_NAME="Proj1-Data"
MONGODB_URL_KEY="MONGODB_URL"

# ------------------ Pipeline ------------------
PIPELINE_NAME:str = ""
ARTIFACT_DIR:str='artifact'  

# ------------------ Dataset ------------------

FILE_NAME:str="data.csv"
TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"
SCHEMA_FILE_PATH:str=os.path.join("config","schema.yaml")

# ------------------ Data Ingestion ------------------
DATA_INGESTION_DIR_NAME:str="data_ingestion"  
DATA_INGESTION_COLLECTION_NAME:str="Proj1-Data"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.25
DATA_INGESTION_INGESTED_DIR:str="ingested"

# ------------------DataValidation ------------------
DATA_VALIDATION_DIR_NAME:str="DataValidation"
DATA_VALIDATION_REPORT_FILE_NAME:str="report.yaml"

# ------------------ Model ------------------
CURRENT_YEAR=date.today().year
TARGET_COLUMN="Response" 
PREPROCESSING_OBJ_FILE_NAME:str="preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"


# ------------------ Data Transformation ------------------
DATA_TRANSFORMATION_DIR_NAME:str="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_OBJ_DIR:str="transformed_obj"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str="transformed_data"


# ------------------ Model Trainer ------------------
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")
MODEL_TRAINER_N_ESTIMATORS = 100
MODEL_TRAINER_MIN_SAMPLES_SPLIT: int = 7
MODEL_TRAINER_MIN_SAMPLES_LEAF: int = 6
MIN_SAMPLES_SPLIT_MAX_DEPTH: int = 10
MIN_SAMPLES_SPLIT_CRITERION: str = 'entropy'
MIN_SAMPLES_SPLIT_RANDOM_STATE: int = 101 


# ---------------------Backblaze------------------------

AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
ENDPOINT_URL= "https://s3.us-east-005.backblazeb2.com"


# ----------------- Model-Evaluation -------------------
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE:float=0.02
MODEL_BUCKET_NAME:str="Wanted-SG-Bucket"
MODEL_PUSHER_S3_KEY = "model-registry"


# ------------ App ----------------------

APP_HOST="0.0.0.0"
APP_PORT=5000
