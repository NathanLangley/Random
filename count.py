from counter import Counter
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--count", type=int, default=0,
	help="# the count starts at")
args = vars(ap.parse_args())
count = Counter(args["count"]).startCount()
while count.value() <= 1000000000:
	print(count.value()) 
	pass

print("done")
count.stopCount()

