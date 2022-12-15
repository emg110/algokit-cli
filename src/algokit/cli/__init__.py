import click
from algokit.cli.bootstrap import bootstrap_group
from algokit.cli.doctor import doctor_command
from algokit.cli.goal import goal_command
from algokit.cli.init import init_command
from algokit.cli.sandbox import sandbox_group
from algokit.core.conf import PACKAGE_NAME
from algokit.core.log_handlers import color_option, verbose_option


@click.group(
    help="AlgoKit is your one-stop shop to develop applications on the Algorand blockchain.",
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.version_option(package_name=PACKAGE_NAME)
@verbose_option
@color_option
def algokit() -> None:
    pass


algokit.add_command(init_command)
algokit.add_command(sandbox_group)
algokit.add_command(goal_command)
algokit.add_command(bootstrap_group)
algokit.add_command(doctor_command)
