# PMCID Finder Python Program

A Python program that checks if a PubMed ID (PMID) has a corresponding PubMed Central Identifier (PMCID) available.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

PubMed Central (PMC) is a repository of full-text biomedical and life sciences journal articles. This Python program helps you determine whether a given PubMed ID (PMID) has a corresponding PMC ID (PMCID) available. It's particularly useful for researchers and authors who want to ensure their work is accessible through PMC.

## Getting Started

To get started with the PMCID Finder Python Program, follow these steps:

### Requirements

- Python 3.x
- requests library (can be installed using `pip install requests`)

### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo.git
```

2. Navigate to the project directory:

```bash
cd your-repo
```

### Usage

1. Obtain your PubMed API key by visiting the [PubMed API](https://www.ncbi.nlm.nih.gov/home/api.shtml) page.

2. Open the `pmcid_finder.py` file and replace `'YOUR_API_KEY'` with your actual PubMed API key:

```python
# Replace 'YOUR_API_KEY' with your actual PubMed API key
API_KEY = 'YOUR_API_KEY'
```

3. Run the program by executing the following command:

```bash
python pmcid_finder.py
```

4. Input a PubMed ID (PMID) when prompted.

5. The program will display whether a corresponding PMCID is available or not.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- This program utilizes the [PubMed API](https://www.ncbi.nlm.nih.gov/home/api.shtml) to retrieve information about articles.

Feel free to customize the README to match your repository's style and add any additional information you think would be helpful for users.
