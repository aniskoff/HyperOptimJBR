# Copyright (c) Aniskov N.

import json
from typing import List, Dict, Any

import pytest

from src.main.python.hyperparams_extractor.hyperparams_extractor import write_results_to_file
from src.main.util.file_util import get_all_src_files_from_dir
from src.test.util.const import TEST_SAMPLES_DIR, TEST_RESULT_FILENAME

XGBRegressor_HYPERPARAMS = ['objective', 'colsample_bytree', 'learning_rate',
                            'max_depth', 'alpha', 'n_estimators']
SVR_HYPERPARAMS = ['kernel', 'C', 'gamma', 'degree', 'epsilon', 'coef0']

SAMPLE_FILES = get_all_src_files_from_dir(TEST_SAMPLES_DIR)


class TestHyperparamsExtractor:

    @pytest.fixture
    def collected_data(self) -> List[Dict[str, Any]]:
        write_results_to_file(samples_dir=TEST_SAMPLES_DIR, out_filename=TEST_RESULT_FILENAME)
        with open(TEST_RESULT_FILENAME) as input_json:
            return json.load(input_json)

    def test_all_extracted_kwargs_are_hyperparams(self, collected_data):

        for sample in collected_data:
            model_name = list(sample.keys())[0]
            model_hyperparams = list(sample.values())[0]
            if model_name == 'XGBRegressor':
                assert set(model_hyperparams.keys()).issubset(XGBRegressor_HYPERPARAMS)
            elif model_name == 'SVR':
                assert set(model_hyperparams.keys()).issubset(SVR_HYPERPARAMS)



