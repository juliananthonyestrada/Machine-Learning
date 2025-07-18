#[derive(Copy, Clone)]
struct Point {
    x: i32,
    y: i32,
}

let p1 = Point { x: 1, y: 2 };
let p2 = p1; // p1 is copied, not moved
println!("{}, {}", p1.x, p2.x);