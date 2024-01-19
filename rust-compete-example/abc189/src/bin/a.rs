use proconio::{input, marker::Chars};

fn main() {
    input! { ss: Chars }
    if ss[0] == ss[1] && ss[1] == ss[2] {
        println!("Won");
    } else {
        println!("Lost");
    }
}

