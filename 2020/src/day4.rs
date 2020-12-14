use regex::Regex;
use std::collections::HashMap;

#[aoc_generator(day4)]
pub fn gen(input: &str) -> Vec<HashMap<String, String>> {
    input
        .split("\n\n")
        .map(|l| {
            let l = l.replace("\n", " ");
            let pairs = l
                .split(' ')
                .map(|p| p.split(':').collect::<Vec<_>>())
                .filter(|p| p.len() > 1)
                .map(|pairs| (pairs[0].to_string(), pairs[1].to_string()))
                .collect::<Vec<_>>();

            let mut m = HashMap::new();
            for (k, v) in pairs {
                m.insert(k, v);
            }
            m
        })
        .collect::<Vec<_>>()
}

#[aoc(day4, part1)]
pub fn part1(input: &[HashMap<String, String>]) -> u64 {
    input.iter().filter(|f| is_valid(*f)).count() as u64
}

pub fn is_valid(pass: &HashMap<String, String>) -> bool {
    let required_fields = vec!["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];
    required_fields.into_iter().all(|k| pass.contains_key(k))
}

pub fn valid_byr(x: &str) -> bool {
    let num_re = Regex::new("[0-9]{4}").unwrap();
    num_re.is_match(x) && x.parse::<u32>().unwrap() >= 1920 && x.parse::<u32>().unwrap() <= 2002
}

pub fn valid_hgt(x: &str) -> bool {
    let hgt_re = Regex::new("[0-9]+(cm|in)").unwrap();

    if !hgt_re.is_match(x) {
        return false;
    }

    let is_cm = x.contains("cm");
    let num = x[..x.len() - 1 - 1].parse::<i64>().unwrap();

    if is_cm {
        (150..=193).contains(&num)
    } else {
        (59..=76).contains(&num)
    }
}

pub fn valid_hcl(x: &str) -> bool {
    let hcl_re = Regex::new("#[0-9a-f]{6}").unwrap();
    hcl_re.is_match(x)
}

pub fn valid_ecl(x: &str) -> bool {
    let re = Regex::new("(amb|blu|brn|gry|grn|hzl|oth)").unwrap();
    re.is_match(x)
}

pub fn valid_pid(x: &str) -> bool {
    if x.len() != 9 {
        return false;
    }
    let re = Regex::new("[0-9]{9}").unwrap();
    re.is_match(x)
}

pub fn is_valid2(pass: &HashMap<String, String>) -> bool {
    if !is_valid(pass) {
        return false;
    }
    let num_re = Regex::new("[0-9]{4}").unwrap();

    {
        let byr = pass.get("byr").unwrap();
        if !valid_byr(byr) {
            return false;
        }
    }

    {
        let iyr = pass.get("iyr").unwrap();
        if !(num_re.is_match(iyr)
            && iyr.parse::<u32>().unwrap() >= 2010
            && iyr.parse::<u32>().unwrap() <= 2020)
        {
            return false;
        }
    }

    {
        let eyr = pass.get("eyr").unwrap();
        if !(num_re.is_match(eyr)
            && eyr.parse::<u32>().unwrap() >= 2020
            && eyr.parse::<u32>().unwrap() <= 2030)
        {
            return false;
        }
    }

    {
        let x = pass.get("hgt").unwrap();
        if !valid_hgt(x) {
            return false;
        }
    }

    {
        let x = pass.get("hcl").unwrap();
        if !valid_hcl(x) {
            return false;
        }
    }

    {
        let x = pass.get("ecl").unwrap();
        if !valid_ecl(x) {
            return false;
        }
    }

    {
        let x = pass.get("pid").unwrap();
        if !valid_pid(x) {
            return false;
        }
    }

    true
}

#[aoc(day4, part2)]
pub fn part2(input: &[HashMap<String, String>]) -> u64 {
    input.iter().filter(|f| is_valid2(*f)).count() as u64
}

#[cfg(test)]
mod tests {
    use crate::day4::{gen, is_valid2, valid_byr, valid_ecl, valid_hcl, valid_hgt, valid_pid};

    #[test]
    pub fn test_gen() {
        let res = gen("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in");

        assert_eq!(res.len(), 4)
    }

    #[test]
    pub fn test_byr() {
        let x = valid_byr("2002");
        let y = valid_byr("2003");
        assert_eq!(x, true);
        assert_eq!(y, false);
    }

    #[test]
    pub fn test_hgt() {
        assert_eq!(valid_hgt("60in"), true);
        assert_eq!(valid_hgt("190cm"), true);
        assert_eq!(valid_hgt("190in"), false);
        assert_eq!(valid_hgt("190"), false);
    }

    #[test]
    pub fn test_hcl() {
        assert_eq!(valid_hcl("#123abc"), true);
        assert_eq!(valid_hcl("#123abz"), false);
        assert_eq!(valid_hcl("123abc"), false);
    }

    #[test]
    pub fn test_ecl() {
        assert_eq!(valid_ecl("brn"), true);
        assert_eq!(valid_ecl("#wat"), false);
    }

    #[test]
    pub fn test_pid() {
        assert_eq!(valid_pid("000000001"), true);
        assert_eq!(valid_pid("0123456789"), false);
    }

    #[test]
    pub fn test_invalid() {
        let g = gen("eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007");

        assert_eq!(is_valid2(&g[0]), false);
        assert_eq!(is_valid2(&g[1]), false);
        assert_eq!(is_valid2(&g[2]), false);
        assert_eq!(is_valid2(&g[3]), false);
    }

    #[test]
    pub fn test_valid() {
        let g = gen("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719");

        assert_eq!(is_valid2(&g[0]), true);
        assert_eq!(is_valid2(&g[1]), true);
        assert_eq!(is_valid2(&g[2]), true);
        assert_eq!(is_valid2(&g[3]), true);
    }
}
