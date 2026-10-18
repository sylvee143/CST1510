# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.
from pathlib import Path
#obtaining file from lab
here = Path(__file__).parent
sample_path = here.parent / "records_sample.txt"
try:
    with open("records.txt") as f:
       print(f.read())
except FileNotFoundError:
    print("File not found, using sample instead")
    with open(sample_path) as f:
        print(f.read())    
