fn szukaj(t: &mut [i32], l: i32, p: i32, s: i32) -> i32 {
  if l <= p {
    let sr = (l+p) / 2;
    if t[sr] == s{
      sr
    } else if s > t[sr] {
      szukaj(t, sr+1, p, s)
    } else {
      szukaj(t, l, sr-1, s)
    }
  }
}

fn main()
{
  let t: [i32; 10] = [1,2,4,6,7,9,11,12,15,17];
  println!("{}", szukaj(t,0,9,11))
}