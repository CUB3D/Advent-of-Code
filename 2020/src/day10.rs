use itertools::{Itertools};
use rayon::prelude::{ParallelIterator};


use std::collections::{HashMap};

#[aoc_generator(day10)]
pub fn gen(input: &str) -> Vec<u64> {
    input.lines().map(|l| l.parse::<u64>().unwrap()).collect()
}

#[aoc(day10, part1)]
pub fn part1(instructions: &[u64]) -> i64 {
    let sorted = instructions.iter().sorted().copied().collect::<Vec<_>>();

    let mut differences = Vec::new();

    for i in (0..instructions.len()).rev() {
        let big = sorted[i];

        let first = if i == 0 { 0 } else { sorted[i - 1] };

        let difference = big - first;
        differences.push(difference);
    }

    let one = differences.iter().copied().filter(|x| *x == 1).count();
    let three = differences.iter().copied().filter(|x| *x == 3).count() + 1;
    (one * three) as i64
}

pub fn tmp(instructions: &[u64]) -> bool {
    for i in (0..instructions.len()).rev() {
        let big = instructions[i];

        let first = if i == 0 { 0 } else { instructions[i - 1] };

        let difference = big - first;

        if difference < 0 || difference > 3 {
            return false;
        }
    }

    return true;
}

#[aoc(day10, part2)]
pub fn part2(instructions: &[u64]) -> i64 {
    let mut instructions = instructions.iter().copied().collect::<Vec<_>>();
    instructions.insert(0, 0);
    instructions.push(instructions.iter().max().unwrap() + 3);
    let instructions = instructions
        .iter()
        .copied()
        .sorted()
        .rev()
        .collect::<Vec<_>>();

    let mut scores = HashMap::new();

    for (key, num) in instructions.iter().enumerate() {
        let next_num = &instructions[0..key];
        let next_num = next_num.iter().rev().take(3).rev().collect::<Vec<_>>();

        if next_num.len() == 0 {
            scores.insert(num, 1);
            println!("Storing {}", num);
            continue;
        }

        scores.insert(num, 0);
        for next_number in next_num {
            if next_number - num <= 3 {
                scores.insert(num, scores[num] + scores[next_number]);
            }
        }
    }

    println!("scores: {:?}", scores);

    scores[&0]
}

#[cfg(test)]
pub mod test {
    use crate::day10::{gen, part1};

    #[test]
    pub fn first() {
        assert_eq!(
            part1(&gen(r#"16
10
15
5
1
11
7
19
6
12
4"#)),
            35
        );
    }
}
