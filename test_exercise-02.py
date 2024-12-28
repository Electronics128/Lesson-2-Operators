import subprocess

def test_lesson_02():
    result = subprocess.run(['python3', 'lesson_02.py'], capture_output=True, text=True)
    output = result.stdout.strip().splitlines()

    assert output[0].startswith("Exercise 1:"), f"Failed TODO 1: {output[0]}"
    assert "True" in output[1], f"Failed TODO 2: {output[1]}"
    assert "False" in output[2], f"Failed TODO 3: {output[2]}"
    assert "Binary" in output[3], f"Failed TODO 4: {output[3]}"
    assert "Condition" in output[4], f"Failed TODO 5: {output[4]}"
    assert output[5].startswith("Num"), f"Failed TODO 6: {output[5]}"
    assert "Membership" in output[6], f"Failed TODO 7: {output[6]}"
    assert "Mod sum" in output[7], f"Failed TODO 8: {output[7]}"
    assert "Income" in output[8], f"Failed TODO 9: {output[8]}"
    assert "Debugging" in output[9], f"Failed TODO 10: {output[9]}"

    print("Lesson 2: All tests passed!")

if __name__ == "__main__":
    test_lesson_02()
