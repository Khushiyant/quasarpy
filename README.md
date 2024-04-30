![quasar-logo](https://raw.githubusercontent.com/Khushiyant/quasarpy/8346dfd09733a5e8a6c72018a011a128afabcc34/assets/logo_complete_svg.svg)
## Overview
![GitHub](https://img.shields.io/github/license/Khushiyant/quasar?&style=for-the-badge)
![Python](https://img.shields.io/badge/Made%20With%20Python-lightblue?logo=python&&style=for-the-badge&logoColor=black)

Quasar is python package that can be used for smell detection along with detailed report in various formats such as html, pdf, etc. 

# Table of contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Installation](#installation)
  - [Command Line Interface](#command-line-interface)
    - [Arguments](#arguments)
- [Contributing](#contributing)
    - [Versioning](#versioning)
- [License](#license)

## Usage

### Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install quasarpy.

```bash
pip install quasarpy
```

### Command Line Interface

Quasar can be used as a command line tool to detect smells in a project. The command line interface can be used as follows:


```bash
quasar detect --path <path_to_project> --format <format-output> --output <path_to_output_file>
```
#### Arguments

- `--path` : Path to the project directory
- `--format` : Output format of the report (html, pdf, etc.)
- `--output` : Path to the output file
- `--help` : Display help message
- `--version` : Display version of the package
- `--offline` : Run the LLM in offline mode/without internet connection (default: False)


### Contributing

#### Versioning

We use [Sementic Versioning](http://semver.org/) for versioning the package releases.

## License

This project is licensed under the GPL License - see the [LICENSE](https://github.com/Khushiyant/quasarpy/blob/164bc8d8ddfa32f8228fc886871b5a24429c61bb/LICENSE) file for details