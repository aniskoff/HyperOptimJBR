# Copyright (c) Aniskov N.

import json

import pandas as pd

from src.main.util.const import ML_MODELS_LIST
from src.main.util.const import RESULT_FILENAME


class HyperparamsAnalyzer:
    def __init__(self, json_filename: str):
        with open(json_filename) as input_json:
            self.raw_data = json.load(input_json)

    def print_stats(self, ml_model_name, stats):
        if ml_model_name not in ML_MODELS_LIST:
            raise RuntimeError(f'Unknown model: {ml_model_name}')

        samples = []
        for entry in self.raw_data:
            if list(entry.keys())[0] == ml_model_name:
                sample = list(entry.values())[0]
                samples.append(sample)

        df = pd.DataFrame(samples)

        print('-' * 25, f'Stats for {ml_model_name} model', '-' * 25)
        print(df.describe().loc[stats])


def main():

    required_stats = ['mean', 'std', 'min', 'max']
    required_model = 'XGBRegressor'

    hp_analyzer = HyperparamsAnalyzer(RESULT_FILENAME)
    hp_analyzer.print_stats(required_model, required_stats)


if __name__ == '__main__':
    main()
