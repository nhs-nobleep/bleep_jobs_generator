import numpy as np
import datetime as dt
from numpy.random import choice

from utils.time_functions import random_date_in_shift, random_date_after_a_point
from utils import shifts


class JobForStats(object):

    def __init__(self):
        """
        Ideal case of level of information that can be reached when the job is done.
        """
        # id job
        self.urgency = 0
        self.id_job = 0
        # Time
        self.delivery_time = dt.date
        self.check_time = None  # if None the job has to be checked
        self.done_time = None  # if None the job has to be performed

    def export_as_dict(self):
        d = {'delivery_time': self.delivery_time,
             'check_time': self.check_time,
             'done_time': self.done_time,
             'urgency': self.urgency,
             'id_job': self.id_job
             }
        return d

    def __is_checked__(self):
        if self.check_time is None:
            return False
        else:
            return True

    def __is_done__(self):
        if self.done_time is None:
            return False
        else:
            return True

    checked = property(__is_checked__)
    done = property(__is_done__)

    @staticmethod
    def parser_job_from_app(job_from_app):
        # TODO: parse the value from the server to obj JobForStats()
        jb = JobForStats()
        return jb


class DocForStats(object):

    def __init__(self):
        # Id doc
        self.doctor_id = ''
        self.team_name = ''

        self.job_list = []

        # doctor workload
        self.length_list_jobs_when_delivery = [0, 0, 0]  # Number of [high, medium, low] priority jobs.
        self.length_list_jobs_when_check = [0, 0, 0]
        self.length_list_jobs_when_done = [0, 0, 0]

    def export_as_dict(self):
        d = {'length_list_jobs_when_delivery': self.length_list_jobs_when_delivery,
             'length_list_jobs_when_check': self.length_list_jobs_when_check,
             'length_list_jobs_when_done': self.length_list_jobs_when_done,
             'doctor_id': self.doctor_id,
             'team_name': self.team_name,
             }
        return d

    def __is_busy__(self):
        busy = False
        for jb in self.job_list:
            if jb.check_time is True and jb.done_time is False:
                busy = True
                break
        return busy

    busy = property(__is_busy__)


def random_generator_job_for_stats(doctor_id='John Dorian',
                                   team_name='Intensive Care',
                                   urgency_distribution=(1/3, 1/3, 1/3),  # Python3 - [high, medium, low]
                                   percentage_check=0.9,
                                   percentage_done=0.9,
                                   shift=shifts.shift_2,
                                   mu_check=10,
                                   sigma_check=2,
                                   mu_done=15,
                                   sigma_done=2):
    jb = JobForStats()
    jb.doctor_id, jb.team_name = doctor_id, team_name
    jb.urgency = choice([3, 2, 1], 1, urgency_distribution)

    jb.delivery_time = random_date_in_shift(shift)

    is_checked = choice(['checked', 'not checked yet'], 1, [percentage_check, 1 - percentage_check])
    if is_checked == 'checked':
        jb.check_time = random_date_after_a_point(jb.delivery_time, mu_check, sigma_check)

        is_done = choice(['done', 'not done yet'], 1, [percentage_done, 1 - percentage_done])
        if is_done == 'done':
            jb.done_time = random_date_after_a_point(jb.delivery_time, mu_done, sigma_done) ###
        else:
            jb.done_time = None
    else:
        jb.check_time = None

    return jb


def random_generator_doctor():
    pass
