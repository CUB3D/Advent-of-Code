pub struct PasswordEnt {
    pub min: i32,
    pub max: i32,
    pub char: char,
    pub pass: String,
}

#[aoc_generator(day2)]
pub fn input_generator(input: &str) -> Vec<PasswordEnt> {
    input
        .lines()
        .map(|l| {
            let (min, l) = l.split_once("-").unwrap();
            let (max, l) = l.split_once(" ").unwrap();
            let (char, l) = l.split_once(":").unwrap();
            let (_, pass) = l.split_once(" ").unwrap();

            PasswordEnt {
                min: min.parse::<i32>().unwrap(),
                max: max.parse::<i32>().unwrap(),
                char: char.to_string().chars().next().unwrap(),
                pass: pass.to_string(),
            }
        })
        .collect()
}

#[aoc(day2, part1)]
pub fn part1(input: &[PasswordEnt]) -> i32 {
    input
        .iter()
        .filter(|p| {
            let ch = p
                .pass
                .chars()
                .filter(|pc| *pc == p.char)
                .collect::<Vec<_>>();
            ch.len() as i32 <= p.max && ch.len() as i32 >= p.min
        })
        .count() as i32
}

#[aoc(day2, part2)]
pub fn part2(input: &[PasswordEnt]) -> i32 {
    input
        .iter()
        .filter(|p| {
            let a = p.pass.chars().nth(p.min as usize - 1).unwrap() == p.char;
            let b = p.pass.chars().nth(p.max as usize - 1).unwrap() == p.char;

            a ^ b
        })
        .count() as i32
}

#[cfg(test)]
mod tests {}
