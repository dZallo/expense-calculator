import argparse


def main():
    print('Hello World')
    parser = argparse.ArgumentParser()

    parser.add_argument("excel")
    args = parser.parse_args()
    print(f"Procesando: {args.excel}")


if __name__ == '__main__':
    main()