import click

from stat_tools.sampling import compute_sample_size


@click.group()
def cli():
    pass


@click.command("sample_size")
@click.option("--conflvl", help="Confidence Level (0<x<1)", type=float, default=0.95)
@click.option("--marginerr", help="Margin error (0<x<1)", type=float, default=0.05)
@click.option(
    "--proportion", help="Estimated proportion (0<x<1)", type=float, default=0.5
)
@click.option("--size", help="Population Size", type=int, default=None)
@click.option("--how", help="Method, cochran or yamane", type=str, default="cochran")
def sample_size(conflvl, marginerr, proportion, size, how):
    print(compute_sample_size(conflvl, marginerr, proportion, size, how))


cli.add_command(sample_size)

if __name__ == "__main__":
    cli()
