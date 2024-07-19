use std::fs::File;
use std::io::{BufRead, BufReader, Result};
use std::collections::HashSet;

fn main() {
    let start = 109165;
    let end = 576723;

    let mut a = Vec::<i32>::new();

    for x in start..end {
        let xs: String = x.to_string();
        let mut invalid = false;

        let mut last = xs.chars().next().unwrap();
        let mut lc = 0;
        let mut valid = false;
        for ch in xs[1..].chars() {
            if lc == 1 && last != ch {
                valid = true;
                break;
            }
            if last == ch {
                lc += 1;
            } else {
                lc = 0;
            }

            last = ch;
        }
        if lc == 1 {
            valid = true;
        }

        if !valid {
            println!("{} invalid", xs);
            continue;
        }

        let mut last = xs.chars().next().unwrap().to_string().parse::<i32>().unwrap();
        for ch in xs[1..].chars() {
            let b = ch.to_string().parse::<i32>().unwrap();
            if b < last {
                invalid = true;
                break;
            }
            last = b;
        }

        if invalid {
            continue;
        }

        println!("Answer: {}", xs);
        a.push(x);
    }

    println!("Answers part1: {}", a.len());
}

