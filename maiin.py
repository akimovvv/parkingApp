import db, estimate
import datetime

def main():

    while True:
        print("Welcome to our parking!")
        action = input("Выберите действие: \n"
	"1. Получить талон \n"
	"2. Сдать талон \n"
    "3. Выйти \n")

        if action == "1":
            start_time = datetime.datetime.now()
            print("Ваш талон: \n"
                  f"Номер: {db.start(start_time)} \n"
                  f"Дата въезда: {start_time}")
        elif action == "2":
            ticket_id = int(input("Введите номер талона: \n"))
            if db.check_status(ticket_id) == 1:
                end_time = datetime.datetime.now()
                db.end(ticket_id, end_time)
                sum = estimate.sum(start = db.show_start(ticket_id), end = db.show_end(ticket_id))
                db.sum(ticket_id,sum)
                print(f"Дата въезда: {db.show_start(ticket_id)}\n"
                f"Дата выезда: {db.show_end(ticket_id)}\n"
                f"Сумма: {sum}")
            elif db.check_status(ticket_id) == 2:
                print(f"Данный талон был использован {db.show_all(ticket_id)}!")
        elif action == "3":
            db.close()
            break
        else:
            print("Error!")
main()