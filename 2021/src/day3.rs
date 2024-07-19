use std::ops::Not;

#[aoc_generator(day3)]
pub fn input_generator(input: &str) -> Vec<Vec<u8>> {
    input.lines().map(|l| {
       l.chars().map(|c| if c == '1' {
           1
       } else { 0 }).collect::<Vec<_>>()
    }).collect()
}

#[aoc(day3, part1)]
pub fn part1(input: &[Vec<u8>]) -> usize {
    let bit_count = 12;

    let mut bit_counts = vec![0usize; bit_count];
    for line in input {
        for (index, bit) in line.iter().enumerate() {
            if *bit == 1 {
                bit_counts[index] += 1;
            }
        }
    }

    for i in 0..bit_count {
        if bit_counts[i] > input.len() / 2 {
            bit_counts[i] = 1;
        } else {
            bit_counts[i] = 0;
        }
    }

    println!("{:?}", bit_counts);

    if bit_count == 5 {
        let gamma_rate = bit_counts[0] << 4 | bit_counts[1] << 3 | bit_counts[2] << 2 | bit_counts[3] << 1 | bit_counts[4];
        let epsilon_rate = (gamma_rate as u8).not() & 0b00011111;
        println!("g: {}, e: {}", gamma_rate, epsilon_rate);
        gamma_rate as usize * epsilon_rate as usize
    } else {
        let gamma_rate = bit_counts[0] << 11 | bit_counts[1] << 10 | bit_counts[2] << 9 | bit_counts[3] << 8 | bit_counts[4] << 7 | bit_counts[5] << 6 | bit_counts[6] << 5| bit_counts[7] << 4| bit_counts[8] << 3| bit_counts[9] << 2| bit_counts[10] << 1| bit_counts[11];
        let epsilon_rate = (gamma_rate as u16).not() & 0b0000_1111_1111_1111;
        println!("g: {}, e: {}", gamma_rate, epsilon_rate);
        gamma_rate as usize * epsilon_rate as usize
    }
}

#[aoc(day3, part2)]
pub fn part2(input: &[Vec<u8>]) -> i32 {
0
}

#[cfg(test)]
mod tests {
    use crate::day3::{input_generator, part1, part2};

    #[test]
    fn sample1() {
        assert_eq!(part1(&input_generator("00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010")), 198);
    }

//     #[test]
//     fn sample2() {
//         assert_eq!(part2(&input_generator("forward 5
// down 5
// forward 8
// up 3
// down 8
// forward 2")), 900);
//     }
}
