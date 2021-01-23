# import required packages and modules
import requests,json,csv
from collections import defaultdict 

'''
Part #1 : Using Python, convert the above tracker_wise JSON into frame_wise, as described in the problem statement. 
'''
def convert_json(data):
    temp_dict = {'frames' : defaultdict(list)}
    for trackers in data['answer_key']['video2d']['data']['trackers']:
            for frame in trackers['frames']:
                trackers['frames'][frame].update({'tracker_id':trackers['_id']})
                temp_dict['frames'][frame].append(trackers['frames'][frame])
    data['answer_key']['video2d']['data'] = temp_dict
    return data

'''
Part#2 : Programmatically using python, create a csv file having the following  structure for the above tracker_wise json
'''
def write_csv(path,filename,data):
    temp_out_list= []
    title_header = ['frame_id', 'tracking_id', 'label']
    for tracker in data['answer_key']['video2d']['data']['trackers']:
        for frame in tracker['frames']:
            temp_out_list.append({'frame_id':frame,'tracking_id':tracker['_id'],'label':tracker['frames'][frame]['label']})
    with open(path+"/"+filename+".csv", 'w') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = title_header) 
        writer.writeheader()
        writer.writerows(temp_out_list)
        
# Fetch JSON Data from URL
r = requests.get("https://api.jsonbin.io/b/5de5f9825f0db26ed6c0cede")
input_json = r.json()

# Function invoking for JSON TO CSV
write_csv("/home/tapl/Playment","test_json_to_csv",input_json)

# Function invoking for JSON Conversion
modified_json=convert_json(input_json)

'''For writing the modified JSON use below code'''
with open("output.json", "w") as outfile: 
    outfile.write(json.dumps(modified_json, indent = 4))