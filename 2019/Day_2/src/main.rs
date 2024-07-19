use std::fs::File;
use std::io::{BufRead, BufReader, Result};


fn run(noun: i32, verb: i32) -> i32 {
    let mut test_inputs = Vec::<i32>::new();
    let f = File::open("./input").unwrap();
    for line in BufReader::new(f).lines() {
        for x in line.unwrap().split(",") {
            test_inputs.push(x.parse().unwrap());
        }
    }

    test_inputs[1] = noun;
    test_inputs[2] = verb;
//    let mut test_inputs = vec![1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50];

    let mut index = 0;

    loop {
        let v = test_inputs[index]; 
        index+=1;

        match v {
            1 => {
                let x = test_inputs[test_inputs[index] as usize];
                let y = test_inputs[test_inputs[index + 1] as usize];
                let o = test_inputs[index + 2] as usize;

                index += 3;
            
                test_inputs[o] = x + y;
                println!("Case 1: {:?}", test_inputs);
            },
            2 => {
                let x = test_inputs[test_inputs[index] as usize];
                let y = test_inputs[test_inputs[index + 1] as usize];
                let o = test_inputs[index + 2] as usize;

                index += 3;
            
                test_inputs[o] = x * y;
                println!("Case 2: {:?}", test_inputs);
            },
            99 => {
                println!("Case 3: {:?}", test_inputs);
                println!("First value: {}", test_inputs[0]);
                return test_inputs[0];
            }
            _ => { eprintln!("Error {} is not valid", v); return -1; }
        }
    }
}

fn main() {
    for i in 0..100 {
        for j in 0..100 {
            if run(i, j) == 19690720 {
                println!("Final answer: {}", 100 * i + j);
                return;
            }
        }
    }
}
