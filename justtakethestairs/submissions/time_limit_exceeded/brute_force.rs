use std::io::{self, BufRead, BufReader};
use std::cmp;
use std::collections::HashSet;

fn main() {
    let stdin = io::stdin();
    let mut lines = BufReader::new(stdin.lock()).lines();
    let line = lines.next().unwrap().unwrap();
    let mut iter = line.split_whitespace();
    let N: usize = iter.next().unwrap().parse().unwrap();
    let C: i64 = iter.next().unwrap().parse().unwrap();
    let mut S = vec![0i64; N+1];
    let mut F = vec![0i64; N+1];
    for i in 1..=N {
        let line = lines.next().unwrap().unwrap();
        let mut iter = line.split_whitespace();
        S[i] = iter.next().unwrap().parse().unwrap();
        F[i] = iter.next().unwrap().parse().unwrap();
    }

    let mut best = 1_000_000_000;
    let mut stack = vec![(1, 0)];
    while stack.len() != 0 {
        let (start, cost) = stack.pop().unwrap();
        if start > N {
            best = cmp::min(best, cost);
            continue;
        }
        let mut students = 0;
        let mut floors: HashSet<i64> = HashSet::new();
        for end in start..=N {
            students += S[end];
            if students > C {
                break;
            }
            floors.insert(F[end]);
            let max_floor = *floors.iter().max().unwrap();
            let stops = floors.len() as i64;
            let mut trip_cost = max_floor + stops + max_floor;
            if end == N {
                trip_cost -= max_floor;
            }
            stack.push((end + 1, cost + trip_cost))
        }
    }
    println!("{}", best);
}