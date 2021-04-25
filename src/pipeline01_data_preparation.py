import os
import yaml
import argparse
import logging


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def main(config_path , data_source):
    config = read_params(config_path=config_path)
    print(config)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    path = r"D:\MLOPS\wafer_mlops"
    config_path = r"\config\params.yaml"
    default_config_path =path+config_path
    args.add_argument("--config", default=default_config_path)
    args.add_argument("--datasource", default=None)
    print(os.getcwd())
    parsed_arg = args.parse_args()
    main(config_path=parsed_arg.config, data_source=parsed_arg.datasource)
    # print(f"Parsed arguments:{parsed_arg}\n Config:{parsed_arg.config}")
