# Mutation Testing Demo

This project demonstrates the use of mutation testing in Python using [`mutmut`](https://github.com/boxed/mutmut). Mutation testing helps in evaluating the quality of your test cases by introducing changes (mutations) to your code and checking if your tests can detect these changes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.10.13
- pipenv

If you don't have `pipenv` installed, you can install it via pip:

```bash
pip install pipenv
```

### Installation

First, clone the repository to your local machine:

```bash
git clone https://github.com/hernanzini/python/mutmut_demo
cd path/to/cloned/repository
```

Then, use pipenv to create a virtual environment and install the required dependencies:

```bash
pipenv install --dev
```

This will create a virtual environment and install the packages defined in Pipfile.

To interact with the project within the virtual environment, you have two options:

#### 1. Activating the virtual environment:
```bash
pipenv shell
```

#### 2. Running commands directly:
If you prefer not to activate the virtual environment, you can still run commands within it by prefixing them with `pipenv run <command>`.


### Running the Tests
To run the standard test suite using pytest:

```bash
pytest -v
```

### Running `mutmut`
To perform mutation testing with mutmut:
```bash
mutmut run
```
After running mutation testing, you can check the results with:

```bash
mutmut results
```
To apply a mutant on disk:
- `mutmut apply <id>`

To show a mutant:
- `mutmut show <id>`

To view a more detailed HTML report of the mutation testing results:

```bash
mutmut html
```
Then, open the generated HTML file in your browser to view the report.

```bash
open html/index.html
```

#### Automation with a Script
For convenience, a script named `mutmut.sh` is included to automate the mutation testing process, generate the HTML report, and open it:

```bash
./mutmut.sh
```

### Contributing
We welcome contributions to the Mutation Testing Demo! If you have an improvement or a bug fix, please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name for your feature or bug fix.
3. Implement your changes. Make sure your code follows the project's style and has been tested.
4. Submit a pull request with a clear description of what your changes are.

### License
This project is made available under the terms of the [MIT License](https://opensource.org/licenses/MIT).
By contributing to or using the Mutation Testing Demo, you agree to abide by its terms.