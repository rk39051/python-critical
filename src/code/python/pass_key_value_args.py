import argparse

print("check1")
if __name__ == "__main__":
    parser = argparse.ArgumentParser("process key value args")
    parser.add_argument("--key1", type=str, help="key1", required=True)    # Add the args

    args = vars(parser.parse_args())  # vars() need to access or manipulate an object's attributes as a dictionary

    print(f"type(args): {type(args)}")

    print(f"args: {args.get('key1')}")   # access using key
