use std::io;

fn main() {
    let mut buffer = String::new();
    let _ = io::stdin().read_line(&mut buffer);
    let buffer: Vec<&str> = buffer.trim().split_whitespace().collect();
    let a: i32 = buffer[0].parse().expect("");
    let b: i32 = buffer[1].parse().expect("");
    let d: i32 = buffer[2].parse().expect("");
    let mut ans: Vec<i32> = Vec::new();
    for i in (a..=b).step_by(d as usize) {
        ans.push(i)
    }
    println!("{}", ans.iter().map(|&s| s.to_string()).collect::<Vec<String>>().join(" "));

}
