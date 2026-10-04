import argparse
import sys

from src.toolkit.calculator import calc
from src.toolkit.converter import convert


def main():
    parser = argparse.ArgumentParser(description="калькулятор")

    subparsers = parser.add_subparsers(dest = 'use_module', required=True,  help = 'module')




    calc_parser = subparsers.add_parser('calc', help = 'use calculator: {calc} {"EXPRESSION"}')

    calc_parser.add_argument('mathematical_expression', type = str, help='calculator format: {"EXPRESSION"}')




    convert_parser = subparsers.add_parser('convert', help = 'use converter: {conver} {VALUE} {--from} {UNIT} {--to} {UNIT}')
    
    convert_parser.add_argument('value', type = float, help = 'converter format: {VALUE}')
    convert_parser.add_argument('--from', type = str, dest='fromunit', required=True,  help = 'calculator format: {"EXPRESSION"}')
    convert_parser.add_argument('--to', type = str, dest='tounit', required=True,  help = 'calculator format: {"EXPRESSION"}')




    args = parser.parse_args()

    try:
        if args.use_module == 'calc':
            result = calc(args.mathematical_expression)
            sys.stdout.write(str(result) + "\n")

            return 0
            
        elif args.use_module == 'convert':
            result = convert(args.value, args.fromunit, args.tounit)
            sys.stdout.write(str(result) + "\n")

            return 0
            
    except ValueError as e:
        sys.stderr.write(f'ошибка: {e}\n')
        
        return 2


if __name__ == "__main__":
    sys.exit(main())
