def get_customer_group(customer_id_str: str) -> int:
    """
    Алгоритм группировки клиента
    """
    customer_group = sum(list(map(int, customer_id_str.strip())))
    return customer_group


def customer_counter_choose_start_id(n_customers: int, n_first_id: int) -> dict:
    """
    Функция, которая подсчитывает число покупателей, попадающих в каждую группу.
    ID начинается с произвольного числа.
    """
    number_of_customers = {}
    if (n_customers <= 10000000) and (n_first_id <= 10000000) and ((n_customers + n_first_id) <= 10000000):
        for customer in range(0, n_customers):
            customer_id_str = str(customer + n_first_id).zfill(7)
            customer_group = get_customer_group(customer_id_str)
            number_of_customers[customer_group] = number_of_customers.get(customer_group, 0) + 1
    else:
        raise Exception('Такая комбинация числа покупателей и начального ID недопустима!')
    number_of_customers = {k: number_of_customers[k] for k in sorted(number_of_customers)}
    return number_of_customers


def customer_counter_continuous_numbering(n_customers: int) -> dict:
    """
    Функция, которая подсчитывает число покупателей, попадающих в каждую группу.
    Нумерация ID сквозная и начинается с 0.
    """
    return customer_counter_choose_start_id(n_customers, n_first_id=0)
