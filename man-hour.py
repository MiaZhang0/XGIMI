from business_duration import businessDuration
import pandas as pd
received_time = pd.to_datetime('2020-10-19 08:32:00')
complete_time = pd.to_datetime('2020-10-19 19:42:00')
period = (businessDuration(received_time, complete_time, unit='min') - 90)/60
print(period)