def remove_duplicates(some_list):
    return list(set(some_list))


def run():
    random_list = [1,1,2,2,4]
    print(remove_duplicates(random_list))


if __name__ == '__main__':
    run()