from typing import Collection


class Person:

    # Types of parameters can be defined with ': type' afterwards but this will only
    # take effect in your IDE. The program itself will also take other values.
    def __init__(self, surname: str, name: str) -> None:
        # you can't access these fields directly by any child class
        # so we need to use the get-methods
        self.__name = name
        self.__surname = surname

    # You can leave a hint to the return type as well
    def get_name(self) -> str:
        """
        Gets the name.
        :return: the name
        """
        return self.__name

    def get_surname(self) -> str:
        """
        Gets the surname.
        :return: the surname
        """
        return self.__surname


class Trainer(Person):

    # default value for amount_trainees is set to 1
    # if you have a Trainer with one trainee you can skip the amount_trainees values
    def __init__(self, surname: str, name: str, amount_trainees: int = 1) -> None:
        super().__init__(surname, name)
        self.__amount_trainees = amount_trainees

    def get_amount_trainees(self) -> int:
        """
        Gets the amount of trainees.
        :return: the amount of trainees
        """
        return self.__amount_trainees


class Training:

    def __init__(self, location: str, trainer: Trainer, participants: Collection[Trainer]) -> None:
        # These fields can be used by child-classes because there is only one underscore
        self._location = location
        self._trainer = trainer
        self._participants = participants

    # Demo a static method
    @staticmethod
    def build_name_of_trainer(trainer: Trainer) -> str:
        """
        Builds the name of a given trainer to a pretty formatted string.
        :param trainer: the trainer to build the name string from
        :return: the pretty formatted name string
        """
        return trainer.get_name() + ' ' + trainer.get_surname()


class TrainingForTrainers(Training):

    def __init__(self, trainer: Trainer, participants: Collection[Trainer], topic: str) -> None:
        # using super constructor with pre-defined value
        super().__init__('TBH1', trainer, participants)
        self.__topic = topic

    # this method is not visible to the one which is using this class
    def _count_amount_of_participants(self) -> int:
        """
        Count the amount of participants.
        :return: the amount of participants
        """
        return len(self._participants)

    def _sum_amount_of_effected_trainees(self) -> int:
        """
        Calculates the sum of effected trainees.
        :return: the sum of effected trainees
        """
        return sum([participant.get_amount_trainees() for participant in self._participants]) + self._trainer.get_amount_trainees()

    def get_information(self) -> str:
        """
        Builds the information as a pretty formatted string.
        :return: the pretty formatted string
        """
        information = '''
Topic: "%s"
Where: %s
Trainer: %s
Amount of participants: %d
Amount of effected trainees: %d
        ''' % (
            self.__topic,
            self._location,
            Training.build_name_of_trainer(self._trainer),
            self._count_amount_of_participants(),
            self._sum_amount_of_effected_trainees()
        )
        return information


def main():
    trainer = Trainer('Schmidt', 'Peter', 3)
    participants = [
        Trainer('Schäfer', 'Lisa', 2),
        Trainer('Reus', 'Marco', 6),
        Trainer('Witsel', 'Axel'),
    ]

    event = TrainingForTrainers(trainer, participants, 'Python Crashkurs')

    print(event.get_information())


if __name__ == '__main__':
    main()
