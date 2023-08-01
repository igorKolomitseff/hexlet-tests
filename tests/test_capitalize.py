from capitalize import capitalize


if capitalize('hello') != 'Hello':
    raise Exception('The function is not working correctly!')

if capitalize('') != '':
    raise Exception('The function is not working correctly!')


print('All tests are passed!')