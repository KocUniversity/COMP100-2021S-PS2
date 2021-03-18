from ps2 import *

## MAIN LOOP FUNCTIONS

def test_set_level():

  fail = False

  # Test each level 5 times.
  levels = [1, 2, 3]

  for level in levels:
    for i in range(5):
      num_digits = set_level(level)
      if level == 1 and not (num_digits == 2 or num_digits == 3):
        fail = True
        print("Problem in level 1 difficulty. Returned num_digits: ", num_digits)
      elif level == 2 and not (num_digits == 4 or num_digits == 5):
        fail = True
        print("Problem in level 2 difficulty. Returned num_digits: ", num_digits)
      elif level == 3 and not (num_digits == 5 or num_digits == 6):
        fail = True
        print("Problem in level 3 difficulty. Returned num_digits: ", num_digits)

  assert not fail

  if fail:
    return 0
  else:
    print("Success in test_set_level")
    return 5

def test_generate_random_number():

  fail = False

  for i in range(2, 5):
    number = generate_random_number(i)

    if len(str(number)) != i:
      fail = True
      print("Problem when creating a ", i, " digit random number.")

  assert not fail

  if fail:
    return 0
  else:
    print("Success: test_generate_random_number")
    return 10

def test_get_ith_digit():

  cases = [[43456, 3, 5], [12345, 4, 5], [11, 1, 1], [459, 2, 9], [424, 1, 2], [1000000000, 0, 1]]
  fail = False

  for case in cases:

    number, i, true_val = case[0], case[1], case[2]
    val = get_ith_digit(number, i)

    if val != true_val:
      print("Problem. Number: ", number, " i: ", i, " true val: ", true_val, " fn returned: ", val)
      fail = True

  assert not fail

  if fail:
    return 0
  else:
    print("Success: test_get_ith_digit")
    return 10


def test_get_empty_slots():
  fail = False

  cases = [[[2, '_', '_', 3], [1, 2]],
           [[2, 3], []],
           [['_', '_', 3], [0, 1]]]

  for case in cases:

    l, gt = case[0], case[1]

    sl = get_empty_slots(l)

    if gt != sl:
      fail = True

  assert not fail

  if fail:
    return 0
  else:
    print("Success: test_get_empty_slots")
    return 5


def test_create_guess_str():

  fail = False

  guess_list = [2,'_', 3, '_']
  guess_str = create_guess_str(guess_list)

  if guess_str != "2 _ 3 _":
    print("Problem in guess str: ", guess_str)
    fail = True

  assert not fail

  if fail:
    return 0
  else:
    print("Success: test_create_guess_str")
    return 5


def test_init_guess_list():

  fail = False

  cases = [[['_', '_', '_'], 3], [['_', '_'], 2]]

  for case in cases:
    gt, length = case[0], case[1]
    l = init_guess_list(length)

    if l != gt:
      fail = True

  assert not fail

  if fail:
    return 0
  else:
    print("Success: test_init_guess_list")
    return 5


## HINT FUNCTIONS: ALL DIGITS

def test_all_digits_sum():

  fail = False
  cases = [[1000, 1], [1001,  2], [51, 6], [999, 27], [555, 15], [729,18]]

  for case in cases:
    number, true_sum = case[0], case[1]
    val = all_digits_sum(number)

    if val != true_sum:
      print("Problem. Number: ", number, " True Sum: ", true_sum, " Function Returned: ", val)
      fail = True

  assert not fail

  if fail:
    return 0
  else:
    print("Success: test_all_digits_sum")
    return 5

def test_all_digits_mean():

  fail = False
  cases = [[1000, 0.25], [1001,  0.5], [51, 3], [999, 9], [555, 5], [729,6]]

  for case in cases:

    number, true_sum = case[0], case[1]
    val = all_digits_mean(number)

    if val != true_sum:
      print("Problem. Number: ", number, " True Mean: ", true_sum, " Function Returned: ", val)
      fail = True

  assert not fail

  if fail:
    return 0
  else:
    print("Success: test_all_digits_mean")
    return 5


def test_is_factor():
  fail = False

  cases = [[3020, 5, True],
           [2131, 2, False],
           [49, 7 , True],
           [423, 3, True],
           [111, 3, True]]
  for case in cases:

    number, divisor, gt = case[0], case[1], case[2]
    result = is_factor(number, divisor)

    if result != gt:
      print("Problem. Num: ", number, " divisor: ", divisor,  " result: ", result, " gt: ", gt)
      fail = True

  if fail:
    return 0
  else:
    print("Success: test_is_factor")
    return 5

def test_calc_remainder():

  fail = False

  cases = [[3020, 5, 0],
           [3024, 5, 4],
           [2131, 2, 1],
           [49, 7, 0],
           [423, 3, 0],
           [111, 3, 0]]

  for case in cases:

    number, divisor, gt = case[0], case[1], case[2]
    result = is_factor(number, divisor)

    if result != gt:
      print("Problem. Num: ", number, " divisor: ", divisor, " result: ", result, " gt: ", gt)
      fail = True

  if fail:
    return 0
  else:
    print("Success: test_calc_remainder")
    return 5


def test_is_larger():

  fail = False
  cases = [[43456, 3, 4, True],
           [12345, 4, 5, False],
           [11, 1, 0, True],
           [459, 2, 9, False],
           [424, 1, 4, False],
           [1000000000, 0, 0, True]]

  for case in cases:

    num, i, temp_val, gt = case[0], case[1], case[2], case[3]
    result = is_larger(num, i, temp_val)

    if result != gt:

      print("Problem. Num: ", num, " i: ", i , " temp_val: ", temp_val, " gt: ", gt)
      fail = True

  if fail:
    return 0
  else:
    print("Success: test_is_larger")
    return 5


# 15 pts
def test_two_digits_sum():
  fail = False

  cases = [[43456, 0, 1, 7],
           [43456, 1, 0, 7],
           [12345, 1, 2, 5],
           [11, 0, 1, 2],
           [459, 2, 0, 13],
           [424, 1, 2, 6],
           [1000000000, 3, 4, 0]]

  for case in cases:

    num, idx_1, idx_2, gt = case[0], case[1], case[2], case[3]
    value = two_digits_sum(num, idx_1, idx_2)

    if value != gt:
      fail = True
      print("Problem. Num: ", num, " idx_1: ", idx_1 , " idx_2: ", idx_2, " gt: ", gt)

  if fail:
    return 0
  else:
    print("Success: test_two_digits_sum")
    return 5

def test_two_digits_mean():
  fail = False

  cases = [[43456, 0, 1, 3.5],
           [43456, 1, 0, 3.5],
           [12345, 1, 2, 2.5],
           [11, 0, 1, 1],
           [459, 2, 0, 6.5],
           [424, 1, 2, 3],
           [1000000000, 3, 4, 0]]

  for case in cases:

    num, idx_1, idx_2, gt = case[0], case[1], case[2], case[3]
    value = two_digits_mean(num, idx_1, idx_2)

    if (value - gt) > 0.1:
      fail = True
      print("Problem. Num: ", num, " idx_1: ", idx_1, " idx_2: ", idx_2, " gt: ", gt)

  if fail:
    return 0
  else:
    print("Success: test_two_digits_mean")
    return 5


def test_two_digits_diff():
  fail = False

  cases = [[43456, 0, 1, 1],
           [43456, 1, 0, -1],
           [12345, 1, 2, -1],
           [11, 0, 1, 0],
           [459, 2, 0, 5],
           [424, 1, 2, -2],
           [1000000000, 3, 4, 0]]

  for case in cases:

    num, idx_1, idx_2, gt = case[0], case[1], case[2], case[3]
    value = two_digits_diff(num, idx_1, idx_2)

    if (value - gt) > 0.1:
      fail = True
      print("Problem. Num: ", num, " idx_1: ", idx_1, " idx_2: ", idx_2, " gt: ", gt)

  if fail:
    return 0
  else:
    print("Success: test_two_digits_diff")
    return 5
