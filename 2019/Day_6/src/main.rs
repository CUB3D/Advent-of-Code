   use petgraph::Graph;
   use petgraph::dot::{Dot, Config};
    use std::fs::File;
    use std::io::{BufRead, BufReader, Result};

fn main() {
    let f = File::open("./input").expect("No input file");
    let mut graph = Graph::<_, ()>::new();
    graph.add_node("COM".to_string());
    for line in BufReader::new(f).lines() {
        if let Ok(line) = line {
            let mut parts = line.split(")");
            let lhs = parts.next().unwrap();
            let rhs = parts.next().unwrap();
            graph.add_node(rhs.to_string());
        }
    }

  // graph.extend_with_edges(&[
  // ]);
println!("{:?}", Dot::with_config(&graph, &[Config::EdgeNoLabel]));
}
