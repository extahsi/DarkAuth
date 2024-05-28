# init.py

# Standard library imports
import logging
import tkinter as tk
from tkinter import ttk
import time
import random

# Third-party module imports
from passlib.hash import bcrypt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from twilio.rest import Client
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Local module imports
from . import dark_auth
from . import config
from . import utils
from . import chatgpt

# Initialize ChatGPT with API key from configuration
from .config import load_config
if "ai_settings" in load_config():
    ai_settings = load_config()["ai_settings"]
    if "api_key" in ai_settings:
        chatgpt.initialize_chatgpt(ai_settings["api_key"])

# Define __all__ to specify modules to import when using `from <package> import *`
__all__ = ['dark_auth', 'config', 'utils', 'chatgpt']
