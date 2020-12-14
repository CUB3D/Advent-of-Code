use std::collections::HashSet;

#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct Rule {
    pub bag: String,
    pub contains: Vec<(u32, String)>,
}

impl Rule {
    pub fn can_hold(&self, b: &str) -> bool {
        self.contains.iter().any(|(_c, bb)| bb == b)
    }
}

#[aoc_generator(day7)]
pub fn gen(input: &str) -> Vec<Rule> {
    input
        .lines()
        .map(|l| {
            let x = l.split(" bags contain ").collect::<Vec<_>>();
            let bag = x[0].to_string();
            let l = x[1].to_string();

            let contains = if l != "no other bags." {
                let l = l.replace(",", "").replace(".", "").replace("bags", "bag");
                l.split("bag")
                    .filter(|l| !l.is_empty())
                    .map(|b| {
                        let b = b.trim().to_string();
                        let count_s = b.split(' ').next().unwrap().to_string();
                        let count = count_s.parse::<u32>().unwrap();
                        let bag_name = b.split(' ').skip(1).collect::<Vec<_>>().join(" ");

                        (count, bag_name)
                    })
                    .collect()
            } else {
                Vec::new()
            };

            Rule { bag, contains }
        })
        .collect()
}

#[aoc(day7, part1)]
pub fn part1(rules: &[Rule]) -> u64 {
    let mut can_hold_gold = HashSet::new();

    // Everything that can hold gold
    for rule in rules {
        if rule.can_hold("shiny gold") {
            can_hold_gold.insert(rule);
        }
    }

    let mut last_len = can_hold_gold.len();

    loop {
        for rule in rules {
            for existing in can_hold_gold.clone() {
                if rule.bag != existing.bag {
                    // println!("can {:?} hold {:?}", rule, existing);
                    if rule.can_hold(&existing.bag) {
                        can_hold_gold.insert(rule);
                    }
                }
            }
        }

        if can_hold_gold.len() != last_len {
            last_len = can_hold_gold.len();
        } else {
            break;
        }
    }

    can_hold_gold.len() as u64
}

pub fn sum_bags(rules: &[Rule], rule: &Rule) -> u64 {
    if rule.contains.is_empty() {
        return 1;
    }

    let sum = rule
        .contains
        .iter()
        .map(|(count, bag)| {
            let child_rule = rules.iter().find(|b| b.bag == *bag).unwrap();
            sum_bags(rules, child_rule) * (*count) as u64
        })
        .sum::<u64>();

    sum + 1
}

#[aoc(day7, part2)]
pub fn part2(rules: &[Rule]) -> u64 {
    let root = rules.iter().find(|f| f.bag == "shiny gold").unwrap();
    // sub one as the total includes the gold bag
    sum_bags(rules, root) - 1
}

#[cfg(test)]
pub mod test {
    use crate::day7::{gen, part1, part2};

    #[test]
    pub fn test_1() {
        assert_eq!(
            part1(&gen(
                "light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."
            )),
            4
        );
    }

    #[test]
    pub fn test_2() {
        assert_eq!(
            part2(&gen("shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.")),
            126
        );
    }
}
