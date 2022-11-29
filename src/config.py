import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))

except FileNotFoundError:
    pass

PLOT_FILENAME = os.getenv("PLOT_FILENAME") or "plot.csv"
PLOT_FILE_PATH = os.path.join(dirname, "..", "data", PLOT_FILENAME)
