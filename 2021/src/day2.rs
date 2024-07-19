pub enum Motion {
    F(u32),
    D(u32),
    U(u32),
}

#[aoc_generator(day2)]
pub fn input_generator(input: &str) -> Vec<Motion> {
    input.lines().map(|l| {
        let v = l.split(" ").nth(1).unwrap().parse::<u32>().unwrap();

        match l.split(" ").nth(0).unwrap() {
            "forward" => Motion::F(v),
            "down" => Motion::D(v),
            "up" => Motion::U(v),
            _ => panic!()
        }
    }).collect()
}

#[aoc(day2, part1)]
pub fn part1(input: &[Motion]) -> i32 {
    let mut h = 0;
    let mut d = 0;

    for i in input {
        match i {
            Motion::F(x) => {
                h += x
            }
            Motion::D(y) => {
                d += y;
            }
            Motion::U(y) => {
                d -= y;
            }
        }
    }

    (h * d) as i32
}

#[aoc(day2, part2)]
pub fn part2(input: &[Motion]) -> i32 {
    let mut h = 0;
    let mut d = 0;
    let mut aim = 0;

    for i in input {
        match i {
            Motion::F(x) => {
                h += x;
                d += aim * x;
            }
            Motion::D(y) => {
                aim += y;
            }
            Motion::U(y) => {
                aim -= y;
            }
        }
    }

    (h * d) as i32
}

#[cfg(test)]
mod tests {
    use crate::day2::{input_generator, part1, part2};

    #[test]
    fn sample1() {
        assert_eq!(part1(&input_generator("forward 5
down 5
forward 8
up 3
down 8
forward 2")), 150);
    }

    #[test]
    fn sample2() {
        assert_eq!(part2(&input_generator("forward 5
down 5
forward 8
up 3
down 8
forward 2")), 900);
    }
}
