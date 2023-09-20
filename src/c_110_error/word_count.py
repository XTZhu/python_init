
def count_word(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print('no such file or directory: ' + filename)
    except UnicodeDecodeError:
        print('decode error')
    else:
        words = contents.split()
        num_words = len(words)
        print('the file ' + filename + ' has about ' + str(num_words) + ' words.')
