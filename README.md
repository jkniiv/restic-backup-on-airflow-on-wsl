# restic-backup-on-airflow-on-wsl

These are some of the parts I use for a restic-based backup on my Windows 10 laptop. [Restic](https://github.com/restic/restic) is being 
scheduled via Apache Airflow DAGs (task groups) on Windows Subsystem for Linux (v1) and this concoction allows me to monitor the status of 
these jobs much easier (via the Airflow webapp) than a traditional solution based on 'cron' or Task Scheduler would. Some of the parts 
needed are Scoop (for the restic binary etc.) and Msys2 (in my case installed via Scoop; really for proper Windows-based Bash scripting)
while Apache Airflow itself is being run under WSL (in my case version 1) due to a native Windows support for Airflow being non-existent
for the moment.

All of this is mostly a venture of documenting for myself what I've accomplished. The basic idea of using Airflow for mere task scheduling
is nothing new but there are these certain hoops you have to run through to make this work on Windows.
