use std::io;
use std::collections::HashMap;

fn f(x: usize, memo: &mut HashMap<usize, usize>) -> usize {
    if let Some(&result) = memo.get(&x) {
        return result;
    }

    let mut result: usize = x;

    if x%2 == 0 {
        result += f(x/2, memo)*2;
    } else {
        result += f(x/2, memo) + f(x/2+1, memo);
    }
    memo.insert(x, result);
    result
}

fn main() {
    let mut buffer = String::new();
    let _ = io::stdin().read_line(&mut buffer);
    let n: usize = buffer.trim().parse().expect("Fail");

    let mut memo: HashMap::<usize, usize> = HashMap::new();
    memo.insert(1, 0);
    println!("{}", f(n, &mut memo));
}