const N: i32 = 10;
fn rysuj(x: i32) {
  if 2 * x <= N {
    println!("strzalka od {} do {}", x, 2*x);
    rysuj(2*x);
  }
  if 2 * x + 1 <= N {
    println!("strzalka od {} do {}", x, 2*x+1);
  }
}

fn main() {
  rysuj(1);
}