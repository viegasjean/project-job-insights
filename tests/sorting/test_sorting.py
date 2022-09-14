import pytest
from src.sorting import sort_by


@pytest.fixture
def mock_jobs():
    return [
        {
            "job_title": "Marketing",
            "min_salary": "3000",
            "max_salary": "4000",
            "date_posted": "2020-05-08",
        },
        {
            "job_title": "Registered Nurse",
            "min_salary": "4000",
            "max_salary": "5000",
            "date_posted": "2020-04-25",
        },
        {
            "job_title": "Dental Hygienist",
            "min_salary": "5000",
            "max_salary": "6000",
            "date_posted": "2020-05-02",
        },
    ]


@pytest.fixture
def sorted_by_min_salary():
    return [
        {
            "job_title": "Marketing",
            "min_salary": "3000",
            "max_salary": "4000",
            "date_posted": "2020-05-08",
        },
        {
            "job_title": "Registered Nurse",
            "min_salary": "4000",
            "max_salary": "5000",
            "date_posted": "2020-04-25",
        },
        {
            "job_title": "Dental Hygienist",
            "min_salary": "5000",
            "max_salary": "6000",
            "date_posted": "2020-05-02",
        },
    ]


@pytest.fixture
def sorted_by_max_salary():
    return [
        {
            "job_title": "Dental Hygienist",
            "min_salary": "5000",
            "max_salary": "6000",
            "date_posted": "2020-05-02",
        },
        {
            "job_title": "Registered Nurse",
            "min_salary": "4000",
            "max_salary": "5000",
            "date_posted": "2020-04-25",
        },
        {
            "job_title": "Marketing",
            "min_salary": "3000",
            "max_salary": "4000",
            "date_posted": "2020-05-08",
        },
    ]


@pytest.fixture
def sorted_by_date():
    return [
        {
            "job_title": "Marketing",
            "min_salary": "3000",
            "max_salary": "4000",
            "date_posted": "2020-05-08",
        },
        {
            "job_title": "Dental Hygienist",
            "min_salary": "5000",
            "max_salary": "6000",
            "date_posted": "2020-05-02",
        },
        {
            "job_title": "Registered Nurse",
            "min_salary": "4000",
            "max_salary": "5000",
            "date_posted": "2020-04-25",
        },
    ]


def test_sort_by_criteria(
    mock_jobs, sorted_by_min_salary, sorted_by_max_salary, sorted_by_date
):
    """
    Test sorting by criteria.
    """

    # sort_by(mock_jobs, "min_salary")

    # assert mock_jobs == sorted_by_min_salary

    sort_by(mock_jobs, "max_salary")

    assert mock_jobs == sorted_by_max_salary

    sort_by(mock_jobs, "min_salary")

    assert mock_jobs == sorted_by_min_salary

    sort_by(mock_jobs, "date_posted")

    assert mock_jobs == sorted_by_date
