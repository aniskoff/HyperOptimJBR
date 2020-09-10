# Copyright (c) Aniskov N.

import os

from src.main.util.const import ROOT_DIR

TEST_RESOURCES_DIR = os.path.join(ROOT_DIR, 'test', 'resources')
TEST_SAMPLES_DIR = os.path.join(TEST_RESOURCES_DIR, 'samples')
TEST_RESULT_DIR = os.path.join(TEST_RESOURCES_DIR, 'result')
TEST_RESULT_FILENAME = os.path.join(TEST_RESULT_DIR, 'result.json')