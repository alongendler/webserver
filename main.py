import sdnotify
import time


def main():
    # Inform systemd that we've finished our startup sequence...
	n = sdnotify.SystemdNotifier()
	n.notify("READY=1")

	count = 1
	while True:
		print("Running... {}".format(count))
		n.notify("STATUS=Count is {}".format(count))
		count += 1
		time.sleep(2)


if __name__ == "__main__":
    print("Test starting up...")
    main()

