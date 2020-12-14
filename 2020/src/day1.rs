#[aoc_generator(day1)]
pub fn input_generator(input: &str) -> Vec<i32> {
    input.lines().map(|l| l.parse::<i32>().unwrap()).collect()
}

#[aoc(day1, part1)]
pub fn part1(input: &[i32]) -> i32 {
    input
        .iter()
        .copied()
        .map(|i| {
            input
                .iter()
                .copied()
                .find(|i2| i2 + i == 2020)
                .map(|i2| i2 * i)
        })
        .find(|x| x.is_some())
        .unwrap()
        .unwrap()
}

#[aoc(day1, part2)]
pub fn part2(input: &[i32]) -> i32 {
    input
        .iter()
        .copied()
        .flat_map(|i| {
            input
                .iter()
                .copied()
                .map(|i2| {
                    input
                        .iter()
                        .copied()
                        .find(|i3| i3 + i2 + i == 2020)
                        .map(|i3| i3 * i2 * i)
                })
                .filter_map(|x| x)
                .collect::<Vec<_>>()
        })
        .next()
        .unwrap()
}

#[cfg(test)]
mod tests {
    use crate::day1::{part1, part2};

    #[test]
    fn sample1() {
        assert_eq!(part1(&[1721, 979, 366, 299, 675, 1456]), 514579);
    }

    #[test]
    fn sample2() {
        assert_eq!(part2(&[1721, 979, 366, 299, 675, 1456]), 241861950);
    }
}
