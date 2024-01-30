from radon.cli.harvest import (
    CCHarvester,
    HCHarvester,
    MIHarvester,
    RawHarvester,
)
import os
from radon.cli import Config
from radon.cli import log_result
from radon.cli import outstream

def analyse(path: str, type: str):
    config = Config(
        exclude=None,
        ignore=None,
        summary=False,
        show_closures=False,
        min='A',
        max='F',
        exclude_patterns=None,
        ignore_patterns=None,
        order=None,
        no_assert=False,
        show_complexity=False,
        total_average=False,
        show_multi=False,
        average=False,
        json=False,
        xml=False,
        show_mi=False,
        show_closures_complexity=False,
        nb=False,
        show_halstead=False,
        show_raw=False,
        show_cyclomatic=False,
        show_cyclomatic_complexity=False,
        show_all=False,
        exclude_self=False,
        ignore_decorators=False,
        ignore_imports=False,
        ignore_defaults=False,
        ignore_trailing=False,
        ignore_closures=False,
        ignore_all=False,
        ignore_closures_complexity=False,
        ignore_halstead=False,
        ignore_mi=False,
        ignore_cyclomatic=False,
        ignore_cyclomatic_complexity=False,
        ignore_coding=False,
        ignore_blocks=False,
        ignore_inline=False,
        ignore_function_length=False,
        ignore_long=False,
        ignore_docstrings=False,
        ignore_string_formatting=False,
        ignore_literals=False,
        ignore_comments=False,
    )
    if os.path.exists(path):
        harvester = RawHarvester(path, config)
    else:
        raise Exception('Path does not exist')

    with outstream("output_file.json") as stream:
        log_result(harvester, json=True, stream=stream)