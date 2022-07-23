import datetime


def paramsdecorator(put):
    def logs(funtion_):
        def logs_(*args, **kwargs):
            data_time = str(datetime.datetime.now())
            name_funtion = funtion_.__name__
            arguments_args = str(args)
            arguments_kwargs = str(kwargs)
            result = str(funtion_(*args, **kwargs))
            vernul = f'Функция вернула {result}'
            with open(put, 'a', encoding="utf-8") as logsfile:
                logsfile.write(f'\nДата и время: {data_time}\n')
                logsfile.write(f'Функция: {name_funtion}\n')
                logsfile.write(f'Аргументы: {arguments_args}, {arguments_kwargs}\n')
                logsfile.write(vernul + '\n')
                logsfile.write('*' * 20)
            return result
        return logs_
    return logs


@paramsdecorator('logs/logfiles.log')
def onefunction(first, b=5):
    return first + b


@paramsdecorator('logs/logfiles.log')
def twofunction():
    print('Функция отработала')


if __name__ == '__main__':
    s = onefunction(1, 4)

    d = twofunction()
