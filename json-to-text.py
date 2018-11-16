import json

def get_speaker_by_timestamp(timestamp, speaker_timestamps):
    for item in speaker_timestamps:
        if item['from'] == timestamp:
            return str(item['speaker'])

with open ("watson.json") as json_file:
    json_string = json_file.read()
    json_string = json_string.replace('\t', '').replace('\n', ' ')
    data = json.loads(json_string)
f = open('formatted_text.txt', 'w+')
text = ""
text_data = data['results']
prev_speaker = ""
for each in text_data:
    first_timestamp = each['alternatives'][0]['timestamps'][0][1]
    cur_speaker = get_speaker_by_timestamp(first_timestamp, data['speaker_labels'])
    if cur_speaker != prev_speaker:
        f.write('\n\n' + cur_speaker + ': ')
        prev_speaker = cur_speaker
    f.write(each['alternatives'][0]['transcript'])

f.close()