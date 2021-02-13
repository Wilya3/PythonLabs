class UIFactory:

    def createUI(self, language):
        language = language.lower()
        if language == "russian":
            return RussianUI()
        elif language == "english":
            return EnglishUI()


class UI(object):
    """
    ABSTRACT CLASS.
    Each method returns string with question, warning, etc.
    """

    def table(self):
        pass

    def file(self):
        pass

    def action(self):
        pass

    def initialization(self):
        pass

    def column(self):
        pass

    def values(self):
        pass

    def newValue(self):
        pass

    def changeWarning(self):
        pass

    def changeCondition(self):
        pass

    def deleteCondition(self):
        pass

    def deleteWarning(self):
        pass

    def loadWarning(self):
        pass

    def wrongCommand(self):
        pass

    def cancel(self):
        pass

    def pressAnyButton(self):
        pass


class RussianUI(UI):
    def table(self):
        return "С какой таблицей производится действие? (Menu/Content/Author)"

    def file(self):
        return "Введите название файла (без расширения) с таблицей "

    def action(self):
        return "Введите название файла с таблицей (Без расширения)"

    def initialization(self):
        return "Инициализация закончена. Работа с таблицами разрешена"

    def column(self):
        return "Введите название столбца"

    def values(self):
        return "Введите данные для каждого столбца через пробел"

    def newValue(self):
        return "Введите новое значение"

    def changeWarning(self):
        return "Внимание! Связанные данные из дочерних таблиц будут изменены!"

    def changeCondition(self):
        return "Введите условие WHERE (email = 'pochta')." \
               "\nИли не вводите ничего для изменения всех строк."

    def deleteCondition(self):
        return "Введите условие WHERE (email = 'pochta'). " \
               "\nИли не вводите ничего для удаления всех строк."

    def deleteWarning(self):
        return "Внимание! Связанные данные из дочерних таблиц будут удалены!"

    def loadWarning(self):
        return "Вы уверены? Все данные в БД будут перезаписаны данными из файла!" \
               "\nВнимание! Связанные данные из дочерних таблиц будут удалены!"

    def wrongCommand(self):
        return "Неверная команда! Повторите ввод"

    def cancel(self):
        return "Отмена..."

    def pressAnyButton(self):
        return "Для продолжения нажмите на любую кнопку..."


class EnglishUI(UI):
    pass