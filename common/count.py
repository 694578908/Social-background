from config.color import print_centered_ansi

test_case_counter = 0


def count(data):
    global test_case_counter
    separator = '>' * 20
    test_case_counter += 1  # 递增类级别的测试用例计数器
    print_centered_ansi(f"\n{separator}这是第{test_case_counter}条用例{separator}\n", '33')
    return data
