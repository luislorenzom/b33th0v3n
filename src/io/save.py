import json


def save_output(output: dict, output_path: str) -> None:
    """
    Save output analyzer

    :param output: data after analyze
    :param output_path: where output is going to be save

    :return: None
    """
    with open(output_path, 'w') as f:
        json.dump(output, f)
