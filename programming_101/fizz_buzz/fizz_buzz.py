def fizz_buzz(number):
    result = []
    for index in range(number):
        count = index + 1
        str_result = str(count)

        if count % 15 == 0 and count % 5 == 0 and count % 3 == 0:
            str_result = 'fizzbuzz'
        elif count % 3 == 0:
            str_result = 'fizz'
        elif count % 5 == 0:
            str_result = 'buzz'


        result.append(str_result)
    return result
