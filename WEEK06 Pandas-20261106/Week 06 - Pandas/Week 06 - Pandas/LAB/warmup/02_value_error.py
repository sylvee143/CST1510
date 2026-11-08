# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({
    "label": ["R-001", "R-002"],   #removed R-003 so that they both have 2 items thus equal
    "value": [87, 120],
})
