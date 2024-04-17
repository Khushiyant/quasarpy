from radon.cli.harvest import RawHarvester
from ast import literal_eval
from typing import Dict, Any
from radon.cli import Config
from radon.metrics import h_visit
from quasar.utils.errors import LiteralEvalError


def analyse(paths: list, exclude: str = None, ignore=None, show_closures=False, no_assert=False, order='SCORE', **kwargs) -> Dict[str, Any]:
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
        raw_json = literal_eval(raw.as_json())
    except LiteralEvalError:
        raise LiteralEvalError("Unable to evaluate the literal string")

    combined_json = {key: {
        **value, **{k: round(v, 2) if isinstance(v, float) else v for k, v in h_visit(open(key).read()).total._asdict().items()}} for key, value in raw_json.items()}

    return combined_json
