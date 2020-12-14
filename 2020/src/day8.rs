#[derive(Clone)]
pub enum Instruction {
    Nop { value: i64 },
    Acc { change: i64 },
    Jmp { offset: i64 },
}

#[aoc_generator(day8)]
pub fn gen(input: &str) -> Vec<Instruction> {
    input
        .lines()
        .map(|l| {
            let parts = l.split(' ').collect::<Vec<_>>();
            let ins = parts[0].to_string();
            let value = parts[1].parse::<i64>().unwrap();

            match ins.as_str() {
                "nop" => Instruction::Nop { value },
                "acc" => Instruction::Acc { change: value },
                "jmp" => Instruction::Jmp { offset: value },
                _ => unimplemented!(),
            }
        })
        .collect()
}

#[aoc(day8, part1)]
pub fn part1(instructions: &[Instruction]) -> i64 {
    let mut executed_before = vec![0; instructions.len()];
    let mut ip: i64 = 0;
    let mut acc: i64 = 0;

    while let Some(ins) = instructions.get(ip as usize) {
        if executed_before[ip as usize] == 1 {
            println!("Value in acc = {}", acc);
            break;
        }
        executed_before[ip as usize] = 1;
        match ins {
            Instruction::Nop { value: _ } => {
                ip += 1;
            }
            Instruction::Acc { change } => {
                acc += *change;
                ip += 1;
            }
            Instruction::Jmp { offset } => {
                ip += *offset;
            }
        }
    }

    acc
}

#[aoc(day8, part2)]
pub fn part2(instructions: &[Instruction]) -> i64 {
    for (i, instruction) in instructions.iter().enumerate() {
        let mut real_instructions = instructions.to_vec();
        match instruction {
            Instruction::Nop { value } => {
                real_instructions[i] = Instruction::Jmp { offset: *value };
            }
            Instruction::Jmp { offset } => {
                real_instructions[i] = Instruction::Nop { value: *offset };
            }
            _ => continue,
        }

        let mut executed_before = vec![0; instructions.len()];
        let mut ip: i64 = 0;
        let mut acc: i64 = 0;

        while let Some(ins) = real_instructions.get(ip as usize) {
            if executed_before[ip as usize] == 1 {
                break;
            }
            executed_before[ip as usize] = 1;
            match ins {
                Instruction::Nop { value: _ } => {
                    ip += 1;
                }
                Instruction::Acc { change } => {
                    acc += *change;
                    ip += 1;
                }
                Instruction::Jmp { offset } => {
                    ip += *offset;
                }
            }
        }

        if ip == instructions.len() as i64 {
            return acc;
        }
    }

    -1
}

#[cfg(test)]
pub mod test {
    use crate::day8::{gen, part1};

    #[test]
    pub fn test_1() {
        assert_eq!(
            part1(&gen("nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6")),
            5
        );
    }

    //     #[test]
    //     pub fn test_2() {
    //         assert_eq!(
    //             part2(&gen("shiny gold bags contain 2 dark red bags.
    // dark red bags contain 2 dark orange bags.
    // dark orange bags contain 2 dark yellow bags.
    // dark yellow bags contain 2 dark green bags.
    // dark green bags contain 2 dark blue bags.
    // dark blue bags contain 2 dark violet bags.
    // dark violet bags contain no other bags.")),
    //             126
    //         );
    //     }
}
