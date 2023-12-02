pub fn next_number1(input: &str) -> Option<(&str, Option<i64>)> {
    if input.is_empty() {
        return None;
    }

    let c = input.chars().next().unwrap();

    if c.is_numeric() {
        Some((&input[1..], Some(c.to_string().parse().unwrap())))
    } else {
        Some((&input[1..], None))
    }
}

pub fn next_number2(input: &str) -> Option<(&str, Option<i64>)> {
    if input.is_empty() {
        return None;
    }

    let c = input.chars().next().unwrap();

    if c.is_numeric() {
        Some((&input[1..], Some(c.to_string().parse().unwrap())))
    } else {
        let words = [
            ("one", 1),
            ("two", 2),
            ("three", 3),
            ("four", 4),
            ("five", 5),
            ("six", 6),
            ("seven", 7),
            ("eight", 8),
            ("nine", 9),
        ];

        for (name, val) in words {
            if input.starts_with(name) {
                return Some((&input[name.len()..], Some(val)))
            }
        }

        Some((&input[1..], None))
    }
}


#[aoc_generator(day1)]
pub fn input_generator(input: &str) -> String {
    input.to_string()
}

#[aoc(day1, part1)]
pub fn part1(input: &str) -> i64 {
    input.lines().map(|l| {
        let mut numbers = Vec::new();

        let mut input = l;
        while let Some((next, num)) = next_number1(input) {
            if let Some(num) = num {
                numbers.push(num);
            }
            input = next;
        }

        let last = numbers.last().unwrap();
        let first = numbers.first().unwrap();

        format!("{first}{last}").parse::<i64>().unwrap()
    }).sum()
}

#[aoc(day1, part2)]
pub fn part2(input: &str) -> i64 {
    input.lines().map(|l| {
        let l = l.trim();

        let mut inp = l;
        let first = loop {
            if let Some((_, Some(num))) = next_number2(inp) {
                break num;
            }
            inp = &inp[1..];
        };

        let mut offset = 0;
        let last = loop {
            if let Some((_, Some(num))) = next_number2(&l[l.len() - offset..]) {
                break num;
            }
            offset += 1;
        };

       // println!("{input} = {first}:{last}");

        format!("{first}{last}").parse::<i64>().unwrap()
    }).sum()
}

#[cfg(test)]
mod tests {
    use crate::day1::{part1, part2};

    #[test]
    fn sample1() {


        assert_eq!(part2("two1nine"), 29);
        assert_eq!(part2("eightwothree"), 83);
        assert_eq!(part2("abcone2threexyz"), 13);
        assert_eq!(part2("xtwone3four"), 24);
        assert_eq!(part2("4nineeightseven2"), 42);
        assert_eq!(part2("zoneight234"), 14);
        assert_eq!(part2("7pqrstsixteen"), 76);
        assert_eq!(part2("oneight"), 18);
        assert_eq!(part2("1abc2"), 12);
        assert_eq!(part2("pqr3stu8vwx"), 38);
        assert_eq!(part2("a1b2c3d4e5f"), 15);
        assert_eq!(part2("treb7uchet"), 77);
        assert_eq!(part2("99lbqpxzzlbtvkmfrvrnmcxttseven"), 97);
        assert_eq!(part2("q7cnfslbtpkvseven"), 77);
        assert_eq!(part2("four98"), 48);
        assert_eq!(part2("xcntwone4633sixmkm1nine"), 29);
        assert_eq!(part2("3eightlrrlgck967"), 37);
        assert_eq!(part2("fivexpx1vsrreightkp7dph"), 57);
        assert_eq!(part2("eightwo"), 82);
    }
}
