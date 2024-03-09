from radon.cli.harvest import (
    RawHarvester, CCHarvester, MIHarvester
)
from radon.cli import Config


def analyse(path, exclude=None, ignore=None, show_closures=False, no_assert=False, order='SCORE', json=False, **kwargs):
    """
    Analyzes the given path using different harvesters and returns the results.

    Args:
        path (str): The path to analyze.
        exclude (list, optional): List of patterns to exclude from analysis. Defaults to None.
        ignore (list, optional): List of patterns to ignore during analysis. Defaults to None.
        show_closures (bool, optional): Whether to show closures in the analysis results. Defaults to False.
        no_assert (bool, optional): Whether to exclude assert statements from the analysis. Defaults to False.
        order (str, optional): The order in which to display the analysis results. Defaults to 'SCORE'.
        json (bool, optional): Whether to return the results in JSON format. Defaults to False.
        **kwargs: Additional keyword arguments.

    Returns:
        tuple: A tuple containing the results from different harvesters:
            - harvester: RawHarvester object containing raw analysis results.
            - cc_harvester: CCHarvester object containing cyclomatic complexity analysis results.
            - mi_harvester: MIHarvester object containing maintainability index analysis results.
    """
    config = Config(
        exclude=exclude,
        ignore=ignore,
        show_closures=show_closures,
        no_assert=no_assert,
        order=order,
        json=json,
        **kwargs
    )
    harvester = RawHarvester(path, config)
    cc_harvester = CCHarvester(path, config)
    mi_harvester = MIHarvester(path, config)
  
    return harvester, cc_harvester, mi_harvester
