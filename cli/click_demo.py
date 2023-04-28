import click


@click.command()
@click.option('--name', default='Leijun', help='name 参数，非必须，有默认值')
@click.option('--year', help='year 参数', type=int)
@click.option('--body', help='body 参数', required=True)
def test_for_sys(year, name, body):
    print('the year is', year)
    print('the name is', name)
    print('the body is', body)


if __name__ == '__main__':
    test_for_sys()
