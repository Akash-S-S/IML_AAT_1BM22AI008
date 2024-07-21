#!/bin/python3
import sys

def clean_input(string):
    return [float(x) for x in string.strip().split(",")]

def read_training_data(filename, num_instances):
    training_data = {}
    with open(filename, "r") as file:
        for _ in range(num_instances):
            instance = clean_input(file.readline())
            training_data[instance[0]] = instance[1]
    return training_data

def sum_xys(data):
    return sum(x * y for x, y in data.items())

def sum_xs(data):
    return sum(data.keys())

def sum_ys(data):
    return sum(data.values())

def sum_x_sqrd(data):
    return sum(x**2 for x in data.keys())

def linear_regression(data):
    n = len(data)
    xys = sum_xys(data)
    xs = sum_xs(data)
    ys = sum_ys(data)
    x_sqrd = sum_x_sqrd(data)
    
    denominator = (n * x_sqrd) - (xs**2)
    if denominator == 0:
        raise ValueError("Denominator in linear regression calculation is zero.")
    
    m = ((n * xys) - (xs * ys)) / denominator
    b = ((x_sqrd * ys) - (xs * xys)) / denominator
    
    return m, b

def estimate_life(chrg_time, lin_vars, full_battery, max_life):
    if chrg_time >= full_battery:
        return max_life
    else:
        m, b = lin_vars
        return (m * chrg_time) + b

def main():
    data = float(sys.stdin.readline().strip())
    num_instances = 100
    filename = "trainingdata.txt"

    training_data = read_training_data(filename, num_instances)
    
    max_life = max(training_data.values())
    max_case = {k: v for k, v in training_data.items() if v == max_life}
    lin_case = {k: v for k, v in training_data.items() if v < max_life}

    if not lin_case:
        raise ValueError("No data available for linear regression.")

    full_battery = min(max_case.keys(), default=0)

    lin_vars = linear_regression(lin_case)

    batt_life = estimate_life(data, lin_vars, full_battery, max_life)
    
    print(batt_life)

if __name__ == '__main__':
    main()



