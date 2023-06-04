use std::collections::HashMap;

/// Solution for twosum problem in rust

/// Solution using double loop O(n^2) here.
fn two_sum_dbl_loop(nums: Vec<i32>, target: i32) -> Vec<i32> {
    
}

/// Solution using hashmap O(n) here.
fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut seen_vals: HashMap<i32, usize> = HashMap::new();
    let mut twosum = Vec::new();

    for (idx, val) in nums.iter().enumerate() {
        let target_diff = target - val;
        if seen_vals.contains_key(val) {
            twosum.push(seen_vals[val]);
            twosum.push(idx.try_into().unwrap());
        } else {
            seen_vals.insert(target_diff, idx.try_into().unwrap());
        }
    }
    twosum
}

fn main() {
    println!("Hello, world!");
}
