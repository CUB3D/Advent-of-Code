use itertools::Itertools;

use std::collections::HashMap;
use std::fmt;
use std::fmt::Formatter;
use itertools::FoldWhile::Continue;
use std::collections::hash_map::Entry::Occupied;

#[derive(Copy, Clone, Hash, Eq, PartialOrd, PartialEq, Debug)]
pub enum Seat {
    Floor,
    Seat(bool),
}

#[derive(Clone, Hash, Eq, PartialOrd, PartialEq)]
pub struct Map(Vec<Vec<Seat>>);


impl fmt::Debug for Map {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        for row in self.0.iter() {
            for c in row.iter() {
                match c {
                    Seat::Floor => {f.write_str(".");}
                    Seat::Seat(occu) => {
                        if *occu {
                            f.write_str("#");
                        } else {
                            f.write_str("L");
                        }
                    }
                }
            }
            f.write_str("\n");
        }

        f.write_str("\n")
    }
}

#[aoc_generator(day11)]
pub fn gen(input: &str) -> Map {
    Map {
        0: input
            .lines().map(|l| {
            l.chars().map(|c| {
                match c {
                    'L' => Seat::Seat(false),
                    '#' => Seat::Seat(true),
                    '.' => Seat::Floor,
                    _ => panic!()
                }
            }).collect::<Vec<_>>()
        }).collect::<Vec<_>>()
    }
}

pub fn occupied(x: usize, y: usize, d: &Map) -> u32 {
    let mut adj_occ = 0;
    for yy in &[-1, 0, 1] {
        for xx in &[-1, 0, 1] {
            if *yy == 0 && *xx == 0 {
                continue;
            }

            let ny = y as i64 + *yy;
            let nx = x as i64 + *xx;

            if ny < 0 || nx < 0 || ny >= d.0.len() as i64 || nx >= d.0[x].len() as i64 {
                continue
            }


            if let Seat::Seat(b) = d.0.get(ny as usize).unwrap().get(nx as usize).unwrap() {
                if *b {
                    adj_occ += 1;
                }
            }
        }
    }

    assert!(adj_occ >= 0);
    assert!(adj_occ < 9);

    adj_occ
}

#[test]
pub fn test_6() {
    assert_eq!(occupied(1, 1, &gen(r#"###
###
###"#)), 8);
    assert_eq!(occupied(1, 1, &gen(r#"###
###
##."#)), 7);
    assert_eq!(occupied(0, 0, &gen(r#"###
###
##."#)), 3);


    assert_eq!(occupied(1, 1, &gen(r#"#########.####.#####.##########.################.######.##################.#######.########
#########.####.############.#############.######.#################################.########
#########.####.#####.######.########.###########.###############.#########.#######.########
########..####.#####.######.########.###########.######.########.###############.########.#
####.###############.####################.######.###############.#########.#######.########
####################.####################.################################.#######.########
......#.##.....#.#..#.....#.#..##.#.##.#...#..#..............#..#......##.....##...#.#....."#)), 8);
}

pub fn iter(mm: &Map) -> Map {
    let d = mm.0.clone();

    let mut m = Vec::new();

    for y in 0..d.len() {
        let mut row = Vec::new();

        for x in 0..d[y].len() {
            let old_cell = d.get(y).unwrap().get(x).unwrap().clone();
            let mut new_cell = old_cell.clone();

            let adj_occ = occupied(x, y, &mm);

            if let Seat::Seat(occ) = old_cell {
                if occ {
                    if adj_occ >= 4 {
                        new_cell = Seat::Seat(false)
                    }
                } else {
                    if adj_occ == 0 {
                        new_cell = Seat::Seat(true)
                    }
                }
            }

            row.push(new_cell);
        }

        m.push(row);
    }

    assert_eq!(m.len(), mm.0.len());
    assert_eq!(m[0].len(), mm.0[0].len());

    Map {0:m}
}

pub fn count_seats(d: &[Vec<Seat>]) -> i64 {
    d.iter().map(|l| l.iter().filter(|s| matches!(s, Seat::Seat(true))).count() as i64).sum()
}

#[aoc(day11, part1)]
pub fn part1(d: &Map) -> i64 {

    let mut state = d.clone();
    let mut n = 0;
    loop {
        println!("Iter {}", n);
        println!("{:?}", state);
        n += 1;

        let new_state = iter(&state);
        if new_state == state {
            println!("Got new state");
            println!("{:?}", new_state);
            break
        }
        state = new_state
    }

    println!("{:?}", state);

    count_seats(&state.0)
}
//
// #[aoc(day10, part2)]
// pub fn part2(instructions: &[u64]) -> i64 {
//     let mut instructions = instructions.iter().copied().collect::<Vec<_>>();
//     instructions.insert(0, 0);
//     instructions.push(instructions.iter().max().unwrap() + 3);
//     let instructions = instructions
//         .iter()
//         .copied()
//         .sorted()
//         .rev()
//         .collect::<Vec<_>>();
//
//     let mut scores = HashMap::new();
//
//     for (key, num) in instructions.iter().enumerate() {
//         let next_num = &instructions[0..key];
//         let next_num = next_num.iter().rev().take(3).rev().collect::<Vec<_>>();
//
//         if next_num.is_empty() {
//             scores.insert(num, 1);
//             println!("Storing {}", num);
//             continue;
//         }
//
//         scores.insert(num, 0);
//         for next_number in next_num {
//             if next_number - num <= 3 {
//                 scores.insert(num, scores[num] + scores[next_number]);
//             }
//         }
//     }
//
//     println!("scores: {:?}", scores);
//
//     scores[&0]
// }

#[cfg(test)]
pub mod test {
    use crate::day11::{part1, gen, iter};

    #[test]
    pub fn test_p1() {
        assert_eq!(part1(&gen(r#"L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"#)), 37)
    }

    #[test]
    pub fn test_1() {
        assert_eq!(iter(&gen(r#"L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"#)), gen(r#"#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"#))
    }

    #[test]
    pub fn test_2() {
        assert_eq!(iter(&gen(r#"#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"#)), gen(r#"#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##"#))
    }

    #[test]
    pub fn test_3() {
        assert_eq!(iter(&gen(r#"#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##"#)), gen(r#"#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##"#))
    }

    #[test]
    pub fn test_4() {
        assert_eq!(iter(&gen(r#"#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##"#)), gen(r#"#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##"#))
    }

    #[test]
    pub fn test_5() {
        assert_eq!(iter(&gen(r#"#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##"#)), gen(r#"#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"#))
    }
}
