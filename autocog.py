#!/usr/bin/env python

import argparse

from autocog_cli import template_parsers


def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    new_parser = subparser.add_parser('new', help='Generates a new cog file.')
    new_parser.add_argument('cogs', type=str, nargs='+')
    new_parser.add_argument('-t', '--template', help='Which template to use when generating the cog.')
    new_parser.add_argument('-a', '--typed', help='Type annotates the generated cog. Can only be used with builtin templates.', nargs='?', const=True)
    new_parser.add_argument('-d', '--dest', type=str, help='Set the path the cog will be created in. Defaults to current directory.')

    parser.add_argument('-v', '--version', help='Current version of autocog.', action='version', version='autocog v0.1.0')

    args = parser.parse_args()
    try:
        template = args.template if args.template else 'typed_base' if args.typed else 'base'

    except AttributeError:
        return print('Project generation CLI not implemented yet. Please refer to autocog --help')

    template_parsers.create_from_template(template, args.cogs, args.dest)
    print(f'Successfully created files!')
    print('\n'.join([f" + {cog.lower()}.py" for cog in args.cogs]))


if __name__ == '__main__':
    main()
