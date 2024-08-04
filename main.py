import sys
from sensor.exception import SensorException 

def function_that_raises_error():
    # This function will raise an error for testing
    raise ValueError("This is a test error.")

def main():
    try:
        function_that_raises_error()
    except Exception as e:
        # Raise a SensorException with detailed error information
        raise SensorException("An error occurred in the application", sys) from e

if __name__ == "__main__":
    try:
        main()
    except SensorException as se:
        print(se)
