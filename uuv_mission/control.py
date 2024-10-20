class PDController:
    def __init__(self, kp: float, kd: float):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0

    def compute_control_action(self, reference: float, output: float) -> float:
        error = reference - output
        derivative = error - self.previous_error
        control_action = self.kp * error + self.kd * derivative
        self.previous_error = error
        return control_action