# specify the path to data folder


from pathlib import Path
from datetime import datetime
DATA_PATH = Path(__file__).parents[2] / "data"
CURRENT_YEAR = datetime.now().year


