import tarfile, os, hashlib, pickle, argparse
from collections import namedtuple

questions_data_file = './questions_data.pkl'
QuestionData = namedtuple('QuestionData', 'hashed_url question_hash dataset entity_mapping question answer')


def map_questions_data(all_questions_paths):
    data = {}
    for questions_path in all_questions_paths:
        questions_file = tarfile.open(questions_path)

        for i, file in enumerate(questions_file.getmembers()):
            qd = create_question_data(questions_file, file)
            if not qd: continue
            hashed_url = qd.hashed_url
            if not hashed_url in data:
                data[hashed_url] = {'dataset': qd.dataset, 'mapping': qd.entity_mapping, 'questions_entities': set()}
            if 'questions' not in data[hashed_url]:
                data[hashed_url]['questions'] = {qd.question_hash: {'question': qd.question, 'answer': qd.answer}}
            else:
                data[hashed_url]['questions'][qd.question_hash] = {'question': qd.question, 'answer': qd.answer}
            data[hashed_url]['questions_entities'].add(qd.answer)
            if i%5000 == 0 and i!=0:
                    print("found "+str(i)+" questions")

    write_pickle(questions_data_file, data)
    print("successfully wrote questions data.")

def create_question_data(questions_file, file):
    if not file.path.endswith('.question'): return
    splited_path = file.path.split('/')
    dataset = splited_path[3]
    question_hash = splited_path[4].split('.')[0]
    entity_mapping, hashed_url, question, answer = find_question_attributes(questions_file, file)
    if not entity_mapping:
        print("couldn't find mapping for question hash " + question_hash)
        return
    return QuestionData(hashed_url, question_hash, dataset, entity_mapping, question, answer)
    
def find_question_attributes(questions_file, filename):
    f = questions_file.extractfile(filename)
    lines = [line.strip() for line in f.readlines()]
    hashed_url = hashhex(lines[0].strip())
    mapping = {}
    for idx, line in enumerate(reversed(lines)):
        try:
            key, value = line.decode().split(':', 1)
            mapping[key] = value
        except:
            question = lines[len(lines)- idx - 4].decode()
            answer = lines[len(lines)- idx - 2].decode()
            break
    return mapping, hashed_url, question, answer

def write_pickle(file, data):
    with open(file, 'wb') as f:
        pickle.dump(data, f, protocol=2)

def hashhex(s):
    h = hashlib.sha1()
    h.update(s)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser(description='Map Question Data/Create Anonymized datasets')
    parser.add_argument('--cnn_questions_path', required=True)
    parser.add_argument('--dm_questions_path', required=True)
    parser.add_argument('--stories_path')

    args = parser.parse_args()
    all_questions_paths = [args.cnn_questions_path, args.dm_questions_path]
    
    map_questions_data(all_questions_paths)

if __name__ == '__main__':
  main()

