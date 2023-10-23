"""
CS 491 Project 1
Team Members: Scott Ratchford, Ben Fioresi, and Alexander Reese
"""
try:
  import tensorflow as tf
except ModuleNotFoundError:
  !pip install tensorflow
  import tensorflow as tf

try:
  import tensorflow_decision_forests as tfdf
except ModuleNotFoundError:
  !pip install tensorflow_decision_forests
  import tensorflow_decision_forests as tfdf

try:
  import pandas as pd
except ModuleNotFoundError:
  !pip install pandas
  import pandas as pd

# import numpy as np
# import matplotlib.pyplot as plt
