# HFM-study
personal HFM study material

## update
- 2026/2/16: change activate function to swish (x * sigmoid(beta * x)) (beta could be updated)
- 2026/2/17: training the model
- 2026/2/18: training the model to 6 and 12 hours
    + problem: p converges significantly slower than c, v
    + available solution: raise the weight of loss_e during training
- 2026/2/19: training the model to 18 hours
    + change loss function: L = 0.1 * loss_c + 0.9 * loss_e
    + sth wrong: p_error seems to converge to 1.8
    + considering to join L-BFGS to train for 10 epochs
- 2026/2/20: training the model in L-BFGS for 10 epochs (respectively in 30k and 60k batch size)
    + problem: p_error still more than 1
- 2026/2/20: modify model to optimize predicting p:
    + add auto-adjust weight of loss function
    + add pressure Poisson's equation to specifically restrain pressure
    + Poisson: e5 = p_xx + p_yy + (u_x ^ 2 + 2 * u_y * v_x + v_y ^ 2)
    + loss function auto-adjust
- 2026/2/21: train model for 12 hours (58000 epochs), works
