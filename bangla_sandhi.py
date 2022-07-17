from bangla_sandhi_rules import *
from bangla_characters import *
from bangla_word_library import *


def bng_to_unicode(word):
    return word.encode('unicode_escape')


def unicode_to_bng(unicode_str):
    return unicode_str.decode('unicode_escape')


def get_last_char(word):
    return list(word)[-1]


def get_first_char(word):
    return list(word)[0]


def get_pattern(word_1, word_2):
    char_1 = get_last_char(word_1)
    char_2 = get_first_char(word_2)
    if char_1 in bangla_consonants:
        char_1 = 'অ'
    elif char_1 == '্':
        char_1 = word_1[-2]
    pattern = char_1 + '+' + char_2
    return pattern


def search_sandhi_rules(pattern):
    if pattern in swara_sandhi_rules:
        return swara_sandhi_rules[pattern]
    if pattern in byanjan_sandhi_rules:
        return byanjan_sandhi_rules[pattern]
    if pattern in bisarga_sandhi_rules:
        return bisarga_sandhi_rules[pattern]
    return None


def swara_sandhi_adder(word_1, word_2):
    pattern = get_pattern(word_1, word_2)
    joiner = search_sandhi_rules(pattern)
    if get_last_char(word_1) in bangla_consonants:
        part_1 = word_1
    else:
        part_1 = word_1[:-1]
    part_2 = word_2[1:]
    if joiner is not None:
        result = part_1 + joiner + part_2
        return result
    return '[ERROR: No rule found.]'


def byanjan_sandhi_adder(word_1, word_2):
    pattern = get_pattern(word_1, word_2)
    joiner = search_sandhi_rules(pattern)
    if get_last_char(word_1) == '্':
        part_1 = word_1[:-2]
    elif get_last_char(word_1) == 'ৎ':
        part_1 = word_1[:-1]
    else:
        part_1 = word_1
    part_2 = word_2[1:]
    if joiner is not None:
        result = part_1 + joiner + part_2
        return result
    return '[ERROR: No rule found.]'


def bisarga_sandhi_adder(word_1, word_2):
    return '[ERROR: No rule found.]'


def sandhi_adder(word_1, word_2):
    word_1 = word_1.strip()
    word_2 = word_2.strip()
    if word_1[-1] in ['্', 'ৎ'] or word_2[0] in bangla_consonants:
        return byanjan_sandhi_adder(word_1, word_2)
    if word_1[-1] in bangla_vowel_signs or word_1[-1] in bangla_consonants or word_1[-1] in bangla_vowels:
        return swara_sandhi_adder(word_1, word_2)
    if word_1[-1] == 'ঃ':
        return bisarga_sandhi_adder(word_1, word_2)
    return '[ERROR: No rule found.]'


################################################################################
# sandhi splitter
def sandhi_splitter(word):
    word = word.strip()
    possible_results = get_possible_results(word)
    final_result = filter_results(possible_results)
    no_of_results = len(final_result)
    if no_of_results == 0:
        return '[ERROR: Unable to split word]'
    final_result = repr(final_result).replace(',', ' /').replace('\'', '').strip('[]')
    return final_result


def get_possible_results(word):
    possible_patterns = find_patterns(word)
    possible_results = []
    for pattern, position in possible_patterns:
        possible_results.extend(split_word(word, pattern, position))
    return possible_results


def find_patterns(word):
    word_length = len(word)
    possible_patterns = []
    # all_sandhi_patterns = {}
    # all_sandhi_patterns.update(swara_sandhi_patterns)
    # all_sandhi_patterns.update(byanjan_sandhi_patterns)
    # all_sandhi_patterns.update(bisarga_sandhi_patterns)
    for i in range(1, word_length - 1):
        for pattern in all_sandhi_patterns:
            if word[i:].startswith(pattern):
                possible_patterns.append((pattern, i))
    return possible_patterns


def split_word(word, pattern, position):
    # print(word, pattern)
    rules = all_sandhi_patterns[pattern]
    # print(rules)
    if pattern in swara_sandhi_patterns:
        type = 1
    elif pattern in byanjan_sandhi_patterns:
        type = 2
    elif pattern in bisarga_sandhi_patterns:
        type = 3
    else:
        type = 0
    possible_results = []
    for rule in rules:
        possible_results.append(construct_words(word, pattern, rule, position, type))
    return possible_results


def construct_words(word, pattern, rule, position, type):
    suffix_1 = rule.split('+')[0]
    prefix_2 = rule.split('+')[1]
    if suffix_1 == 'অ':
        suffix_1 = ''
    word_1 = word[:position] + suffix_1
    if type == 2:
        word_1 += '্'
    # to-check - (lstrip() should be replaced with removeprefix() if python version 3.9+)
    word_2 = prefix_2 + word[position:].lstrip(pattern)
    # print(word_1, word_2)
    return f'{word_1} + {word_2}'


def filter_results(possible_results):
    final_result = []
    for result in possible_results:
        word_1 = result.split('+')[0].strip()
        word_2 = result.split('+')[1].strip()
        if word_1 in bangla_words and word_2 in bangla_words:
            final_result.append(result)
    # if not final_result:
    #     final_result = possible_results
    return final_result
