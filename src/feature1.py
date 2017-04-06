import pickle
import heapq

feature1_list = pickle.load(open('host.p'))
#feature2_list = pickle.load(open('bandwidth.p'))
#feature3_list = pickle.load(open('host.p'))
#feature4_list = pickle.load(open('second_hit.p'))
#print feature1_list
host_map = feature1_list[0]

feature1_h = []
for host, count in host_map.iteritems():
  heapq.heappush(feature1_h, (count, host))
top_10_active_host = [heapq.nlargest(10, feature1_h)]
with open('hosts.txt','w') as f:
  for pair in top_10_active_host[0]:
    f.write(pair[1] + ',' + str(pair[0]) + '\n')

  


