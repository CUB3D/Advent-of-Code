use std::collections::HashSet;

#[aoc_generator(day6)]
pub fn gen(input: &str) -> Vec<Vec<HashSet<char>>> {
    input
        .split("\n\n")
        .map(|l| {
            l.lines()
                .map(|person_answers| person_answers.chars().collect::<HashSet<char>>())
                .collect()
        })
        .collect::<Vec<_>>()
}

#[aoc(day6, part1)]
pub fn part1(groups: &[Vec<HashSet<char>>]) -> u64 {
    groups
        .iter()
        .map(|group| {
            group
                .iter()
                .cloned()
                .flatten()
                .collect::<HashSet<_>>()
                .len()
        })
        .fold(0, |acc, x| acc + x as u64)
}

#[aoc(day6, part2)]
pub fn part2(groups: &[Vec<HashSet<char>>]) -> u64 {
    groups
        .iter()
        .map(|group| {
            let first_answers = &group[0];
            let common_answers = first_answers
                .iter()
                .filter(|answer| group.iter().all(|member| member.contains(answer)))
                .collect::<HashSet<_>>();
            common_answers.len()
        })
        .fold(0, |acc, x| acc + x as u64)
}
