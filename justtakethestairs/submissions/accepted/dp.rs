use std::io::{self, BufRead, BufReader};
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

    let mut solution = vec![1_000_000_000i64; N+1]; //Same problem as kotlin solution
    solution[0] = 0;

    for i in 1..=N {
        let mut students: i64 = 0;
        let mut floors: HashSet<i64> = HashSet::new();
        for j in (0..i).rev() {
            students += S[j+1];
            if students > C {
                break;
            }
            floors.insert(F[j+1]);
            let max_floor = *floors.iter().max().unwrap();
            let stops = floors.len() as i64;
            let mut trip_cost = max_floor + stops + max_floor;
            if i == N {
                trip_cost -= max_floor;
            }
            if solution[j] + trip_cost < solution[i] {
                solution[i] = solution[j] + trip_cost
            }
        }
    }
    print!("{}", solution[N])
}