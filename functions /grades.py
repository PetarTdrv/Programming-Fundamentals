def grade_info(result):
    if 2.00 <= result <= 2.99:
        return "Fail"
    elif 3.00 <= result <= 3.49:
        return "Poor"
    elif 3.50 <= result <= 4.49:
        return "Good"
    elif 4.50 <= result <= 5.49:
        return "Very Good"
    elif 5.50 <= result <= 6.00:
        return "Excellent"


grade_as_digits = float(input())
res = grade_info(grade_as_digits)
print(res)
