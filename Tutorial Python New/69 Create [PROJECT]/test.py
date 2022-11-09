import datetime
import time

x = datetime.datetime.now()
data = f"{x.date()}-{x.hour}-{x.minute}-{x.second}{x.tzinfo}"

print(data)
