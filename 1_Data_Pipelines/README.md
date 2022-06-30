## Section 1: Data Pipelines

For this section, I used Apache Airflow as my scheduling solution to implement the scheduling component of my solution for this section. Essentially, my solution included two Python scripts: `main-dag.py` and `main.py` to process the two data files: `dataset1.csv` and `dataset2.csv`. A data job run has been scheduled and these data files will be processed at 1am daily. The output of these processing tasks are two csv files: `dataset1_output.csv` and `dataset2_output.csv`.

The two Python scripts: `main-dag.py` and `main.py` help to carry out the following processing tasks:
- Split the `name` field into `first_name` and `last_name`.
- Remove any zeros prepended to the `price` field.
- Delete any rows which do not have a `name`.
- Create a new field named `above_100` which is `true` if the price is strictly greater than 100.

For the scheduling component of my solution with Apache Airflow, I ran into an error which did not allow my data job run to be carried out successfully.
Nevertheless, my Python scripts worked well in my local environment and were able to output the two csv files: `dataset1_output.csv` and `dataset2_output.csv`.
I have attached screenshots of the log for my data job run in Apache Airflow. They are two jpg files: `Airflow1.jpg` and `Airflow2.jpg`.
