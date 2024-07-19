use std::fs::File;
use std::io::{BufRead, BufReader, Result};


fn run(noun: i32, verb: i32) -> i32 {
    let mut test_inputs = Vec::<i32>::new();
    let f = File::open("./input").expect("No input file");
    for line in BufReader::new(f).lines() {
        for x in line.expect("Invalid line").split(",").filter(| x | x.len() > 0) {
            test_inputs.push(x.parse().expect("Invalid input"));
        }
    }


//    test_inputs[1] = noun;
  //  test_inputs[2] = verb;
//    let mut test_inputs = vec![1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50];

    let mut index = 0;

    loop {
        let v = test_inputs[index]; 

        let v_str = v.to_string();
        println!("Instruction: {}", v_str);

        let mut opcode = 0;
        let mut modes = vec![0; 50];

        if v_str.len() <= 2 {
            opcode = v_str.parse::<i32>().expect("Unable to parse opcode");
        } else {
            let opcode_str = &v_str[v_str.len() - 2..];
            opcode = opcode_str.parse::<i32>().expect("Unable to parse opcode");

            let modes_str = &v_str[..v_str.len() - 2];
            //println!("Modes_str: {}", modes_str);

            let l = match opcode {
                1 => 3,
                2 => 3,
                3 => 1,
                4 => 1,
                5 => 2,
                6 => 2,
                7 => 3,
                8 => 3,
                99 => 0,
                _ => {
                    eprintln!("Invalid opcode: {}", opcode);
                    0
                }
            };

            modes = vec![0; (l - modes_str.len()) as usize];

            for c in modes_str.chars().map(| c | c.to_string().parse::<u32>().expect("Unable to parse mode")) {
                modes.push(c);
            }

            let mut m2: Vec<u32> = Vec::new();

            for x in modes.iter().rev() {
                m2.push(*x);
            }

            modes = m2;

        }

        println!("Op: {}", opcode);
        //println!("Modes: {:?}", modes);
        index+=1;


        match opcode {
            1 => {
                println!("Opcode 1: {}, {}", index, test_inputs[index]);
                let x = read_val(test_inputs[index], modes[0], &test_inputs);
                println!("{}", x);
                let y = read_val(test_inputs[index + 1], modes[1], &test_inputs);
                println!("{}", index);
                let o = test_inputs[index + 2] as usize;

                index += 3;
            
                println!("{} + {} = {}:{}", x, y, x + y, o);
                test_inputs[o] = x + y;
                println!("Case 1: {:?}", test_inputs);
            },
            2 => {
                let x = read_val(test_inputs[index], modes[0], &test_inputs);
                let y = read_val(test_inputs[index + 1], modes[1], &test_inputs);
                //let o = read_val(test_inputs[index + 2], modes[2], &test_inputs) as usize;
                let o = test_inputs[index + 2] as usize;

                index += 3;
            
                println!("{} x {} = {}:{}", x, y, x * y, o);
                test_inputs[o] = x * y;
                println!("Case 2: {:?}", test_inputs);
            },
            3 => {
                println!("Opcode 3");
                let input = 5;
                println!("Index = {}", index);
                let i = test_inputs[index] as usize;
                println!("input[{}] = {}", i, input);
                test_inputs[i] = input;
                index += 1;
            },
            4 => {
                let x = read_val(test_inputs[index], modes[0], &test_inputs);
                println!("Output: {}", x);
                //println!("Output: data[{}] = {}", x, test_inputs[x as usize]);
                index += 1;
            },
            5 => {
                let x = read_val(test_inputs[index], modes[0], &test_inputs);
                let y = read_val(test_inputs[index + 1], modes[1], &test_inputs);

                index += 2;
                println!("IF {} != 0: IP = {}", x, y);
                if x != 0 {
                    println!("  True");
                    index = y as usize;
                } else {
                    println!("  False");
                }
            },
            6 => {
                let x = read_val(test_inputs[index], modes[0], &test_inputs);
                let y = read_val(test_inputs[index + 1], modes[1], &test_inputs);

                index += 2;
                println!("IF {} == 0: IP = {}", x, y);
                if x == 0 {
                    println!("  True");
                    index = y as usize;
                } else {
                    println!("  False");
                }
            },
            7 => {
                let x = read_val(test_inputs[index], modes[0], &test_inputs);
                let y = read_val(test_inputs[index + 1], modes[1], &test_inputs);
                let z = test_inputs[index + 2];

                index += 3;
                println!("IF {} < {}: data[{}] = 1 else 0", x, y, z);
                if x < y {
                    println!("  True");
                    test_inputs[z as usize] = 1;
                } else {
                    println!("  False");
                    test_inputs[z as usize] = 0;
                }
            },
            8 => {
                let x = read_val(test_inputs[index], modes[0], &test_inputs);
                let y = read_val(test_inputs[index + 1], modes[1], &test_inputs);
                let z = test_inputs[index + 2];

                index += 3;
                println!("IF {} == {}: data[{}] = 1 else data[{}] = 0", x, y, z, z);
                if x == y {
                    println!("  True");
                    test_inputs[z as usize] = 1;
                } else {
                    println!("  False");
                    test_inputs[z as usize] = 0;
                }
            },
            99 => {
                println!("Case 3: {:?}", test_inputs);
                println!("First value: {}", test_inputs[0]);
                return test_inputs[0];
            }
            _ => { eprintln!("Error {} is not valid", v); return -1; }
        }
        println!("{:?}", test_inputs);
    }
}

fn read_val(val: i32, mode: u32, input: &Vec<i32>) -> i32 {
    let r = match mode {
        0 => {
            println!("  Addr mode 0");
            let index = val as usize;
            println!("  Position mode value: data[{}] = {}", index, input[index]);
            input[index]
        },
        1 => {
            println!("  Immediate mode value {}", val);
            val
        },
        _ => { println!("  Unknown mode: {}", mode); 0 }
    };

    println!("  Mode: {}", mode);
    println!("  Result: {}", r);
    return r;
}

fn main() {
    run(0, 0);
    /*
    for i in 0..100 {
        for j in 0..100 {
            if run(i, j) == 19690720 {
                println!("Final answer: {}", 100 * i + j);
                return;
            }
        }
    }*/
}
