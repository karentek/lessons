SEPARATOR = '------------------------------------------'
#i am training mace commit
# user profile
name = ''
age = 0
phone = ''
email = ''
info = ''
# busines links
post_code = ''
adress = ''
ogrn = 0
inn = 0
banc_name = ''
corr_account = 0
bic_code = 0
payment_account = 0


def main_menu(separator):
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')


def sub_menu(separator):
    print(SEPARATOR)
    print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
    print('1 - Общая информация')
    print('2 - Информация о предпринимателе')
    print('0 - Назад')


def sub_menu2(separator):
    print(SEPARATOR)
    print('ВЫВЕСТИ ИНФОРМАЦИЮ')
    print('1 - Общая информация')
    print('2 - Вся информация')
    print('0 - Назад')


def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, info_parameter, post_code,
                      adress):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс: ', post_code)
    print('Почтовый адрес: ', adress)

    if info:
        print('')
        print('Дополнительная информация:')
        print(info_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    main_menu(SEPARATOR)
    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break
    if option == 1:
        # submenu 1: edit info
        while True:
            sub_menu(SEPARATOR)
            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')
                uphone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for ch in uphone:
                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch
                email = input('Введите адрес электронной почты: ')

                postcode = input('Введите индекс: ')
                for ch in postcode:
                    if ('0' <= ch <= '9'):
                        post_code += ch
                adress = input('Введите адрес: ')
                info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input busines links
                while True:
                    ogrn = int(input('Введите ОГРН: '))
                    i_ogrn = ogrn
                    count = 0
                    while i_ogrn != 0:
                        i_ogrn //= 10
                        count += 1
                    if count == 15:
                        break
                    else:
                        print('ОГРНИП должен содержать 15 цифр')
                        i_ogrn = ogrn
                        count = 0

                inn = int(input('Введите ИНН: '))
                while True:

                    payment_account = int(input('Введите Расчетный счет: '))
                    i_p_a = payment_account
                    count = 0
                    while i_p_a != 0:
                        i_p_a //= 10
                        count += 1
                    if count == 20:
                        break
                    else:
                        print('Расчетный счет должен содержать 20 цифр')
                        i_p_a = payment_account
                        count = 0

                banc_name = input('Введите наименование банка: ')
                bic_code = int(input('Введите БИК банка: '))
                corr_account = int(input('Введите корреспондентский счет: '))
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            sub_menu2(SEPARATOR)

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, email, info, post_code, adress)

            elif option2 == 2:
                general_info_user(name, age, phone, email, info, post_code, adress)

                # print busines links
                print('')
                print('Информация о предпринимателе')
                print('ОГРН:', ogrn)
                print('ИНН: ', inn)
                print('Расчетный счет: ', payment_account)
                print('Введите наименование банка: ', banc_name)
                print('Введите БИК банка: ', bic_code)
                print('Введите корреспондентский счет: ', corr_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')