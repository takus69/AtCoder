use std::io;

fn main() {
    let mut buffer = String::new();
    let _ = io::stdin().read_line(&mut buffer);
    let n: usize = buffer.trim().parse().expect("Fail");
    let mut ans: Vec<usize> = Vec::new();
    for _ in 0..n {
        buffer.clear();
        let _ = io::stdin().read_line(&mut buffer).expect("Fail");
        let q: Vec<usize> = buffer.trim().split_whitespace().map(|s| s.parse().expect("Fail")).collect();
        if q[0] == 1 {
            ans.push(q[1]);
        } else {
            println!("{}", ans[ans.len()-q[1]]);
        }
    }
}
