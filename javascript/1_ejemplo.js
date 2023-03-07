let x = 'z'.charCodeAt(0);
let y = 'Y'.charCodeAt(0);

while (x >= 'a'.charCodeAt(0) && y >= 'A'.charCodeAt(0)) {
  console.log(String.fromCharCode(x) + String.fromCharCode(y));
  x -= 2;
  y -= 2;
}
