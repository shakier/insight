import pickle
import heapq

feature2_list = pickle.load(open('bandwidth.p'))
bandwidth_map = feature2_list[0]
feature2_h = []
for resource, bandwidth in bandwidth_map.iteritems():
  if resource != '/':  
    heapq.heappush(feature2_h, (bandwidth, resource))
top_10_resources = [heapq.nlargest(10, feature2_h)]
with open('resources.txt','w') as f:
  for pair in top_10_resources[0]:
    f.write(pair[1] + '\n')
