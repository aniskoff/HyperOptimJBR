# Copyright (c) Aniskov N.

import os
from pathlib import Path

ROOT_DIR = os.path.join(Path(__file__).resolve().parents[3], 'src')
RESOURCES_DIR = os.path.join(ROOT_DIR, 'main', 'resources')
SAMPLES_DIR = os.path.join(RESOURCES_DIR, 'samples')
RESULT_DIR = os.path.join(RESOURCES_DIR, 'result')
RESULT_FILENAME = os.path.join(RESULT_DIR, 'result.json')

ML_MODELS_LIST = ['XGBRegressor', 'SVR']

