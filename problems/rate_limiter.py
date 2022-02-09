
import datetime
import time

reqLogs = {}
maxRequestPerMinute = 1
limitIntervalinSeconds = 2

def countRequests(customerId, currentTime):
    count = 0 
    for timestamp in reqLogs[customerId]:        
        if count > maxRequestPerMinute:
            break
        
        if (currentTime - timestamp).seconds < limitIntervalinSeconds:
            count += 1
        else: 
            break
    
    if count < maxRequestPerMinute:
        reqLogs[customerId].append(currentTime)
    else:
        Job.eneque(resizeLogs(customerId))
        
    return count < maxRequestPerMinute        


def rateLimit(customerId):
        time.sleep(1)
        if not reqLogs.get(customerId):
            reqLogs[customerId] = [datetime.datetime.now()]                    
            return True
        else:
            return countRequests(customerId, datetime.datetime.now())
        
 
            
def resizeLogs():
    pass

print(rateLimit(1))
print(rateLimit(1))
print(rateLimit(1))
print(rateLimit(1))

