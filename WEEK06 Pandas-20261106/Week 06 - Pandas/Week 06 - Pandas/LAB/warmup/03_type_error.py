# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import pandas as pd

df = pd.DataFrame({"value": [87, 120, 45], "limit": [100, 100, 100]}) #removed the quotes since value are numbers and not text

df["percent"] = (df["value"] / df["limit"]) * 100
