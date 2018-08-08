import logging
from collections import defaultdict
from list_constants import professor_names, staff_names

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


def associate_with_professors(people, pos_neg_feedback):
    f = open('results_at_BYU/strings/file_name' + pos_neg_feedback + '.txt', 'w', encoding='utf-8')

    all_names = staff_names + professor_names + [first.split(' ', 1)[0] for first in staff_names] + [
        first.split(' ', 1)[0] for first in professor_names] + [last.split(' ', 1)[1] for last in staff_names] + [
                    last.split(' ', 1)[1] for last in professor_names]

    name_to_comment = defaultdict(list)
    for person in people:
        if pos_neg_feedback == 'describe_positive_experience':
            comment = getattr(person, 'describe_positive_experience').lower()
        elif pos_neg_feedback == 'describe_negative_experience':
            comment = getattr(person, 'describe_negative_experience').lower()

        for name in all_names:
            # prevents 'running' from matching with dr. ng and 'frankly' with frank
            # except, this also looses 'seppi.' or typo'd names like 'dr.barker '
            if ' ' + name + ' ' in comment:
                no_new_lines = comment.replace('\n', ' ')
                name_to_comment[name].append(no_new_lines.replace(name, name.upper()))

    for name in name_to_comment.keys():
        f.write('\nname: ' + name +' ' + pos_neg_feedback + ': ' + str(name_to_comment[name].__len__()))

    f.write('\n')

    for name in name_to_comment.keys():
        f.write('name: ' + name + '\n')
        for value in name_to_comment[name]:
            f.write('comment: ' + value + '\n\n')
        f.write('\n\n\n')
    f.close()

