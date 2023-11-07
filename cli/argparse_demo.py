import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test for argparse')
    parser.add_argument('--name', '-n', help='name 属性，非必要参数', action='store_true', required=False)
    parser.add_argument('--tags', '-t', nargs='*', help='tags', required=False)
    args = parser.parse_args()
    try:
        print(args.name)
        print(args.tags)
    except Exception as e:
        print(e)
