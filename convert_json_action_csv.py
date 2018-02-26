import sys
import json
import csv
import random

# output: default output to stdout, if given a filename then will output to the file
def convert_file(file_name, output = None):
    print("Reading " + file_name)
    data = json.load(open(file_name)) # TODO check file exists
    output_results(list(map(convert_question, data)), output)

def output_results(data, output):
    if output is None:
        print(data)
        return

    with open(output, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

# returns an array with [question, answer, incorrect, incorrect]
def convert_question(question):
    q = question["question"]
    answer_index = question["answer"]
    answer = question[answer_index]
    return [q, answer] + pick_incorrects(question, answer_index)

def pick_incorrects(question, answer_index):
    choices = filter(lambda k: k not in ["question", answer_index, "answer"], question.keys())
    selected = random.sample(set(choices), 2)
    return map(lambda x: question[x], selected)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Please pass json file as argument.")
        sys.exit()
    convert_file(sys.argv[1], sys.argv[2] if len(sys.argv) >= 3 else None)