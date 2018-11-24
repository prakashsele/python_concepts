"""
Program to parse and validate csv file
format1:
Lastname, Firstname, (703)-742-0996, Blue, 10013
format2:
Firstname Lastname, Red, 11237, 703 955 0373
format3:
Firstname, Lastname, 10013, 646 111 0101, Green
"""
from __future__ import with_statement
# from   file     import       class
import re  # Process regular expressions (search for a pattern)
import json  # To handle json conversion
import operator  # Sort function

"""
Check_format function takes list of elements and
returns format type.
"""


def check_format(element_list):
    len_list = len(element_list)
    if len_list == 5:
        check_code = re.match('\d{5}$', element_list[4])
        if check_code is not None:
            return 1  # format 1

        check_code = re.match('\d{5}$', element_list[2])
        if check_code is not None:
            return 3  # format 3

    elif len_list == 4:
        check_code = re.match('\d{5}$', element_list[2])
        if check_code is not None:
            return 2  # format 2

    return -1  # This indicates invalid format


"""
Validate_phone function takes phone number and
returns 1 if valid else 0
"""


def validate_phone(phone):
    phone_regex = re.compile(r'^([0-9\(\)\/\+ \-]*)$', re.VERBOSE)
    if phone_regex.match(phone) is not None:
        return 1
    return 0


##Main program starts here##

# Required Variables
line_number = 0
all_entries = {}
entries = []
errors = []

# opening file and reading line by line
print("Program to parse file and write json to other file")
print("Started..")
try:
    with open("data.txt") as fp:
        for line in fp:
            entry = {}
            element_list = line.rstrip().split(',')
            element_list = [x.lstrip().rstrip() for x in element_list]
            format_type = check_format(element_list)
            if format_type == 1:
                if validate_phone(element_list[2]):
                    entry['color'] = element_list[3]
                    entry['firstname'] = element_list[1]
                    entry['lastname'] = element_list[0]
                    entry['phonenumber'] = element_list[2]
                    entry['zipcode'] = element_list[4]
                    entries.append(entry)
            elif format_type == 2:
                if validate_phone(element_list[3]):
                    entry['color'] = element_list[1]
                    entry['firstname'] = element_list[0].split(' ')[0]
                    entry['lastname'] = element_list[0].split(' ')[1]
                    entry['phonenumber'] = element_list[3]
                    entry['zipcode'] = element_list[2]
                    entries.append(entry)

            elif format_type == 3:
                if validate_phone(element_list[3]):
                    entry['color'] = element_list[4]
                    entry['firstname'] = element_list[0]
                    entry['lastname'] = element_list[1]
                    entry['phonenumber'] = element_list[3]
                    entry['zipcode'] = element_list[2]
                    entries.append(entry)
            else:
                errors.append(line_number)

            line_number += 1

    all_entries['errors'] = errors
    entries.sort(key=operator.itemgetter('lastname', 'firstname'))
    all_entries['entries'] = entries

    try:
        json_file = open("result.json", "w")
        json_file.write(json.dumps(all_entries, sort_keys=True, indent=2))
        json_file.close()
    except IOError:
        print('An error occured trying to Write json file.')

except IOError:
    print('An error occured trying to read the file.')

except ValueError:
    print('Non-numeric data found in the file.')

except ImportError:
    print("NO module found")

except EOFError:
    print('EOF error occured')

except KeyboardInterrupt:
    print('Operation cancelled by user')

except:
    print('An error occured. '
          '\nAdd required exception to handle it')

else:
    print("Program completed Successfully.."
          "\nCheck result.json in your current directory")
