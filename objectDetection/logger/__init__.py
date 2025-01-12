import logging
import os 
from datetime import datetime
from pathlib import Path

# Get project root directory
def get_project_root():
    return str(Path(__file__).parent)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(get_project_root(), 'log')
os.makedirs(log_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"
)

