use std::fs::File;
use std::io::{BufRead, BufReader, Result};
use std::collections::HashSet;

fn main() {
    let f = File::open("./input").unwrap();
    let mut wires = Vec::<Vec<(i32, i32, i32)>>::new();
    for line in BufReader::new(f).lines() {
        println!("Processing wire: {}", wires.len() + 1);
        let mut instructions = Vec::<String>::new();
        for x in line.unwrap().split(",") {
            instructions.push(x.to_string());
        }
        println!("{} inst", instructions.len());
        wires.push(walk_wire(instructions));
    }
    println!("Find crosses");

    println!("Done {} wires", wires.len());

    let mut crosses = Vec::<(i32, i32, i32)>::new();

    for w1 in &wires {
        for w2 in &wires {
            if w1 != w2 {
                for p1 in w1 {
                    for p2 in w2 {
                        if p1.0 == p2.0 && p1.1 == p2.1 {
                            println!("Cross at {:?} and {:?}", p1, p2); 
                            let x = (p1.0, p1.1, p1.2 + p2.2);
                            if !crosses.contains(&x) {
                                crosses.push(x);
                            }
                        }
                    }
                }
            }
        }
    }

    println!("Crosses {}", crosses.len());

    let mut l = *crosses.iter().next().unwrap();
    for w in &crosses {
        if l.0.abs() + l.1.abs() > w.0.abs() + w.1.abs() {
            l = *w;
        }
    }
    println!("Solution {:?}, {}", l, l.0.abs() + l.1.abs());

    let mut a = *crosses.iter().next().unwrap();

    for w in crosses {
        println!("{:?}, {}", w, w.2);
        if a.2 > w.2 {
            a = w;
        }
    }
    println!("Part 2: {:?}, {}", a, a.2);
}

fn walk_wire(instructions: Vec::<String>) -> Vec<(i32, i32, i32)> {
    let mut current_pos = (0, 0, 0);
    let mut visited = Vec::<(i32, i32, i32)>::new();
    
    for i in instructions {
        let d = i[0..].chars().next().unwrap();
        let l: i32 = i[1..].parse().unwrap();
        match d {
            'R' => {
                for x in 0..l {
                    current_pos.0 += 1;
                    current_pos.2 += 1;
                    visited.push(current_pos);
                }
            }
            'L' => {
                for x in 0..l {
                    current_pos.0 -= 1;
                    current_pos.2 += 1;
                    visited.push(current_pos);
                }
            }
            'U' => {
                for x in 0..l {
                    current_pos.1 += 1;
                    current_pos.2 += 1;
                    visited.push(current_pos);
                }
            }
            'D' => {
                for x in 0..l {
                    current_pos.1 -= 1;
                    current_pos.2 += 1;
                    visited.push(current_pos);
                }
            }
            _ => { eprintln!("Unknown pos: {}", d);}
        }
    }

    return visited;
}
