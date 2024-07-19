#[aoc_generator(day1)]
pub fn input_generator(input: &str) -> Vec<i32> {
    input.lines().map(|l| l.parse::<i32>().unwrap()).collect()
}

#[aoc(day1, part1)]
pub fn part1(input: &[i32]) -> i32 {
    input.windows(2).filter(|w| w[0] < w[1]).count() as i32
}

#[aoc(day1, part2)]
pub fn part2(input: &[i32]) -> i32 {
    input.windows(4).filter(|&w| &w[..3].iter().sum::<i32>() < &w[1..].iter().sum()).count() as i32
}

#[cfg(test)]
mod tests {
    use crate::day1::{part1, part2};

    #[test]
    fn sample1() {
        assert_eq!(part1(&[199,
                         200,
                         208,
                         210,
                         200,
                         207,
                         240,
                         269,
                         260,
                         263]), 7);
    }

    #[test]
    fn sample2() {
        assert_eq!(part2(&[199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263]), 5);
    }
}
