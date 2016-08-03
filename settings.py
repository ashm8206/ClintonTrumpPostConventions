TRACK_TERMS = ["trump", "clinton", "Mike pence", "tim kaine"]

TWITTER_APP_KEY = "hRG7INKwRqTmYGfLqJVXSZiCT"
TWITTER_APP_SECRET = "53i8SakUNDJzTpY8EnPAWk3FH6VE8PC6XECYszQrnADUUdFmLc"
TWITTER_KEY = "3192402942-PAqjNYH27n9CFzUhwoJBTe3wmOowIH5GiCgj2ir"
TWITTER_SECRET = "a5Aw7zjJGurPO2vGRVRah0rv9B3zTHjXwxiz3bzUrLboV"

CONNECTION_STRING = "sqlite:///tweets.db"
CSV_NAME = "tweets.csv"
TABLE_NAME = "election"

try:
    from private import *
except Exception:
    pass
