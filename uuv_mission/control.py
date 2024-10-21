class PDController:
    def __init__(self, K_P: float, K_D: float):
        self.K_P = K_P
        self.K_D = K_D
        self.previous_error = 0

    def compute_action(self, reference: float, output: float) -> float:
        error = reference - output
        derivative = error - self.previous_error
        action = self.K_P * error + self.K_D * derivative
        self.previous_error = error
        return action