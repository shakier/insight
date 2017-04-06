import re
from datetime import timedelta
from datetime import datetime
import pickle

host_map = {} 
time_map = {}
bandwidth_map = {}
second_hit_list = []
bad_temp_time = {}
bad_temp_count = {}
bad_temp_map = {}
bad_temp_log = []

#parse the log file line by line
with open('./log_input/log.txt', 'rb') as f:
  for line in f:
    m = re.search('(.+)\s-\s-\s\[(.+)\s.+\]\s\"(.+)"\s(\d+)\s(.+)', line)
    host = m.group(1)
    time = m.group(2)
    parsed_time = datetime.strptime(time, '%d/%b/%Y:%H:%M:%S')
    #some of the requests do not follow common format; treat as special cases
    try:
      request = m.group(3).split()[1]
    except:
      print 'bad input:', line
    reply = m.group(4)
    byte_num = m.group(5)
    #count all hits by hosts
    if host not in host_map:
      host_map[host] = 1
    elif host in host_map:
      host_map[host] += 1
    #count bandwidth by requests
    if request not in bandwidth_map:
      bandwidth_map[request] = 1
    elif request in bandwidth_map:
      bandwidth_map[request] += 1
    second_hit_list.append(parsed_time) 

    ########## following is for processing for feature 4 ############
    ########## uncommon the lines beginning with 'print' will see detail processing while executing ########
    
    if host in bad_temp_map:
#      print 'host in bad_temp_map', host, bad_temp_map
      if parsed_time <= bad_temp_map[host] + timedelta(minutes = 5):
        bad_temp_log.append(m.group(0))
#        print 'within five minutes window, added to bad_log'
      elif parsed_time > bad_temp_map[host] + timedelta(minutes = 5):
        del bad_temp_map[host]
#        print 'not within five minutes window, deleted from bad_temp_map'
    else:
      if reply == '200':
#        print 'reply is 200'
        if host in bad_temp_time:
          if parsed_time <= bad_temp_time[host] + timedelta(seconds = 20):
#            print 'reply 200 within 20 seconds of last 401, delete the host from the list'
            del bad_temp_time[host]
            del bad_temp_count[host]
      if reply == '401':
#        print 'reply is 401'
        if host not in bad_temp_time:
#          print 'host not in bad_temp_time, add to it for the first time'
          bad_temp_time[host] = parsed_time
          bad_temp_count[host] = 1
        elif host in bad_temp_time:
          if parsed_time > bad_temp_time[host] + timedelta(seconds = 20):
#            print 'host in bad_temp_time, but out of 20 seconds, add again, renewed time'
            bad_temp_time[host] = parsed_time
            bad_temp_count[host] = 1
          elif parsed_time <= bad_temp_time[host] + timedelta(seconds = 20):
#            print 'host in badtemp_time, within 20 seconds, add one more count, time same'
            bad_temp_count[host] += 1
            if bad_temp_count[host] == 3:
              bad_temp_map[host] = parsed_time
              del bad_temp_count[host]
              del bad_temp_time[host]
#              print 'reached 3 times, added to map', bad_temp_map

host = [host_map]
pickle.dump(host, open('host.p', 'wb')) 
bandwidth = [bandwidth_map]
pickle.dump(bandwidth, open('bandwidth.p', 'wb'))
pickle.dump(second_hit_list, open('second_hit.p', 'wb'))
pickle.dump(bad_temp_log, open('bad_log.p','wb'))


