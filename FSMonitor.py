import pyinotify
import logging
import argparse
import getpass
import sys

class eventHandler(pyinotify.ProcessEvent):

	def process_IN_ACCESS(self, event):
		if args.file not in event.pathname and args.logLevel == 1:
			logging.info("ACCESS file: "+event.pathname)
		
		elif args.file not in event.pathname and args.logLevel == 0:
			docs = (event.pathname).split("/")

			for doc in docs:
				if doc.startswith("."):
					return None

			logging.info("ACCESS file: "+event.pathname)


	def process_IN_ATTRIB(self, event):
		if args.file not in event.pathname and args.logLevel == 1:
			logging.info("ATTRIB file: "+event.pathname)

		elif args.file not in event.pathname and args.logLevel == 0:
			docs = (event.pathname).split("/")

			for doc in docs:
				if doc.startswith("."):
					return None

			logging.info("ATTRIB file: "+event.pathname)

	def process_IN_CLOSE_NOWRITE(self, event):
		if args.file not in event.pathname and args.logLevel == 1:
			logging.info("CLOSE_NOWRITE file: "+event.pathname)

		elif args.file not in event.pathname and args.logLevel == 0:
			docs = (event.pathname).split("/")

			for doc in docs:
				if doc.startswith("."):
					return None

			logging.info("CLOSE_NOWRITE file: "+event.pathname)

	def process_IN_CLOSE_WRITE(self, event):
		if args.file not in event.pathname and args.logLevel == 1:
			logging.info("CLOSE_WRITE file: "+event.pathname)

		elif args.file not in event.pathname and args.logLevel == 0:
			docs = (event.pathname).split("/")

			for doc in docs:
				if doc.startswith("."):
					return None

			logging.info("CLOSE_WRITE file: "+event.pathname)

	def process_IN_CREATE(self, event):
		if args.file not in event.pathname and args.logLevel == 1:
			logging.info("CREATE file: "+event.pathname)

		elif args.file not in event.pathname and args.logLevel == 0:
			docs = (event.pathname).split("/")

			for doc in docs:
				if doc.startswith("."):
					return None

			logging.info("CREATE file: "+event.pathname)

	def process_IN_DELETE(self, event):
		if args.file not in event.pathname and args.logLevel == 1:
			logging.info(r"DELETE file: "+event.pathname)

		elif args.file not in event.pathname and args.logLevel == 0:
			docs = (event.pathname).split("/")

			for doc in docs:
				if doc.startswith("."):
					return None

			logging.info(r"DELETE file: "+event.pathname)

	def process_IN_MODIFY(self, event):
		if args.file not in event.pathname and args.logLevel == 1:
			logging.info("MODIFY file: "+event.pathname)

		elif args.file not in event.pathname and args.logLevel == 0:
			docs = (event.pathname).split("/")

			for doc in docs:
				if doc.startswith("."):
					return None

			logging.info("MODIFY file: "+event.pathname)

	def process_IN_OPEN(self, event):
		if args.file not in event.pathname and args.logLevel == 1:
			logging.info("OPEN file: "+event.pathname)

		elif args.file not in event.pathname and args.logLevel == 0:
			docs = (event.pathname).split("/")

			for doc in docs:
				if doc.startswith("."):
					return None

			logging.info("OPEN file: "+event.pathname)

def main():
	global args

	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", action="store", dest="file", required=True, help="specify the log file")
	parser.add_argument("-t", "--target", action="store", dest="target", nargs="+", required=True, help="specify paths to handle")
	parser.add_argument("-l", "--level", action="store", dest="logLevel", default=0, type=int, help="0 logs normals files; 1 logs also hidden files")
	args = parser.parse_args()

	if args.logLevel > 1 or args.logLevel < 0:
		parser.error("-l/--level reqire only 0 or 1")

	logging.basicConfig(level=logging.INFO, filename=args.file, filemode="a", format="%(asctime)s " + getpass.getuser() + "\t%(message)s", datefmt="%a, %d %b %Y %H:%M:%S")

	wm = pyinotify.WatchManager()

	for t in args.target:
		wm.add_watch(t, pyinotify.ALL_EVENTS, rec=True)

	eh = eventHandler()

	notifier = pyinotify.Notifier(wm, eh)
	notifier.loop()

if __name__ == '__main__':
	main()