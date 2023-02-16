fn silnia(n: i32) -> i32 {
  println!("wywołuje sie z {n}");
  if n == 1 {
    return 1
  }
  silnia(n-1)*n
}

fn main() {
  println!("{}", silnia(5));
}