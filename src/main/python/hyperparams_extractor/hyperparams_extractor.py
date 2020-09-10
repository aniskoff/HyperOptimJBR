#!/usr/bin/env python3
# Copyright (c) Aniskov N.

import ast
import json
from typing import Dict, List, Any

from src.main.util.const import SAMPLES_DIR, RESULT_FILENAME, ML_MODELS_LIST
from src.main.util.file_util import read_file_to_string, get_all_src_files_from_dir


class HyperparamsExtractor:
    """
    This class is extracting hyperparameters from python 3 source code
    of machine learning model training
    """
    def __init__(self, filename: str) -> None:
        """
        :param filename: path to .py file with python 3 source code
        """
        src = read_file_to_string(filename)
        self.__tree = ast.parse(src)
        self.__models_to_hyperparams_list = []

    def __extract_hyperparams(self, node: ast.AST) -> None:
        """
        recursively traverses the AST (starting at given node) and adds all found and collected
        dicts of the form {<MODEL_NAME>: <HYPERPARAMS>} to self.__models_to_hyperparams_list
        """
        if not isinstance(node, ast.AST):
            return

        if not isinstance(node, ast.Call) or self.__get_func_name(node) not in ML_MODELS_LIST:
            for field_name in node._fields:
                field = getattr(node, field_name)
                if isinstance(field, list):
                    for elem in field:
                        self.__extract_hyperparams(elem)
                self.__extract_hyperparams(field)

        else:
            hyperparams = {}
            self.__models_to_hyperparams_list.append({self.__get_func_name(node): hyperparams})
            for keyword in node.keywords:
                if isinstance(keyword.value, ast.Constant):
                    hyperparams[keyword.arg] = keyword.value.value  # Python 3.8+
                elif isinstance(keyword.value, ast.Num):
                    hyperparams[keyword.arg] = keyword.value.n  # before Python 3.8
                elif isinstance(keyword.value, ast.Str):
                    hyperparams[keyword.arg] = keyword.value.s  # before Python 3.8

    @staticmethod
    def __get_func_name(node: ast.Call) -> str:
        if not isinstance(node, ast.Call):
            raise TypeError(f'Expected ast.Call node, but {type(node).__name__} received')
        try:
            return node.func.id
        except AttributeError:
            return node.func.attr

    def get_hyperparams(self) -> List[Dict[str, Any]]:
        if not self.__models_to_hyperparams_list:
            self.__extract_hyperparams(self.__tree)
        return self.__models_to_hyperparams_list


def write_results_to_file(samples_dir: str = SAMPLES_DIR, out_filename: str = RESULT_FILENAME):
    """
    This function extracts hyperparameters from all files located in samples_dir folder,
    creates out_filename file and writes the result of work to it.
    """
    result = []
    for sample_filename in get_all_src_files_from_dir(samples_dir):
        hp_extractor = HyperparamsExtractor(sample_filename)
        result += hp_extractor.get_hyperparams()

    with open(out_filename, 'w') as out_f:
        json.dump(result, out_f)


def main() -> None:
    write_results_to_file(samples_dir=SAMPLES_DIR, out_filename=RESULT_FILENAME)


if __name__ == '__main__':
    main()

