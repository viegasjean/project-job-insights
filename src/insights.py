from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    unique_job_types = []
    for job in jobs:
        job_type = job["job_type"]
        if job_type not in unique_job_types:
            unique_job_types.append(job_type)
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    jobs = read(path)
    unique_industries = []
    for job in jobs:
        industry = job["industry"]
        if industry not in unique_industries and industry != "":
            unique_industries.append(industry)
    return unique_industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if industry == job["industry"]]


def get_max_salary(path):
    jobs = read(path)
    return max(
        [
            int(job["max_salary"])
            for job in jobs
            if job["max_salary"].isnumeric()
        ]
    )


def get_min_salary(path):
    jobs = read(path)
    return min(
        [int(job["min_salary"]) for job in jobs if job["min_salary"].isdigit()]
    )


def matches_salary_range(job: dict, salary: int):
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        if max_salary > min_salary:
            return max_salary >= salary >= min_salary
        else:
            raise ValueError("max_salary must be greater than min_salary")
    except KeyError:
        raise ValueError("max_salary and min_salary must be informed")
    except TypeError:
        raise ValueError("max_salary and min_salary must be int")


def filter_by_salary_range(jobs: list, salary: int):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """

    return [
        job for job in jobs
        if type(salary) == int
        and type(job["max_salary"]) == int
        and type(job["min_salary"]) == int
        and job["max_salary"] > job["min_salary"]
        and matches_salary_range(job, salary)
    ]
