import pickle
import heapq
from datetime import timedelta

time_list = pickle.load(open('second_hit.p'))

hour_window = []
max_window = []
hour_window.append(time_list[0])
for i in xrange(1, len(time_list)):
  if len(hour_window) == 0:
    break
  if time_list[i] <= hour_window[0] + timedelta(seconds = 3600):
    hour_window.append(time_list[i])
  else:
    heapq.heappush(max_window, (len(hour_window), hour_window[0]))
    while len(hour_window) != 0 and hour_window[0] + timedelta(seconds = 3600) < time_list[i]:
      del hour_window[0]

top_10_hours = [heapq.nlargest(10, max_window)]

with open('hours.txt','w') as f:
    for pair in top_10_hours[0]:
      f.write(pair[1].strftime('%d/%b/%Y:%H:%M:%S -0400') + ',' + str(pair[0]) + '\n')



