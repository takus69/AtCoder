import subprocess
import json


def run(i):
    output_str = subprocess.run(f'powershell cat in/{i:04}.txt | tester.exe python A.py > out/{i:04}_out.txt', shell=True, capture_output=True, text=True).stderr
    result = json.loads(output_str.split('\n')[0].replace("'", '"'))
    return result


if __name__ == '__main__':
    i = 0
    result = run(i)
    print('score:', result['score'])
    print(subprocess.run(f'powershell cat in/{i:04}.txt | tester.exe python A.py > out/{i:04}_out.txt', shell=True, capture_output=True, text=True).stderr)
