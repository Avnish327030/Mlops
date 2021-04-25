import os
import yaml
import argparse
import logging

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="default")
    args.add_argument("--datasource", default=None)
    print(os.getcwd())
    parsed_arg = args.parse_args()
    print(f"Parsed arguments:{parsed_arg}\n Config:{parsed_arg.config}")

