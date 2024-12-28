import lesson_02

def test_arithmetic_operators():
    assert lesson_02.a == 10, "Variable 'a' should be 10."
    assert lesson_02.b == 3, "Variable 'b' should be 3."
    assert lesson_02.addition == 13, "Addition result is incorrect."
    assert lesson_02.subtraction == 7, "Subtraction result is incorrect."
    assert lesson_02.multiplication == 30, "Multiplication result is incorrect."
    assert lesson_02.division == 10 / 3, "Division result is incorrect."
    assert lesson_02.modulus == 10 % 3, "Modulus result is incorrect."
    assert lesson_02.exponentiation == 10**3, "Exponentiation result is incorrect."

def test_comparison_operators():
    assert lesson_02.greater_than == True, "Comparison 'a > b' is incorrect."
    assert lesson_02.less_than == False, "Comparison 'a < b' is incorrect."
    assert lesson_02.greater_or_equal == True, "Comparison 'a >= b' is incorrect."
    assert lesson_02.less_or_equal == False, "Comparison 'a <= b' is incorrect."
    assert lesson_02.equal == False, "Comparison 'a == b' is incorrect."
    assert lesson_02.not_equal == True, "Comparison 'a != b' is incorrect."

def test_logical_operators():
    assert lesson_02.x is True, "Variable 'x' should be True."
    assert lesson_02.y is False, "Variable 'y' should be False."
    assert lesson_02.and_result == False, "'x and y' result is incorrect."
    assert lesson_02.or_result == True, "'x or y' result is incorrect."
    assert lesson_02.not_x == False, "'not x' result is incorrect."

def test_bitwise_operators():
    assert lesson_02.bitwise_and == 10 & 3, "Bitwise AND result is incorrect."
    assert lesson_02.bitwise_or == 10 | 3, "Bitwise OR result is incorrect."
    assert lesson_02.bitwise_xor == 10 ^ 3, "Bitwise XOR result is incorrect."
    assert lesson_02.left_shift == 10 << 1, "Left shift result is incorrect."
    assert lesson_02.right_shift == 10 >> 1, "Right shift result is incorrect."

def test_operator_precedence():
    expected = (10 + 3) > 10 and True
    assert lesson_02.precedence_result == expected, "Operator precedence result is incorrect."

def test_augmented_assignment():
    assert lesson_02.num_after_add == 10, "Result after 'num += 5' is incorrect."
    assert lesson_02.num_after_subtract == 5, "Result after 'num -= 5' is incorrect."
    assert lesson_02.num_after_multiply == 25, "Result after 'num *= 5' is incorrect."
    assert lesson_02.num_after_divide == 5, "Result after 'num /= 5' is incorrect."
    assert lesson_02.num_after_exponentiate == 25, "Result after 'num **= 2' is incorrect."

def test_special_operators():
    assert lesson_02.list1 is lesson_02.list2, "'list1 is list2' should be True."
    assert lesson_02.list1 == [1, 2, 3], "'list1' should contain [1, 2, 3]."
    assert lesson_02.membership_in == True, "'1 in list1' should be True."
    assert lesson_02.membership_not_in == False, "'4 not in list1' should be False."

def test_custom_operator_examples():
    result = lesson_02.mod_sum(10, 3)
    assert result == (10 + 3) % 3, "Custom function 'mod_sum' result is incorrect."
    result = lesson_02.mod_sum(15, 4)
    assert result == (15 + 4) % 4, "Custom function 'mod_sum' result for (15, 4) is incorrect."

def test_real_world_example():
    assert lesson_02.total_income == 7000, "Total income calculation is incorrect."

def test_debugging_with_operators():
    assert lesson_02.fixed_expression == True, "The debugging expression result is incorrect."
