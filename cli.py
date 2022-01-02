import psycopg2
from tabulate import tabulate
import click


connection_string = "host='db' user='postgres' dbname='postgres'"
conn = psycopg2.connect(connection_string)

cur = conn.cursor()


@click.group()
def main():
    pass


@main.command(name='select')
@click.option('-n', '--neighbourhood')
@click.option('-r', '--reviews')
def select(neighbourhood, reviews):
    if neighbourhood:
        offset = 0
        while True:
            cur.execute(
                f'SELECT id, name, host_id, neighbourhood, price FROM rooms\
                    WHERE neighbourhood=%s LIMIT 20 OFFSET %s;',
                (neighbourhood.strip(), offset)
            )
            result = cur.fetchall()
            if not result:
                exit()
            click.echo(tabulate(result, headers=['id', 'name', 'host_id', 'neighbourhood', 'price']))

            click.echo("\nClick 'n' to see next 20 rooms.\nClick 'p' to see previous 20 rooms.\nClick 'q' to exit.")
            cmd = input()
            if cmd.lower().strip() == 'n':
                offset += 20
            elif cmd.lower().strip() == 'p':
                if offset >= 20:
                    offset -= 20
            elif cmd.lower().strip() == 'q':
                exit()
            else:
                click.echo("Unknown command")
                exit()
    elif reviews:
        offset = 0
        while True:
            cur.execute(
               'SELECT reviews.listing_id, reviewers.reviewer_name, reviews.comment FROM reviews\
                JOIN reviewers ON reviews.reviewer_id=reviewers.reviewer_id\
                WHERE listing_id=%s LIMIT 20 OFFSET %s;',
                (reviews, offset)
            )
            result = cur.fetchall()
            if not result:
                exit()
            click.echo(f"Reviews for room {reviews}")
            for r in result:
                click.echo(f"Reviewer: {r[1]}\nReview: {r[2]}\n-------------------------------")

            click.echo("\nClick 'n' to see next 20 rooms.\nClick 'p' to see previous 20 rooms.\nClick 'q' to exit.")
            cmd = input()
            if cmd.lower().strip() == 'n':
                offset += 20
            elif cmd.lower().strip() == 'p':
                if offset >= 20:
                    offset -= 20
            elif cmd.lower().strip() == 'q':
                exit()
            else:
                click.echo("Unknown command")
                exit()
        



if __name__ == '__main__':
    main()

