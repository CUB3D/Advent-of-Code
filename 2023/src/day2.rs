#[derive(Copy, Clone, Debug, Default)]
struct Round {
    blue: u64,
    red: u64,
    green: u64,
}

#[derive(Clone, Debug, Default)]
struct Game {
    id: u64,
    rounds: Vec<Round>,
}

#[aoc_generator(day2)]
pub fn input_generator(input: &str) -> Vec<Game> {
    input.lines().map(|l| {
        let input = l.trim().to_string();
        let input = input.replace("Game ", "");
        let mut id_parts = input.split(":");
        let id = id_parts.next().unwrap().parse::<u64>().unwrap();

        let mut rounds_data = Vec::new();

        let games = id_parts.next().unwrap();
        let rounds = games.split(";");

        for round in rounds {
            let round = round.trim();

            let cubes = round.split(", ");

            let mut round_data = Round::default();

            for cube in cubes {
                let mut parts = cube.split(" ");
                let count = parts.next().unwrap().parse::<u64>().unwrap();
                let name = parts.next().unwrap();

                match name {
                    "red" => round_data.red = count,
                    "green" => round_data.green = count,
                    "blue" => round_data.blue = count,
                    _ => panic!("what"),
                }
            }

            rounds_data.push(round_data);
        }

        Game {
            id,
            rounds: rounds_data,
        }
    }).collect::<Vec<_>>()
}

#[aoc(day2, part1)]
pub fn part1(input: &[Game]) -> u64 {
    input.iter().filter(|g| {
        for round in &g.rounds {
            if round.red > 12 || round.blue > 14 || round.green > 13 {
                return false;
            }
        }

        true
    }).map(|g| g.id).sum()
}

#[aoc(day2, part2)]
pub fn part2(input: &[Game]) -> u64 {
    input.iter().map(|g| {
        let mut max_round = Round::default();

        for round in &g.rounds {
            if round.red > max_round.red {
                max_round.red = round.red;
            }
            if round.green > max_round.green {
                max_round.green = round.green;
            }

            if round.blue > max_round.blue {
                max_round.blue = round.blue;
            }
        }

        max_round.red * max_round.blue * max_round.green
    }).sum()
}
