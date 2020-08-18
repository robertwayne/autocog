from pathlib import Path
from string import Template


def generate_file(root: Path, tmp: str, cog: str):
    with open(Path(root / f'{cog.lower()}.py'), 'w') as file:
        file.write(tmp)


def read_template(template: str) -> Template:
    with open(Path(__file__).parents[1] / 'templates' / f'{template}.cog', 'r') as file:
        return Template(file.read())


def create_from_template(template: str, cogs: str, dest: str):
    for cog in cogs:
        tokens = {'NAME': cog, 'NAME_LOWER': cog.lower(), 'NAME_UPPER': cog.upper()}
        tmp = read_template(template).safe_substitute(**tokens)
        root = Path(Path.cwd() / dest if dest else 'cogs')

        try:
            generate_file(root, tmp, cog)

        except FileNotFoundError:
            root.mkdir()
            generate_file(root, tmp, cog)
