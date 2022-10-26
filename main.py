from application.salary import calculate_salary
from application.db.people import get_employees
from pick import pick
if __name__ == "__main__":
    menu = {
    'Рассчитать зарплату': calculate_salary,
    'Получить список работников': get_employees}
    choice, index = pick(list(menu), 'Выберите действие', indicator='=>')
    menu[choice]()
