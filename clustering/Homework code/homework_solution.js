class Perceptron {

  constructor(n){
    this.weights = [];
    for(let i =0; i < n; i++){
      this.weights.push(random(-1, 1));
    }
    this.learningRate = 0.01;
  }

  activate(sum){
    // sigmoid function
    return 1/(1 + Math.pow(Math.E, -1*sum));
  }

  feedForward(inputs){
    let sum = 0;
    for(let i = 0; i < inputs.length; i++){
      sum += inputs[i]*this.weights[i];
    }
    return this.activate(sum);
  }

  // completed training function
  train(inputs, desired){
    let guess = this.feedForward(inputs);
    let error = desired - guess;
    for(let i = 0; i < this.weights.length; i++){
      this.weights[i] += this.learningRate*error*inputs[i];
    }
  }

}
