class Sequential:
    def __init__(self, *optims):
        self.optims = optims
        
    def __call__(self, x):
        for optim in self.optims:
            x = optim(x)
        return x
