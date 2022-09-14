from src.counter import count_ocurrences


def test_counter():
    path = 'src/jobs.csv'
    word = 'Python '
    'Retorna um inteiro'
    assert type(count_ocurrences(path, word)) == int
    'Retorna a contagem 611'
    assert count_ocurrences(path, word) == 611
