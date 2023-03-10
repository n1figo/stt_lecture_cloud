from pydub import AudioSegment
import os

# files
src = "transcript.mp3"
dst = "test.wav"

curr_path = os.getcwd()
input_path = os.path.join(curr_path, 'input_mp3')

## 
# print(input_path)

input_filename = [x for x in os.listdir(input_path) if 'mp3' in x][0]
# print("="*50)
# print(input_filename)
input_mp3_filename_path = os.path.join(input_path, input_filename)

# print("="*50)
# print(input_mp3_filename_path)

# convert wav to mp3
audSeg = AudioSegment.from_mp3(input_mp3_filename_path)

dst_path_filename = os.path.join('./output_mp3/', 'test.wav')
audSeg.export(dst_path_filename, format="wav")

print('wav 전환완료!!')