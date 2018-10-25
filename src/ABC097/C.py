def run(s, K):
    '''
    ある文字から始まる文字列の数は、ある文字の位置から文字列sの最後までの長さとなる
    ただし、ある文字が文字列sに複数回出現する場合は、その分の考慮が必要
    aからzまで順に出現するsubstringの数を数える
    Kが範囲に入る文字の順をすべて数えることで、最終的な結果が得られる
    '''
    return (s, K)


def main():
    s = input()
    K = int(input())
    print(run(s, K))


if __name__ == '__main__':
    main()
