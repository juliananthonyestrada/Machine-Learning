// ! Example 0
struct Area(f32);

trait Shape {
    fn area_of(shape: &Self) -> Area;
}

struct Circle {
    radius: f32,
}

impl Shape for Circle {
    fn area_of(circle: &Self) -> Area {
        return Area(3.1415 * circle.radius * circle.radius);
    }
}

fn create_simple_circle() {
    let circle: Circle = Circle { radius: 2.0 };
    let area: Area = Circle::area_of(&circle);
}

// ! Example 1
struct Circle_ex1 {
    radius: f32,
}

fn example1() {
    let circles: Vec<Circle> = (0..5)
        .map(|i| Circle {
            radius: i as f32 + 1.0,
        })
        .collect();

    for (i, circle) in circles.iter().enumerate() {
        println!("Circle {} has radius {}", i, circle.radius);
    }
}

// ! Example 2
struct Circle_ex2 {
    radius: f32,
}

fn example2() {
    let mut circles = Vec::new();
    for i in 0..5 {
        let circle = Circle {
            radius: (i + 1) as f32,
        };
        circles.push(circle);
    }
    // Use circles here!
}

pub fn main() {
    create_simple_circle();
    example1();
    example2();
}