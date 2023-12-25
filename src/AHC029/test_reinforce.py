import subprocess
import sys


def run(i):
    output_str = subprocess.run(f'powershell cat in/{i:04}.txt | tester.exe python reinforce.py > reinforce_out/{i:04}_out.txt', shell=True, capture_output=True, text=True).stderr
    print(output_str, file=sys.stderr)
    # score = int(output_str.split('\n')[0].split()[-1])
    return score


if __name__ == '__main__':
    i = 1
    score = run(i)
    print('score:', score)
    print(subprocess.run(f'powershell cat in/{i:04}.txt | tester.exe python reinforce.py > reinforce_out/{i:04}_out.txt', shell=True, capture_output=True, text=True).stderr)
