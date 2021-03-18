import random

def set_level(level):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return num_digits


def generate_random_number(digits):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return n


def get_ith_digit(number, i):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return digit


def calc_remainder(num, divisor):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return remainder


def is_factor(num, divisor):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return result


def is_larger(num, i, target):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return result


def two_digits_diff(num, idx_1, idx_2):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return result


def two_digits_sum(num, idx_1, idx_2):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return result


def two_digits_mean(num, idx_1, idx_2):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return result


def all_digits_sum(num):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return result


def all_digits_mean(num):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return result



def init_guess_list(length):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return l


def create_guess_str(guess_list):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return guess_str


def get_empty_slots(l):

  # START OF YOUR CODE

  # END OF YOUR CODE

  return empty_slots



def hint_maker(number, guess_list, empty_slots):

  # START OF YOUR CODE

  # END OF YOUR CODE

  if hint_idx == 0:
    value = all_digits_mean(number)
    print(f"Mean of all digits is: {value}")
  elif hint_idx == 1:
    value = all_digits_sum(number)
    print(f"The sum of all digits is: {value}")
  elif hint_idx == 2:
    value = two_digits_mean(number, empty_idx, second_idx)
    print(f"The mean of digit {empty_idx} and digit {second_idx} is {value}")
  elif hint_idx == 3:
    value = two_digits_sum(number, empty_idx, second_idx)
    print(f"The sum of digit {empty_idx} and digit {second_idx} is {value}")
  elif hint_idx == 4:
    value = two_digits_diff(number, empty_idx, second_idx)
    print(f"The difference between digit {empty_idx} and digit {second_idx} is {value}")
  elif hint_idx == 5:
    value = is_larger(number, empty_idx, temp_digit)
    if value:
      print(f"The {empty_idx}th digit is larger than {temp_digit}")
    else:
      print(f"The {empty_idx}th digit is smaller than {temp_digit}")
  elif hint_idx == 6:
    value = is_factor(number, temp_digit)
    if value:
      print(f"The {temp_digit} is a factor of the number")
    else:
      print(f"The {temp_digit} is not a factor of the number")
  elif hint_idx == 7:
    value = calc_remainder(number, temp_digit)
    print(f"The remainder of the number is {value}, when the number is divided by {temp_digit}")
  else:
    pass

def make_guess(number, guess_list, empty_slots):

  i = input(f"Select an index. The empty slots are: {empty_slots}")

  # Make a guess
  guess = input(f"Make a guess:")

  # START OF YOUR CODE

  # END OF YOUR CODE


  return result, guess_list


def main():
  # The game starts with selecting a difficulty level.
  level = input("Please select a difficulty level. Enter 1 for easy, 2 for medium and 3 for hard:")
  level = int(level)

  difficulties = ["easy", "medium", "hard"]
  print(f"You selected: {difficulties[int(level) - 1]}")

  # Decide how many digits we have
  num_digits = set_level(level)

  # Get the random number
  number = generate_random_number(num_digits)
  guess_list = init_guess_list(num_digits)
  print(number)

  # Set this variable to True when the game is finished.
  is_finished = False
  attempts = 0
  while not is_finished:

    print("")
    empty_slots = get_empty_slots(guess_list)
    print(empty_slots)

    if empty_slots == []:
      print("Success!")
      print(f"Total attempts: {attempts}")
      is_finished = True
      continue

    print(f"### Attempts: {attempts} - Remaining Digits: {len(empty_slots)} ###")
    print("")
    print(f"Number: {create_guess_str(guess_list)}")
    print("")
    hint_maker(number, guess_list, empty_slots)
    result, guess_list = make_guess(number, guess_list, empty_slots)

    if result:
      print("Correct!")
    else:
      print("Please try again.")

    attempts += 1


if __name__ == '__main__':
  main()
