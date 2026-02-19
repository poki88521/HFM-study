## HFM-swish

- 2026/2/16: change activate function to swish (x * sigmoid(beta * x)) (beta could be updated)
- 2026/2/17: training the model
- 2026/2/18: training the model to 6 and 12 hours
    + problem: p converges significantly slower than c, v
    + available solution: raise the weight of loss_e during training
- 2026/2/19: training the model to 18 hours
    + change loss function: L = 0.1 * loss_c + 0.9 * loss_e
    + sth wrong: p_error seems to converge to 1.8
    + considering to join L-BFGS to train for 10 epochs
