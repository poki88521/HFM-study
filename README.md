## HFM-swish

- 2026/2/16: change activate function to swish (x * sigmoid(beta * x)) (beta could be updated)
- 2026/2/17: training the model
- 2026/2/18: training the model for 6 and 12 hours
    + problem: p converges significantly slower than c, v
    + available solution: raise the weight of loss_e during training
