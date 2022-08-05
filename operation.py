
def add(a):
    def start_add(b):
        return a + b
    return start_add


def sub(a):
    def start_sub(b):
        return a - b
    return start_sub


def mul(a):
    def start_mul(b):
        return a * b
    return start_mul


def div(a):
    def start_div(b):
        return a / b
    return start_div

def mod(a):
    def start_mod(b):
        return a % b
    return  start_mod
