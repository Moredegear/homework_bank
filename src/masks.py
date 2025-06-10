from typing import Union
import logging


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs.log')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: Union[str, int]) -> Union[str]:
    """маскируем номер карты пользователя"""
    logger.info("принимам номер карты и переводим его в вид строки")
    number_card = str(number_card)
    logger.info("проверяем количество символов")
    if len(number_card) == 0:
        logger.critical("Номер карты не введен")
        return "Номер карты не введен"
    if len(number_card) < 16:
        logger.critical("Введено недостаточно символов")
        return "Вы ввели недостаточно символов"
    elif len(number_card) > 16:
        logger.critical("Введено слишком много символов")
        return "Вы ввели слишком много символов"
    logger.info("маскируем номер карты")
    mask_card_number_list = []
    for i in range(len(number_card)):
        if i < 6 or i > 11:
            if i == 4 or i == 12:
                mask_card_number_list.append(" ")
            mask_card_number_list.append(number_card[i])
        else:
            if i == 8:
                mask_card_number_list.append(" ")
            mask_card_number_list.append("*")
    mask_card_number = "".join(mask_card_number_list)
    logger.debug("возвращаем получившийся результат")
    return mask_card_number


def get_mask_account(number_account: Union[str, int]) -> Union[str]:
    """Маскируем номер счета пользователя"""

    logger.info("принимам номер карты и переводим его в вид строки")
    number_account = str(number_account)
    logger.info("проверяем количество символов")
    if len(number_account) == 0:
        logger.critical("Номер счета не введен")
        return "Номер счета не введен"
    if len(number_account) < 20:
        logger.critical("Введено недостаточно символов")
        return "Вы ввели недостаточно символов"
    elif len(number_account) > 20:
        logger.critical("Введено слишком много символов")
        return "Вы ввели слишком много символов"
    logger.info("маскируем номер карты")
    mask_account_list = []
    for i in range(len(number_account)):
        if i > len(number_account) - 5:
            mask_account_list.append(number_account[i])
        elif i > len(number_account) - 7:
            mask_account_list.append("*")
        else:
            continue
    mask_account = "".join(mask_account_list)
    logger.debug("возвращаем получившийся результат")
    return mask_account
