"""
Написать функцию, которая принимает как аргумент алфавит последовательности,
а возвращает функцию получения статистики встречаемости символов в последовательности
"""


def create_function_symbol_stats(alphabet: str):
    """
    Создает функцию для подсчета статистики символов в последовательности по заданному алфавиту.

    :param alphabet: алфавит, заданный в виде строки без пробельных символов (регистр учитывается)
    :return: функция для подсчета статистики символов в заданной последовательности
    """
    alphabet = set(alphabet)

    def calculate_symbol_stats(sequence: str) -> None:
        """
        Подсчитывает процентное содержание каждого символа в заданной последовательности.

        :param sequence: последовательность для подсчета символов в ней
        :return: печатает на экран результат статистической обработки
        """
        stats = {key: 0 for key in sorted(alphabet)}  # сортировка множества -- плохо
        symbols = set(sequence)

        if not (symbols <= alphabet):
            raise Exception("Sequence's symbols not in alphabet")

        print(f'Symbol percent statistic for {sequence[:3]}...:')
        for symbol in sorted(symbols):
            stats[symbol] = sequence.count(symbol)
        for symbol, stat in stats.items():
            print(f'{symbol}: {stat / len(sequence):.2%}')  # прогнать на огромной последовательности
        print()
    return calculate_symbol_stats


count_nucleotides_DNA = create_function_symbol_stats('ATGCatgc')
count_nucleotides_DNA('aaaaaattggccatATGAGCTACGATCGACTaaatttggacatttatg')
# count_nucleotides_DNA('yaATTggC')  # Error
