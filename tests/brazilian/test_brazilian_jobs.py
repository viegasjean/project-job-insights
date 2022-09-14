from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"

    translated_jobs = read_brazilian_file(path)

    assert type(translated_jobs) == list

    for job in translated_jobs:
        assert "title" in job
        assert "salary" in job
        assert "type" in job
