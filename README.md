# sofascore

[sofascore](https://www.github.com/shimst3r/sofascore) is a Python package for computing the [SOFA score](https://en.wikipedia.org/wiki/SOFA_score) according to [Singer et al.](https://doi.org/10.1001%2Fjama.2016.0287)

## Use Cases

Use sofascore wherever you are interested in computing the SOFA score, i.a.

- Clinical Decision Support Systems
- Research
- Smart Medical Devices (as sofascore only uses the standard library, it can be easily adapted to [MicroPython](https://micropython.org) based microcontrollers)

## Installation

sofascore is available on PyPI, so you can install it easily via

```shell
pip install sofascore
```

For manual installation, check the [Release](https://github.com/shimst3r/sofascore/releases/tag/v1.0.0) page.

## Pre-Commit Hooks

The project comes with a [.pre-commit-config.yaml](./.pre-commit-config.yaml) file for configuring pre-commit hooks via [pre-commit](https://pre-commit.com). To install the hooks, install pre-commit on your system (see the [installation guide](https://pre-commit.com/#install)) and run

```shell
pre-commit install
pre-commit run -a
```

## License

> Copyright 2021 shimst3r
>
> Licensed under the Apache License, Version 2.0 (the "License");
> you may not use this file except in compliance with the License.
> You may obtain a copy of the License at
>
>     http://www.apache.org/licenses/LICENSE-2.0
>
> Unless required by applicable law or agreed to in writing, software
> distributed under the License is distributed on an "AS IS" BASIS,
> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> See the License for the specific language governing permissions and
> limitations under the License.
