pub enum Element {
    Tree,
    Open,
}

#[aoc_generator(day3)]
pub fn gen(input: &str) -> Vec<Vec<Element>> {
    input
        .lines()
        .map(|l| {
            l.chars()
                .map(|c| match c {
                    '#' => Element::Tree,
                    '.' => Element::Open,
                    _ => panic!(),
                })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>()
}

#[aoc(day3, part1)]
pub fn part1(input: &[Vec<Element>]) -> u64 {
    algo(input, 3, 1)
}

pub fn algo(input: &[Vec<Element>], xdiff: usize, ydiff: usize) -> u64 {
    let mut x = 0;
    let mut y = 0;

    let mut trees = 0;

    loop {
        if let Some(row) = input.get(y) {
            let col = row.get(x % row.len()).unwrap();
            if let Element::Tree = col {
                trees += 1;
            }
            x += xdiff;
            y += ydiff;
        } else {
            break;
        }
    }

    trees
}

#[aoc(day3, part2)]
pub fn part2(input: &[Vec<Element>]) -> u64 {
    algo(input, 1, 1)
        * algo(input, 3, 1)
        * algo(input, 5, 1)
        * algo(input, 7, 1)
        * algo(input, 1, 2)
}

#[cfg(test)]
mod tests {}
