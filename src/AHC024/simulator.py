from A import solver


def fetch_input(input_file):
    in_f = open(input_file, 'r')
    n, m = [int(v) for v in in_f.readline().split(' ')]
    c = []
    for _ in range(n):
        c.append(list(map(int, in_f.readline().split())))
    in_f.close()
    return n, m, c

def output(d, output_file):
    out_f = open(output_file, 'w')
    for i in range(len(d)):
        out_f.write(' '.join(map(str, d[i]))+'\n')
    out_f.close()


if __name__ == '__main__':
    n, m, c = fetch_input('sample.txt')
    d = solver(n, m, c)
    output(d, 'sample_out.txt')

    n, m, c = fetch_input('seed0.txt')
    d = solver(n, m, c)
    output(d, 'seed0_out.txt')