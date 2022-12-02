use std::env;
use std::fs;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // Parse args
    let args: Vec<String> = env::args().collect();
    let file_path = &args[1];
    println!("In file {}", file_path);

    // Read file
    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");
    // Print file
    //println!("With text:\n{contents}");

    let mut total_cals: Vec<i32> = Vec::new();
    // iterate over file
    if let Ok(lines) = read_lines(file_path) {
        let mut current_cal = 0;
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(ip) = line {
                if ip == "" {
                    // println!("{current_cal}");
                    total_cals.push(current_cal);
                    current_cal = 0;
                }
                else {
                    current_cal += ip.parse::<i32>().unwrap();
                }
            }
        }
    }
    // println!("{total_cals:?}");
    let max = total_cals.iter().max();
    println!("Part 1 : {max:?}");

    total_cals.sort();
    total_cals.reverse();
    let top_three = total_cals[0] + total_cals[1] + total_cals[2];
    println!("Part 2 : {top_three:?}")

}
// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}