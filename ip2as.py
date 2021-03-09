#!/usr/bin/python3
import sys
from Entry import Entry, is_valid_ip_add


def main():
    ip_database = []  # type [Entry]
    ip_inputs = []  # type [str]

    # get file names
    db_file_name = str(sys.argv[1])
    ip_file_name = str(sys.argv[2])

    # get files
    db_file = open(db_file_name, 'r')
    ip_file = open(ip_file_name, 'r')

    # parse db file
    print(f"importing {db_file_name} to database")
    while True:
        line = db_file.readline()
        if not line or line == "\n":
            break
        else:
            data = line.split(" ")
            ip_prefix = data[0]
            # check if ip_prefix is valid
            if not is_valid_ip_add(ip_prefix):
                print(f"invalid entry in database: {line.strip()}")
                continue

            prefix_length = int(data[1])
            as_number = data[2].strip()
            ip_prefix_bin = ''.join(map(lambda x: str(format(int(x), '08b')), ip_prefix.split(".")))[: prefix_length]
            ip_database.append(Entry(ip_prefix=ip_prefix,
                                     ip_prefix_bin=ip_prefix_bin,
                                     prefix_length=prefix_length,
                                     as_number=as_number))

    print("*******************************************")
    print(f"Start reading input file: {ip_file_name}")
    while True:
        line = ip_file.readline()
        if not line:
            break
        elif line == "\n":
            continue
        elif not is_valid_ip_add(line.strip()):
            print(f"invalid input: {line.strip()}")
        else:
            ip_inputs.append(line.strip())
    print("*******************************************")

    # sort ip_database based on prefix_length
    def sort_func(e: Entry):
        return e.prefix_length
    ip_database.sort(key=sort_func, reverse=True)

    for ip in ip_inputs:
        match = False
        for entry in ip_database:
            match_and_output = entry.is_match_and_output(ip)
            if match_and_output[0]:
                match = True
                print(match_and_output[1])
                break
        if not match:
            print("There is no match")


if __name__ == '__main__':
    main()
