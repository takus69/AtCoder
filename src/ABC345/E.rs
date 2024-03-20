#[derive(Clone, Copy, Debug)]
struct VC {
    v: i64,
    c: i64,
}

impl VC {
    fn new(v: i64, c: i64) -> Self {
        VC { v, c }
    }
}

#[derive(Clone, Copy, Debug)]
struct Top2 {
    vc1: VC,
    vc2: VC,
}

impl Top2 {
    fn new() -> Self {
        Top2 {
            vc1: VC::new(-1, -1),
            vc2: VC::new(-1, -1),
        }
    }

    fn add_vc(&mut self, vc: VC) {
        let mut tmp = vc;
        if self.vc2.v < vc.v {
            std::mem::swap(&mut self.vc2, &mut tmp);
        }
        if self.vc1.v < self.vc2.v {
            std::mem::swap(&mut self.vc1, &mut self.vc2);
        }
        if self.vc1.c == self.vc2.c {
            std::mem::swap(&mut self.vc2, &mut tmp);
        }
    }

    fn add_top2(&mut self, top2: &Top2) {
        self.add_vc(top2.vc1);
        self.add_vc(top2.vc2);
    }
}

fn main() {
    let mut input_line = String::new();
    std::io::stdin().read_line(&mut input_line).unwrap();
    let mut parts = input_line.split_whitespace();
    let n: usize = parts.next().unwrap().parse().unwrap();
    let k: usize = parts.next().unwrap().parse().unwrap();

    let mut c = Vec::with_capacity(n);
    let mut v = Vec::with_capacity(n);
    for _ in 0..n {
        input_line.clear();
        std::io::stdin().read_line(&mut input_line).unwrap();
        let mut parts = input_line.split_whitespace();
        let ci: i64 = parts.next().unwrap().parse().unwrap();
        let vi: i64 = parts.next().unwrap().parse().unwrap();
        c.push(ci);
        v.push(vi);
    }

    let mut dp = vec![Top2::new(); k + 1];
    dp[0].add_vc(VC::new(0, -1));

    for i in 1..=n {
        let vi = v[i - 1];
        let ci = c[i - 1];
        let mut old = vec![Top2::new(); k + 1];
        std::mem::swap(&mut dp, &mut old);
        for j in 0..=k {
            if old[j].vc1.c == ci {
                if old[j].vc2.v >= 0 {
                    dp[j].add_vc(VC::new(old[j].vc2.v + vi, ci));
                }
            } else {
                if old[j].vc1.v >= 0 {
                    dp[j].add_vc(VC::new(old[j].vc1.v + vi, ci));
                }
            }
            if j > 0 {
                dp[j].add_top2(&old[j-1]);
            }
        }
    }

    println!("{}", dp[k].vc1.v);
}
