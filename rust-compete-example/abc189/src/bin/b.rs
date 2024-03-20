use proconio::input;

fn main() {
    input! {
        n: usize,  // アイテムの総数
        x: u64,    // 特定の閾値または制限
        vp: [(u64, u64); n],  // 各アイテムとそのパーセンテージのリスト
    }

    let mut total_alcohol = 0;
    for (i, (v, p)) in vp.into_iter().enumerate() {
        total_alcohol += v * p;
        if total_alcohol > x * 100 {
            println!("{}", i + 1);
            return;
        }
    }

    println!("{}", -1);
}

