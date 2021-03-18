# COMP 100  -  PS2: Guess The Number!

### Overview

In this assignment, you will implement a number guessing game in Python, where the goal is to guess a number in minimum number of attempts. We will follow good programming practices with decomposition and abstraction. This means that your program will be divided into several reusable functions that you will complete in this assignment. 

The game starts with selecting a difficulty level for the number to be guessed. The user will enter 1 for easy, 2 for medium and 3 for hard. This difficulty level defines the range of the number as the following:

* Easy: 2 or 3 digits {: any number from 10 to 999}
* Medium: 4 or 5 digits {: any number from 1000 to 99999}
* Hard : 5 or 6 digits {: any number from 10000 to 999999 }

Once the number is randomly generated, we enter the guess loop. In this loop, the player gets a hint about the number at each step. This hint will provide information about empty slots, where the player has not guessed correctly yet. Then, the player is asked to make a guess in two steps. First, the player selects an index from `0` to `n-1`, where `0` represents the leftmost digit and `n` is the length of the digit. Then, the player makes a guess. If the guess is correct, we update the guess list and empty indexes to move on. If there are no empty indices left, we exit the loop.

### Part I: First Things First

You have a starter code which serves as a skeleton. First, we start with skimming the `main()` function, where the execution of your program starts. In this part, the program gets an input from the user to set the difficulty level. Then, this difficulty level (as an integer) is passed to the `set_level()` function.

**Task I**: 

* Implement the `set_level()` function which takes the integer difficulty level as an argument, and then generates the number of digits randomly for our number following the difficulty level definition above.

* After randomly selecting the number of digits, we generate a random number with the `generate_random_number()` function, given `num_digits` as the argument. For example, for `num_digits = 3`, the generated random number can be 487.


**Task II**:

After implementing these functions properly, you can move on to implementing three other important functions:

`init_guess_list()` , `get_empty_slots()` and `create_guess_str()`.

* We use `init_guess_list()`  function to initialize a list for guessing the number. It takes number of digits (`N`) as the input and returns a list of length `N`, where all of the elements are "`_`" underscore characters. We use this list as a memory variable of our correct guesses.
  * Example usage: `init_guess_list(5)` returns `['_', '_', '_', '_', '_']`
* We implement one more function called `get_empty_slots()`. It takes a `guess_list` as an argument and returns the indices where there is an underscore, meaning an empty slot.
  * Example usage: `get_empty_slots(['_', '7', '_'])` returns `[0,2]`
* Finally, we implement a function `create_guess_str()` that converts a `guess_list` to a readable string, delimited by a whitespace character.
  * Example usage: `create_guess_str(['_', '7', '_'])` returns `_ 7 _`

**Import Remark**: Please do not use numpy, pandas for generating the random number, and use the standard random library instead.

### Part II: Hint Maker

We will implement a hint-making mechanism for our number to be guessed. For this mechanism, we have a master-function called `hint_maker()` which takes two arguments `number`, `guess_list` and `empty_slots`. 

Recall that these parameters are:
* `number` is the randomly generated number to be guessed
* `guess_list` is the memory variable that holds correct guesses
* `empty_slots` is the list of empty slots (which are not guessed yet)

Here, our aim is to give hints that are as informative as possible. To have this property, follow these steps:

1. Select an empty index from empty list and assign it to `empty_index` variable.
**Hint**: You can use `random.sample()` for selecting an empty index.
2. Select another index `second_idx` in cases where we use hint functions that requires two digits. 
3. Randomly generate a digit (0-9) `temp_digit` to make comparisons with a digit from our number.
4. Finally, randomly generate another integer `hint_idx` that allows us to select a hint.

We are all set! We can proceed to implement mathematical functions that will provide the hints:

* `all_digits_mean(number)`: takes the number as the argument, returns the mean of all the digits in the number.
* `all_digits_sum(number)`: takes the number as the argument, returns the sum of all the digits in the number.
* `two_digits_mean(number, empty_idx, second_idx)`: takes the number, and two digit indices as the argument, and returns the mean of them.
* `two_digits_sum(number, empty_idx, second_idx)`: takes the number, and the two digit indices as the argument, returns the sum of them.
* `two_digits_diff(number, empty_idx, second_idx)`: takes the number, and the two digit indices as the argument, and returns the difference (empty-second) of them.
* `is_larger(number, empty_idx, temp_digit)`: takes the number, an empty index and a temporary digit and returns `True` if the number is larger than temp_digit, otherwise `False`.
* `is_factor(number, temp_digit)`: takes the number, and the temp digit and returns `True` if the number is a factor of the temp digit.
* `calc_remainder(number, temp_digit)`: Returns the remainder when we divide number by the temp digit.

### Part III: Make a Guess!

Go to the `make_guess()` function and read the skeleton code. We provide the code for the part to take input from the user. Get the guess, set the `result` variable to `True` if the guess is correct, otherwise set it to `False`. Update the `guess_list` so that the player can see the progress.

### Part IV: Play the game!

As programmers, it is our responsibility to make sure that our code is doiing what we expect it to do. Play the game with your implementation a few times with different inputs. Then, run the tests provided by submitting your work to the GitHub.