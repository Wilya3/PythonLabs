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

    def connectionError(self):
        pass

    def fileNotFoundError(self):
        pass

    def queryError(self):
        pass

    def badFileError(self):
        pass


class RussianUI(UI):
    def table(self):
        return "С какой таблицей производится действие? (Menu/Content/Author)"

    def file(self):
        return "Введите название файла (Без расширения) с таблицей "

    def action(self):
        return "Какое действие необходимо выполнить?"

    def initialization(self):
        return "Инициализация закончена. Работа с таблицами разрешена"

    def column(self):
        return "Введите название столбца"

    def values(self):
        return "Введите данные для каждого столбца"

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

    def connectionError(self):
        return "Ошибка соединения с базой данных!\nПрограмма завершает свое выполнение..."

    def fileNotFoundError(self):
        return "Ошибка! Таблица с таким именем не найдена. Действие отменяется..."

    def queryError(self):
        return "Ошибка добавления данных в базу данных!" \
               "\nВозможные проблемы:" \
               "\n-Данные повреждены или не соответствуют типам столбцов" \
               "\n-Повторяются значения первичного ключа" \
               "\n-Неправильный ввод условия WHERE" \
               "\n-Неправильно указан столбец (команда change)"

    def badFileError(self):
        return "Ошибка! Файл поврежден или содержит некорректные данные!"


class EnglishUI(UI):
    pass
