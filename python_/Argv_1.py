import sys

if __name__ == '__main__':
	if len(sys.argv) == 1:    
		print("Es necesario colocar por lo menos un argumento")
	else:
		print(sys.argv[1])
