import subprocess
import tempfile
import sys
# from beat import playHeartBeat
from arduino import myHeartBeat

otherDevice = "shielded-peak-20979"

while True:
    myHeartBeat()
#     with tempfile.TemporaryFile() as tempf:
#         order_commands = ["heroku", "logs", "-n", "1", "--app", otherDevice]
#         output = subprocess.Popen(order_commands, stdout=tempf)
#         output.wait()
#         tempf.seek(0)
#         l = str(tempf.read()).split(" ")
#         otherBeat = l.pop()
#         print(otherBeat[:-3])
        
        # get heart beat then pass that heart beat into the below func
        # playHeartBeat(68)
