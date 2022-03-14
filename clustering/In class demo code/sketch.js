// Variable to store perceptron object
let p;

// sample inputs:

let inputs = [50, -12, 1]
// 50 = x position of point
// -12 = y position of point
// 1 = bias to ensure sum of weights is never zero

function setup() {
  createCanvas(640, 320);
  // create perceptron object with 3 inputs
  p = new Perceptron(3);

  // check initialized weights
  // console.log(p.weights)

  // check feedForward function
  // try this once before writing activation function
  // and again after writing activation function
  // let guess = p.feedForward(inputs);
  // console.log(guess);

}

// we don't need anything here for now
function draw() {
  background(220);

}
