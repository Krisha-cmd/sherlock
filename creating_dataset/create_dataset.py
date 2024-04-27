import pandas as pd
import re

def read_text_from_file(filename):
    with open(filename, "r", encoding='utf-8') as file:
        text = file.read()
    return text

text = read_text_from_file("creating_dataset/transcript.txt")

pattern = r'^(.*?):\s*((?:(?!\().)*)$'

matches = re.findall(pattern, text, re.MULTILINE)

data={
    'name':[],
    'line':[]
}

for match in matches:
    data['name'].append(match[0])
    data['line'].append(match[1])

cleaned_names = []
for name in data['name']:
    cleaned_name = re.sub(r'\s*\([^()]*\)', '', name) 
    cleaned_names.append(cleaned_name)

data['name']=cleaned_names


filtered_data = {'name': [], 'line': []}
for name, line in zip(data['name'], data['line']):
    if not name.startswith('('):
        filtered_data['name'].append(name)
        filtered_data['line'].append(line)


df = pd.DataFrame(filtered_data)
df.to_csv('creating_dataset/dataset.csv', index=False)

