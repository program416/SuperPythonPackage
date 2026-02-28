import time
def slow_print(string, option=list(), delay=0.03, end_delay=0.3):
    if option:
        for arg in option:
            match arg:
                case '-v'|'--vertical':
                    for i in string:
                        print(i)
                        time.sleep(delay)
                    time.sleep(end_delay)
                case _:
                    for i in string:
                        print(i, end='')
                        time.sleep(delay)
                    time.sleep(end_delay)
    else:
        for i in string:
            print(i, end='')
            time.sleep(delay)
        time.sleep(end_delay)


slow_print('126ㅅ려ㅑㅓ24ㅜ5ㅓ소혀랴대ㅏㄱ서ㅗㅎ', option=['--vertical'])