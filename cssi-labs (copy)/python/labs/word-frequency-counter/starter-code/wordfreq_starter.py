

def read_process_data():
    with open('third_party/jane-eyre.txt') as f:
        # the following line
        # - joins each line in the file into one big string
        # - removes all newlines and carriage returns
        # - converts everything to lowercase
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content


# You do not need to call this function unless you are doing level 3
def get_stop_words():
    with open('stop-words.txt') as f:
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content.split(' ')

def get_highest_words(counts_dictionary, count):
    highest = sorted(counts_dictionary.items(), key=lambda x:x[1])[::-1][:count]
    for word in highest:
        print("%s: %s" % (word[0], word[1]))


content = read_process_data()
stop_words = get_stop_words()

# Write your solution below!
word_count = {}

words = content.split(" ")

for word in words:
    if word_count.has_key(word):
        word_count[word] = word_count[word] + 1
    else:
        if word != "" and word not  in stop_words:
            word_count[word] = 1

get_highest_words(word_count,10)
