# Table of Contents
1. [Challenge Summary](README.md#challenge-summary)
2. [Details of Implementation](README.md#details-of-implementation)
3. [Download Data](README.md#download-data)
4. [Description of Data](README.md#description-of-data)
5. [Writing clean, scalable, and well-tested code](README.md#writing-clean-scalable-and-well-tested-code)
6. [Repo directory structure](README.md#repo-directory-structure)
7. [Testing your directory structure and output format](README.md#testing-your-directory-structure-and-output-format)
8. [Instructions to submit your solution](README.md#instructions-to-submit-your-solution)
9. [FAQ](README.md#faq)


# Challenge Summary

Picture yourself as a backend engineer for a NASA fan website that generates a large amount of Internet traffic data. Your challenge is to perform basic analytics on the server log file, provide useful metrics, and implement basic security measures. 

The desired features are described below: 

# Dependencies
 ```
 import re
 from datetime import timedelta
 from datetime import datetime
 import pickle
 import heapq
```

# To run the programs:
```
python process_log.py
python feature1.py
python feature2.py
python feature3.py
python feature4.py
```

### Feature 1: 
List the top 10 most active host/IP addresses that have accessed the site.

### Feature 2: 
Identify the 10 resources that consume the most bandwidth on the site

### Feature 3:
List the top 10 busiest (or most frequently visited) 60-minute periods 

### Feature 4: 
Detect patterns of three failed login attempts from the same IP address over 20 seconds so that all further attempts to the site can be blocked for 5 minutes. Log those possible security breaches.

