import sys

argv = sys.argv[1:]
argc = len(argv)

if argc == 0:
    print("Number of argument(s): 0.")
else:
    print("Number of argument(s): {} argument{}".format(argc, "" if argc == 1 else "s"))
    for i in range(argc):
        print("{}: {}".format(i + 1, argv[i]))
