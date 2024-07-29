class Parent:
    def __init__(self, value):
        self.value = value

parent = Parent("example_value")

def configure_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Passing keyword arguments to the function
configure_parameters(
    param1="value1",
    value=parent.value,
    param3="value3"
)
