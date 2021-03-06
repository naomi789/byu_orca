import logging
import nltk
import string
from nltk.corpus import stopwords
from operator import itemgetter
from collections import defaultdict
from data_structures import professor_names, staff_names
from new_constants import ques_num_to_shorthand
import os


def graph_string(question, people):
    logging.info("graph string")
    f = open('results_at_BYU/strings/' + question + '.txt', 'w', encoding='utf-8')
    f.write("question: " + question + '\n\n')
    string_value = defaultdict(int)
    for person in people:
        value = getattr(person, question)
        if value != "":
            string_value[value] += 1

    for key in string_value.keys():
        f.write(str(key) + ": " + str(string_value[key]))
        f.write('\n')
    f.close()


def long_text(question, people):
    logging.info("graph long text")
    f = open('results_at_BYU/strings/' + question + '.txt', 'w')
    f.write("question: " + question + '\n\n')
    for person in people:
        value = getattr(person, question)
        if value != "":
            f.write(value)
            f.write('\n')
            f.write('\n')

    f.close()


def associate_with_professors(df, pos_neg_sug):
    f = open(f'panda_BYU_results/strings/professors_{ques_num_to_shorthand[pos_neg_sug]}.txt', 'w', encoding='utf-8')

    all_names = staff_names + professor_names + [first.split(' ', 1)[0] for first in staff_names] + [
        first.split(' ', 1)[0] for first in professor_names] + [last.split(' ', 1)[1] for last in staff_names] + [
                    last.split(' ', 1)[1] for last in professor_names]

    existing_comments = df.dropna(subset=[pos_neg_sug])
    existing_comments = existing_comments[pos_neg_sug]
    existing_comments = existing_comments.str.lower()

    name_to_comment = defaultdict(list)
    for comment in existing_comments:
        for name in all_names:
            # prevents 'running' from matching with dr. ng and 'frankly' from matching with frank
            # except, this also looses 'seppi.' or typo'd names like 'dr.barker '
            if (' ' + name + ' ' in comment) or (name + ',' in comment) or (name + '.' in comment):
                no_new_lines = comment.replace('\n', ' ')
                name_to_comment[name].append(no_new_lines.replace(name, name.upper()))


    for name in name_to_comment.keys():
        f.write(f'\nname: {name} {pos_neg_sug}: {name_to_comment[name].__len__()}')
    f.write('\n\n')

    for name in name_to_comment.keys():
        f.write(f'name: {name}\n')
        for value in name_to_comment[name]:
            f.write(f'comment: {value}\n\n')
        f.write('\n\n\n')
    f.close()


def find_common_words(df, pos_neg_sug, split_on_var):
    existing_comments = df.dropna(subset=[pos_neg_sug])
    existing_comments = existing_comments[pos_neg_sug]

    words_to_counts = {}
    for comment in existing_comments:
        words_to_counts = update_words_counts(words_to_counts, comment)
    print_common_words(words_to_counts, pos_neg_sug)


def print_common_words(words_to_counts, pos_neg_sug):
    os.makedirs(f'panda_BYU_results/strings/', exist_ok=True)
    f = open(f'panda_BYU_results/strings/{ques_num_to_shorthand[pos_neg_sug]}.txt', 'w')
    for key, value in sorted(words_to_counts.items(), key=itemgetter(1), reverse=True):
        if value >= 5:
            f.write(key + ': ' + str(value) + '\n')
        else:
            f.close()
            return
    f.close()


def update_words_counts(words_to_counts, response):
    set(stopwords.words('english'))
    stop_words = set(stopwords.words('english'))

    translator = str.maketrans('', '', string.punctuation)

    paragraph = response.split()
    filtered_paragraph = [w.lower().translate(translator) for w in paragraph if w.lower().translate(translator) not in stop_words]  #

    for word in filtered_paragraph:
        if words_to_counts.__contains__(word):
            words_to_counts[word] += 1
        else:
            words_to_counts[word] = 1

    return words_to_counts
