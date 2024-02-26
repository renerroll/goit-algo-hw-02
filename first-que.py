from queue import Queue
import time

queue = Queue()


def generate_request(request):
    queue.put(request)  # normalize output


def process_request():
    if not queue.empty():
        item = queue.get()
        print(f"В процесі {item}")
        time.sleep(1)
        print(f"Завершено {item}")
        time.sleep(1)
        queue.task_done()
    else:
        print("Пустотіла черга")


if __name__ == "__main__":
    try:
        tasks_num = int(input("Введи кількість завдань для обробки: "))
        counter = 0

        while counter < tasks_num:
            counter += 1
            generate_request(counter)
            process_request()

    except KeyboardInterrupt as err:
        print(err)
    except ValueError as err:
        print(err)