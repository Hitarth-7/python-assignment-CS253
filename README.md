# Python Assignment CS253

This repository contains the python code for a python assignment for the course CS253 : Software Development and Operations, Spring 2025 under the Prof. Indranil Saha.

## Setup Instructions

Clone this repository using the below command in terminal.

```
git clone https://github.com/Hitarth-7/python-assignment-CS253.git
```

Run the code below to compile the files and create an executable file.

```
python filename.py
```

## Assignment Structure

The repository consists of :

### SmartTextProcessingTool.py

The tool takes two inputs:

- A unique registration number n (a positive integer) assigned to each writer.
- A content string s (a non-empty string containing only letters) representing the
  writer’s text.
- To ensure dynamic content processing, the tool follows these rules:
- `Even Registration Number`: If n is even, the tool reverses the content to reflect
  a ”mirror perspective,” inspired by ancient Sanskrit scripts.
- `Odd Registration Number`: If n is odd, the tool converts all vowels to uppercase
  (to highlight their importance) and consonants to lowercase (to soften their impact),
  just like in poetic recitations.
- `Word Pattern Extraction`: The number of 1s in the binary representation of
  n determines a substring length k. The tool extracts all substrings of length k from s
  and stores them for analysis.
- `Lexicographical Ordering for Clarity`: If the bitwise AND between n and the
  length of s results in zero, this tool sorts these extracted substrings in lexicographical order (helpful for dictionary-based archiving). Otherwise, it lists them in
  reverse order (often used for artistic effect in poetry).

#### Function Definitions for Smart Text-Processing Tool

| Function Name                       | Purpose                                                                                             |
| ----------------------------------- | --------------------------------------------------------------------------------------------------- |
| `validate_input(n, s)`              | Ensures `n` is a positive integer and `s` is a non-empty string with letters only.                  |
| `process_string(n, s)`              | Transforms the string based on the parity of `n`: reverses if even, else formats vowels/consonants. |
| `count_set_bits(n)`                 | Counts the number of 1s in the binary representation of `n` to determine substring length.          |
| `extract_substrings(s, k)`          | Extracts all substrings of length `k` from the string `s`.                                          |
| `sort_or_reverse(n, s, substrings)` | Sorts substrings lexicographically if `n & len(s) == 0`, otherwise reverses the order.              |
| `main()`                            | Manages user input, calls all necessary functions, and handles multiple test cases.                 |

### RockPaperScissors.py

RPS is a popular hand game played between two players. The rules of the game are as
follows:

- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.
  Imagine you and your friend want to decide who gets the last slice of pizza. Instead of
  arguing, you both agree to play a fair Rock-Paper-Scissors game. The winner gets the pizza,
  and if it’s a tie, you play again.

#### Function Definitions for Rock Paper Scissors game

| Function Name                  | Purpose                                                                             |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| `Rock_Paper_Scissors(user_in)` | Generates random response from the computer side and calculates the winner          |
| `main()`                       | Manages user input, calls all necessary functions, and handles multiple test cases. |

### SumOfNPrimes.py

This program calculates the sum of n primes using Seive of Eratosthenes method

#### Function Definitions for Sum Of N Primes

| Function Name        | Purpose                                                                             |
| -------------------- | ----------------------------------------------------------------------------------- |
| `validate_input(n)`  | Ensures `n` is a non negative integer.                                              |
| `sum_of_n_primes(n)` | Calculates the sum of n primes using Seive Algorithm                                |
| `main()`             | Manages user input, calls all necessary functions, and handles multiple test cases. |

### TemperatureStatisticalAnalysis.py

This program calculates the

- The mean temperature
- The median temperature
- The standard deviation
- The variance (calculated as sample variance, not population variance, using Bessel’s
  correction for an unbiased estimate).
- These calculations will help determine the fluctuations and patterns in the temperature
  data.

#### Function Definitions for Sum Of N Primes

| Function Name                        | Purpose                                                                             |
| ------------------------------------ | ----------------------------------------------------------------------------------- |
| `analyze_temperatures(temperatures)` | Calculates the mean, median, std dev and variance of the data provided.             |
| `main()`                             | Manages user input, calls all necessary functions, and handles multiple test cases. |

### LinearEquationSolver.py

This program solves a system of linear equations of
the form:
AX = B
where A is an N × N matrix and B is an N × 1 vector

| Function Name               | Purpose                                                                             |
| --------------------------- | ----------------------------------------------------------------------------------- |
| `solve_linear_system(A, B)` | Solves the Linear equation AX=B using X=A_inv\*B.                                   |
| `main()`                    | Manages user input, calls all necessary functions, and handles multiple test cases. |

### RandomDatasetGenNPreprocessor.py

This program does the following.

- Generate a synthetic dataset representing environmental observations:
- A dataset with N random points for two numerical variables X and Y .
- X values should be uniformly distributed within a user-defined range.
- Y values should be computed using a randomly generated mathematical function
  of X, following the form:
- Y = Af1(BX) + Cf2(DX) + Ef3(F X)
  where:
- A, B, C, D, E, F are randomly generated constants.
- f1, f2, f3 are randomly chosen from {sin, cos, tan, log (valid for positive X),
  square, cube}. 2. Generate visualizations to analyze patterns:
- A scatter plot of X vs Y .
- A histogram of X with an appropriate number of bins.
- A box plot of Y to detect outliers.
- A line plot of sorted X values against their corresponding Y values. 3. Enhance clarity by adding:
- Proper plot titles.
- Axis labels for better understanding.
- Legends (if applicable).
- Allows user customization:
- The number of data points (N).
- The range of values for X.
- Ensure reproducibility by setting a random seed.

### Function Definitions for Random Dataset Generator and Preprocessor

| Function Name                       | Purpose                                                                                                   |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `generate_dataset(N, x_min, x_max)` | Generates `N` random points for `X` within a range and computes `Y` using a random mathematical function. |
| `plot_scatter(X, Y)`                | Creates a scatter plot of `X` vs `Y` to visualize distribution.                                           |
| `plot_histogram(X)`                 | Plots a histogram of the `X` values to show their distribution across bins.                               |
| `plot_box(Y)`                       | Generates a box plot of `Y` to detect outliers and spread.                                                |
| `plot_line(X, Y)`                   | Creates a line plot of sorted `X` values against corresponding `Y` values.                                |
| `set_random_seed(seed)`             | Sets a fixed seed for random number generation to ensure reproducibility.                                 |

## Author

- Hitarth Makawana

- 230479
