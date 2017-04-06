import pickle

feature4_list = pickle.load(open('bad_log.p'))

with open('./log_output/blocked.txt','w') as f:
    for line in feature4_list:
          f.write(line + '\n')
