from radon.cli.harvest import (
    RawHarvester, CCHarvester, MIHarvester
)
from radon.cli import Config


def analyse(path, exclude=None, ignore=None, show_closures=False, no_assert=False, order='SCORE', json=False, **kwargs):
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
