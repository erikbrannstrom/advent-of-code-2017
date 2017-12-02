import test_data
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("day")
parser.add_argument("--test", help="run tests", action="store_true")
args = parser.parse_args()


def run_test(day):
    day_module = __import__(day)
    test_cases = getattr(test_data, day)

    def run_case(test_cases, fn, star):
        success = True
        for test_case in test_cases:
            output = fn(test_case[0])
            if output != test_case[1]:
                success = False
                print("Star {}: Expected input {} to return {}, received {}".format(
                star, test_case[0], test_case[1], output))
        return success

    success = run_case(test_cases[0], day_module.first, 1)
    if hasattr(day_module, "second"):
        success = success and run_case(test_cases[1], day_module.second, 2)

    if success:
        print("All tests for {} were successful.".format(day))


def get_input_data(day, first_star=True):
    star = "a" if first_star else "b"

    path = "inputs/{}-{}.txt".format(day, star)
    if not os.path.exists(path):
        path = "inputs/{}.txt".format(day)

    with open(path) as file:
        return file.read()


def generate_output(day):
    day_module = __import__(day)

    if hasattr(day_module, "first"):
        data = get_input_data(day, True)
        print("Star 1: {}".format(day_module.first(data)))

    if hasattr(day_module, "second"):
        data = get_input_data(day, False)
        print("Star 2: {}".format(day_module.second(data)))


def main():
    if args.test:
        run_test(args.day)
        return

    generate_output(args.day)

if __name__ == "__main__":
    main()
