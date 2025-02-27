#get_hour(epoch_seconds)

from value_return import get_hour, get_minutes, get_seconds

def main():
    epoch_second = int(input('Enter seconds'))
    hours = get_hour(epoch_second)
    minutes = get_minutes(epoch_second)
    seconds = get_seconds(epoch_second)

    print(f'{hours:02d} : {minutes:02d} : {seconds:02d}')
main()