import time


def get_message():
    return "DevOps app is running"


def run():
    while True:
        print(get_message(), flush=True)
        time.sleep(5)


if __name__ == "__main__":
    run()
