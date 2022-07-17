import bangla_sandhi as bs
import clipboard as cb
import bangla_sandhi_samples as samples


def sandhi_adder_tester(examples):
    print('\nSandhi Adder: ')
    i = 0
    for item in examples:
        i += 1
        words = item.split('+')
        word_1 = words[0].strip()
        word_2 = words[1].strip()
        # print(word_1, word_2)
        result = bs.sandhi_adder(word_1, word_2)
        print(f'{i}: {word_1} + {word_2} = {result} ')
    print('==========================================================================')


def sandhi_splitter_tester(examples):
    print('\nSandhi Splitter: ')
    i = 0
    for item in examples:
        i += 1
        item = item.strip()
        result = bs.sandhi_splitter(item)
        print(f'{i}: {item} = {result}')
    print('==========================================================================')


def sandhi_tester_2():
    first_input = input("Enter the first word: ")
    second_input = input("Enter the second word: ")
    output = bs.sandhi_adder(first_input, second_input)
    print('Result:', output)


def save_samples():
    bangla_sandhi_samples = cb.swara_sandhi_ex + cb.byanjan_sandhi_ex + cb.bisarga_sandhi_ex + cb.misc_ex
    n = len(bangla_sandhi_samples)
    for i in range(n):
        bangla_sandhi_samples[i] = bangla_sandhi_samples[i].replace(' ', '').replace('\u200c', '')
    save_variable_to_file('bangla_sandhi_samples.py', 'bangla_sandhi_samples', bangla_sandhi_samples)


def refresh_word_library():
    bangla_words = {}
    for item in samples.bangla_sandhi_samples:
        words = item.split('+')
        word_1 = words[0].strip()
        word_2 = words[1].strip()
        if word_1 not in bangla_words:
            bangla_words[word_1] = True
        if word_2 not in bangla_words:
            bangla_words[word_2] = True

    save_variable_to_file('bangla_word_library.py', 'bangla_words', bangla_words)


def save_variable_to_file(file_name='unnamed.py', var_name='var', var=None):
    """
    Save var to "file_name" by the name "var_name"
    """
    file = open(file_name, "w", encoding="utf-8")
    to_write = '' + var_name + ' = ' + repr(var) + '\n'
    file.write(to_write)
    file.close()


def create_word_library():
    save_samples()
    refresh_word_library()


def generate_patterns(sandhi_rules):
    sandhi_patterns = {}
    for rule in sandhi_rules:
        pattern = sandhi_rules[rule]
        if pattern in sandhi_patterns:
            sandhi_patterns[pattern].append(rule)
        else:
            sandhi_patterns[pattern] = [rule]

    # print(sandhi_patterns)
    # print(len(sandhi_rules))
    # print(len(sandhi_patterns))
    #
    # i = 0
    # for item in sandhi_patterns:
    #     i += len(sandhi_patterns[item])
    # print(i)

    print('\nPatterns: ')
    for item in sandhi_patterns:
        print(f"'{item}':{sandhi_patterns[item]},")


