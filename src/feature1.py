import pickle
import heapq

feature1_list = pickle.load(open('host.p'))

host_map = feature1_list[0]
# use a heap to keep order (could have keep only the top 10 in the heap so as to minimize space complexity) 
feature1_h = []
for host, count in host_map.iteritems():
  heapq.heappush(feature1_h, (count, host))
top_10_active_host = [heapq.nlargest(10, feature1_h)]
with open('./log_output/hosts.txt','w') as f:
  for pair in top_10_active_host[0]:
    f.write(pair[1] + ',' + str(pair[0]) + '\n')

  


