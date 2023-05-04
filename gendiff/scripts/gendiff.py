import argparse
from gendiff.scripts.file_parser import read_file


def generate_diff(first_file, second_file):
    data1 = read_file(first_file)
    data2 = read_file(second_file)
    diff = []
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f"    {key}: {str(data1[key]).lower()}")
            else:
                diff.append(f"  - {key}: {str(data1[key]).lower()}")
                diff.append(f"  + {key}: {str(data2[key]).lower()}")
        elif key in data1:
            diff.append(f"  - {key}: {str(data1[key]).lower()}")
        else:
            diff.append(f"  + {key}: {str(data2[key]).lower()}")
    return "{\n" + "\n".join(diff) + "\n}"


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration\
                                      files and shows a difference."
    )
    parser.add_argument("first_file", type=str, help="First file to compare")
    parser.add_argument("second_file", type=str, help="Second file to compare")
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
