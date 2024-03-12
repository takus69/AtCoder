import subprocess
import json


if __name__ == '__main__':
    i = 10
    # 実行テスト
    output_str =subprocess.run(f'powershell cat in/{i:04}.txt | tester.exe python C5.py > out/{i:04}.txt', shell=True, capture_output=True, text=True).stderr
    print(output_str)
