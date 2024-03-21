import subprocess
import json


def run(i):
    output_str = subprocess.run(f'powershell cat in/{i:04}.txt | tester.exe python A.py > out/{i:04}.txt', shell=True, capture_output=True, text=True).stderr
    result = json.loads(output_str.split('\n')[0].replace("'", '"'))
    return result


if __name__ == '__main__':
    i = 0
    # 実行テスト
    output_str =subprocess.run(f'powershell cat in/{i:04}.txt | tester.exe python A.py > out/{i:04}.txt', shell=True, capture_output=True, text=True).stderr
    print(output_str)
    with open('output.txt', 'w') as f:
        f.write(output_str)

    # 単体スコア確認
    result = run(i)
    print('score:', result['score'])
