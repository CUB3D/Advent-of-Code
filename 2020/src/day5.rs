pub struct BoardingCard {
    pub rows: Vec<char>,
    pub cols: Vec<char>,
}

#[aoc_generator(day5)]
pub fn gen(input: &str) -> Vec<BoardingCard> {
    input
        .lines()
        .map(|l| {
            let mut rows = Vec::new();
            let mut cols = Vec::new();

            for c in l.chars() {
                match c {
                    'F' | 'B' => rows.push(c),
                    'L' | 'R' => cols.push(c),
                    _ => {}
                }
            }

            BoardingCard { rows, cols }
        })
        .collect::<Vec<_>>()
}

pub fn algo(row: &[char], min_c: char, max_c: char, max_val: u64) -> u64 {
    let mut min = 0;
    let mut max = max_val;

    for c in row {
        if *c == min_c {
            max = ((min + max) as f64 / 2.0).ceil() as u64;
        }
        if *c == max_c {
            min = ((min + max) as f64 / 2.0).ceil() as u64;
        }
    }

    min
}

#[aoc(day5, part1)]
pub fn part1(input: &[BoardingCard]) -> u64 {
    input
        .iter()
        .map(|bc| {
            let row_num = algo(&*bc.rows, 'F', 'B', 127);
            let col_num = algo(&*bc.cols, 'L', 'R', 8);

            row_num * 8 + col_num
        })
        .max()
        .unwrap()
}

#[aoc(day5, part2)]
pub fn part2(input: &[BoardingCard]) -> u64 {
    let seats = 127 * 8;
    let mut all_seats = (0..seats).collect::<Vec<_>>();

    let in_list = input
        .iter()
        .map(|bc| {
            let row_num = algo(&*bc.rows, 'F', 'B', 127);
            let col_num = algo(&*bc.cols, 'L', 'R', 8);

            row_num * 8 + col_num
        })
        .collect::<Vec<_>>();

    for x in in_list {
        let p = all_seats.iter().copied().position(|y| y == x).unwrap();
        all_seats.remove(p);
    }

    all_seats
        .iter()
        .copied()
        .filter(|x| !all_seats.contains(&(x - 1)) && !all_seats.contains(&(x + 1)))
        .nth(0usize)
        .unwrap()
}

#[cfg(test)]
mod tests {
    use crate::day5::{gen, part1};

    #[test]
    pub fn test_1() {
        assert_eq!(part1(&gen("FBFBBFFRLR")), 357);
        assert_eq!(part1(&gen("BFFFBBFRRR")), 567);
        assert_eq!(part1(&gen("FFFBBBFRRR")), 119);
        assert_eq!(part1(&gen("BBFFBBFRLL")), 820);
    }
}
