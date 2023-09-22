import math
import sys

def linear_regression_formula(x_values, y_values):
    n = len(x_values)
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    # special python syntax for looping was used, same as in golang basically
    # the zip() func, for who's curious, creates parallel tuples
    # check README.md for more info
    sum_xy = sum(x * y for x, y in zip(x_values, y_values))
    sum_x2 = sum(x**2 for x in x_values)

    # y2-y1 / x2 - x1
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    intercept = (sum_y - slope * sum_x) / n

    slope = "{:.6f}".format(round(slope, 6))
    intercept = "{:.6f}".format(round(intercept, 6))

    # f = string literal declaration, python weird

    return f"y = {slope}x + {intercept}"


def pearson_correlation_coefficient(x_values, y_values):
    n = len(x_values)
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_xy = sum(x * y for x, y in zip(x_values, y_values))
    sum_x2 = sum(x**2 for x in x_values)
    sum_y2 = sum(y**2 for y in y_values)

    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))

    correlation_coefficient = numerator / denominator

    correlation_coefficient = round(correlation_coefficient, 10)
    formatted_coefficient = "{:.10f}".format(correlation_coefficient)

    return formatted_coefficient


def read_numbers_from_file(file_path):
    yvals = []
    xvals = []
    start = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    yvals.append(number)
                    xvals.append(start)
                    start+=1
                except ValueError:
                    print(f"Invalid number format: {line}")
                    exit(1)
    except FileNotFoundError:
        print("Data File Doesnt exist")
        exit(1)


    return yvals, xvals

# checking terminal argument length
if len(sys.argv) != 2:
    print("Incorrect Terminal Argument Amount")
    exit(1)

data = read_numbers_from_file(sys.argv[1])
print("Linear Regression Line:", linear_regression_formula(data[1], data[0]))
print("Pearson Correlation Coefficient:", pearson_correlation_coefficient(data[1], data[0]))
