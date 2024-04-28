from radon.cli.harvest import RawHarvester
from radon.cli import Config
from radon.metrics import h_visit
from quasarpy.utils.errors import LiteralEvalError
import json


def analyse(paths: list, exclude: str = None, ignore=None, show_closures=False, no_assert=False, order='SCORE', **kwargs) -> str:
    """
    Analyzes the given path using different harvesters and returns the results.

    Args:
        paths (list): List of paths to analyze.
        exclude (str, optional): Pattern to exclude from analysis. Defaults to None.
        ignore (list, optional): List of patterns to ignore during analysis. Defaults to None.
        show_closures (bool, optional): Whether to show closures in the analysis results. Defaults to False.
        no_assert (bool, optional): Whether to exclude assert statements from the analysis. Defaults to False.
        order (str, optional): The order in which to display the analysis results. Defaults to 'SCORE'.
        **kwargs: Additional keyword arguments.

    Returns:
        dict: A dictionary containing the results from different harvesters:
            - 'harvester': RawHarvester object containing raw analysis results.
            - 'mi_harvester': MIHarvester object containing maintainability index analysis results.
    """
    config = Config(
        exclude=exclude,
        ignore=ignore,
        show_closures=show_closures,
        no_assert=no_assert,
        order=order,
        **kwargs
    )

    raw = RawHarvester(paths, config)

   
    try:
        raw_json = json.loads(raw.as_json())
    except json.JSONDecodeError:
        raise LiteralEvalError("Error decoding JSON")

    combined_json = {key: {
        **value, **{k: round(v, 2) if isinstance(v, float) else v for k, v in h_visit(open(key).read()).total._asdict().items()}} for key, value in raw_json.items()}

    return combined_json
