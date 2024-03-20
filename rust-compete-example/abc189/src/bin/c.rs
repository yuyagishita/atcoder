use proconio::*;

fn main() {
    input!{
        n: usize,
        mut a: [u32; n],
    }
    a.push(0);
    let mut ans: u32 = 0;
    let mut stack: Vec<(u32, u32)> = vec![];
    for a in a{
        let mut w: u32 = 0;
        while stack.last().map_or(false, |p: &(u32, u32)| p.0 >= a){
            let (a, b) = stack.pop().unwrap();
            w += b;
            ans = ans.max(a * w);
        }
        stack.push((a, w + 1));
    }
    println!("{:?}", ans);
}

