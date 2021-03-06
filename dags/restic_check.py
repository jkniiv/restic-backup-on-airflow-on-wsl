# -*- coding: utf-8 -*-
#

from builtins import range
from datetime import datetime, timedelta

import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator

def msys2_bash_invocation(command, msys2_bash='/c/scoop/apps/msys2/current/usr/bin/bash.exe'):
    return '{0} -l -c "{1}"'.format(msys2_bash, command)

args = {
    'owner': 'restic',
    'depends_on_past': False,
    #'start_date': airflow.utils.dates.days_ago(2),
    'start_date': datetime(2020,2,29),
    'retries': 0,
}

dag = DAG(
    dag_id='restic_check',
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=60),
    catchup=False,
    default_args=args,
)

run_this_last = DummyOperator(
    task_id='run_END',
    dag=dag,
)

run_restic_check = BashOperator(
    task_id='run_restic_check',
    bash_command=msys2_bash_invocation("restic-do-check"),
    dag=dag,
)

run_restic_check >> run_this_last

if __name__ == "__main__":
    dag.cli()
