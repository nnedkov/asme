##########################################
#   Filename: import_strings_script.py   #
#   Nedko Stefanov Nedkov                #
#   nedko.stefanov.nedkov@gmail.com      #
#   December 2013                        #
##########################################

''' Import strings from external source '''

from db_api import set_strings



def get_strings_from_ext_source():
    file_name = './vocab.nytimes.txt'
    strings = [string.rstrip('\n') for string in open(file_name, 'r')]

    return strings


if __name__ == '__main__':
    ext_strings = get_strings_from_ext_source()
    strings = list()
    not_strings = list()

    for string in ext_strings:
        if isinstance(string, str):
            strings.append(string)
        else:
            not_strings.append(string)

    if strings:
        set_strings(strings)

    if not_strings:
        print 'Non-alphanumeric data (hence not stored): %s' % not_strings
