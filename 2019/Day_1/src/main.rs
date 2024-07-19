use std::fs::read_to_string;
use std::io::{BufRead, BufReader, Result};
use std::iter::successors;

fn part1() {
    let fuel_count: i32 = read_to_string("../input.txt").unwrap().lines().map(|x| x.parse::<i32>().unwrap() / 3 - 2).sum();

    println!("Part 1: {}", fuel_count);
}

fn fuel2_impl(mass: u32) -> u32 {
    let fuel2 = | mass: &u32 |-> Option<u32> {
        (mass / 3).checked_sub(2)
    };
    successors(Some(mass), fuel2).skip(1).sum()
}


fn main() {
    let fuel_count: u32 = read_to_string("../input.txt").unwrap().lines().map(|x| fuel2_impl(x.parse::<u32>().unwrap())).sum();

    println!("Part 2: {}", fuel_count);

}
