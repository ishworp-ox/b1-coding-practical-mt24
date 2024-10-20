class PDController:
    def __init__(self, kp: float, kd: float): #initalises the controller
        #Proportional and Derivative Gains
        self.kp = kp
        self.kd = kd
        # inital error from previous control action
        self.previous_error = 0.0

    def compute_control_action(self, reference: float, output: float) -> float: # Computes control action using reference signal and current output
        error = reference - output
        derivative = error - self.previous_error
        control_action = self.kp * error + self.kd * derivative
        self.previous_error = error
        return control_action