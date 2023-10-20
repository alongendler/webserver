import sdnotify
import time
import logging
from systemd import journal

log = logging.getLogger('demo')
log.addHandler(journal.JournaldLogHandler())
log.setLevel(logging.INFO)


def main():
    # Inform systemd that we've finished our startup sequence...
	# n = sdnotify.SystemdNotifier()
	log.info("READY=1")

	count = 1
	while True:
		log.info("Running... {}".format(count))
		log.info("STATUS=Count is {}".format(count))
		count += 1
		time.sleep(2)


if __name__ == "__main__":
    log.info("Test starting up...")
    main()

