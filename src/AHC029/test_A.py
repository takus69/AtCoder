import subprocess


def run(i):
    output_str = subprocess.run(f'powershell cat in/{i:04}.txt | tester.exe python A.py > out/{i:04}_out.txt', shell=True, capture_output=True, text=True).stderr
    score = int(output_str.split()[-1])
    return score


if __name__ == '__main__':
    i = 1
    score = run(i)
    print('score:', score)
    print(subprocess.run(f'powershell cat in/{i:04}.txt | tester.exe python A.py > out/{i:04}_out.txt', shell=True, capture_output=True, text=True).stderr)
