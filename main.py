import sdnotify
import time

print("Test starting up...")
# In a real service, this is where you'd do real startup tasks
# like opening listening sockets, connecting to a database, etc...
time.sleep(10)
print("Test startup finished")

# Inform systemd that we've finished our startup sequence...
n = sdnotify.SystemdNotifier()
n.notify("READY=1")

count = 1
while True:
	print("Running... {}".format(count))
	n.notify("STATUS=Count is {}".format(count))
	count += 1
	time.sleep(2)
