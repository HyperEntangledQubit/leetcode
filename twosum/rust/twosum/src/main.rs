use std::collections::HashMap;

/// Solution for twosum problem in rust

/// Solution using double loop O(n^2) here.
fn two_sum_dbl_loop(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut twosum = Vec::new();

    for (idx, _) in nums.iter().enumerate() {
        if twosum.len() == 2 {
            break;
        }
        for (jdx, _) in nums.iter().enumerate() {
            if idx != jdx && nums[idx] + nums[jdx] == target {
            twosum.push(idx.try_into().unwrap());
            twosum.push(jdx.try_into().unwrap());
            }
        }
    }
    twosum
}

/// Solution using hashmap O(n) here.
fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut seen_vals: HashMap<i32, i32> = HashMap::new();
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

/// Alternate solution correctly using ownership in rust here.
fn twosum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut seen_vals: HashMap<i32, usize> = HashMap::new();

    for (idx, val) in nums.iter().enumerate() {
        let tdiff = target - val;
        /* Avoid try_into().unwrap() call for usize -> i32 cast */
        if let Some(num) = seen_vals.get(&tdiff) {
            return vec![*num as i32, idx as i32];
        } else {
            seen_vals.insert(*val, idx);
        }
    }
    vec![]
}

fn main() {
    let nums = vec![21, 3, 61, 44, 87, 98, -1, 4];
    let tgt = 60;
    println!("Twosum using dbl loop is: {:?}", two_sum_dbl_loop(nums.clone(), tgt));
    println!("Twosum using hash is: {:?}", two_sum(nums.clone(), tgt));
    println!("Twosum using alt solution is: {:?}", twosum(nums.clone(), tgt));
}
