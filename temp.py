import sys

def main():
    temp = " ".join(sys.argv[1:])
    # print(len(temp))
    # print(sys.argv[1:])
    print(temp)
    shortened_temp = temp.split(",")
    print(shortened_temp)
    # print(sys.argv[1:])

main()
