"""
RECORD CHECK  -  my version
===========================

Name  :  SYLVIA NCHIMBI
Lane  :  AI 
Date  :  4/11

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here
# 1. FUNCTIONS

def parse_line(raw_line):
    """Parse one raw line like 'SRV-02, used=120, total=100' into a dict like"""
    parts = raw_line.strip().lower().split(",")
    hostname = parts[0].strip()
    result = {"hostname": hostname}
    for part in parts[1:]:
        key, value = part.split("=")
        result[key.strip()] = float(value.strip())
    return result

def status_of(record):
    """Return OVER LIMIT / WARNING / OK for one parsed record."""
    perce = record["used"] / record["total"] * 100
    if perce >= 100:
        return "OVER LIMIT"
    elif perce >= 90:
        return "WARNING"
    else:
        return "OK"

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = [
    "  SRV-01 , used=87 , total=100",
    "srv-02,USED=120,total=100",
    "Srv-03, used = 45 , TOTAL = 100",
    "SRV-04, used=95,total=100",
    "  srv-05,used=10,total=100  ",
    "SRV-06,used=unknown,total=100",
]


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.


flagged = 0
for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
        status = status_of(record)
        print(record, status)
        if status != "OK":
            flagged += 1
    except ValueError:
        print(f"Could not parse: {raw_record}")
print(f"Summary: {len(raw_records)} records, {flagged} flagged")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
