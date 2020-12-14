use itertools::iproduct;




#[aoc_generator(day9)]
pub fn gen(input: &str) -> Vec<u64> {
    input.lines().map(|l| l.parse::<u64>().unwrap()).collect()
}

#[aoc(day9, part1)]
pub fn part1(instructions: &[u64]) -> i64 {
    // first 25 numbers
    let mut last_25 = instructions.iter().copied().take(25).collect::<Vec<_>>();

    for number in instructions.iter().skip(25).copied() {
        if let Some((_a, _b)) = iproduct!(last_25.iter().copied(), last_25.iter().copied())
            .find(|(a, b)| (*a + *b) == number)
        {
            last_25.push(number);
        } else {
            return number as i64;
        }
    }

    -1
}

#[aoc(day9, part2)]
pub fn part2(instructions: &[u64]) -> i64 {
    let part1 = part1(instructions);

    let mut pos = 0;

    loop {
        let mut pos2 = pos;
        let mut sum = 0;
        let mut nums = Vec::new();
        while sum < part1 {
            nums.push(instructions[pos2]);
            sum += instructions[pos2] as i64;
            pos2 += 1;
        }
        if sum == part1 {
            println!("Sum is {:?}", nums);
            return (nums.iter().max().unwrap() + nums.iter().min().unwrap()) as i64;
        }
        pos += 1;
    }
}

#[cfg(test)]
pub mod test {}
