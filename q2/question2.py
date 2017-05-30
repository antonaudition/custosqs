import datetime
import requests
import polling


def pretty_print(dct):
	# timestamp in milliseconds
	timestamp = datetime.datetime.fromtimestamp(
		dct["timestamp"] / 1000
	).strftime('%Y-%m-%d %H:%M:%S')
	print "{} Bid: {} Ask: {}".format(timestamp, dct["bid"], dct["ask"])


def poll(step, timeout):
	polling.poll(
		lambda: pretty_print(requests.get("https://api.mybitx.com/api/1/ticker?pair=XBTZAR").json()),
		step=step,
		timeout=timeout,
	)

poll(10, 120)
