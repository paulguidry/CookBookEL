import os
import sys
import json

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
if os.pardir not in sys.path:
    sys.path.append(os.pardir)
if os.path not in sys.path:
    sys.path.append(os.path)

from CookBookEL import ElGlueJobInvoker_lambda





if __name__ == '__main__':
    context: str = ""
    event: dict = {
                   "glue_job_name": "ce_run_table_etl",
                   #
                   "table_name": "tab_1",
                   "table_schema_name": "dbo",
                   "db_name": "database_name",
                   "db_port": "1433",
                   "db_instance": "hkkkkh",
                   "db_user": "pgadmin",
                   "db_password": "1#peanuts",
                   "db_max_retries": 2,
                   "row_count": 12000,
                   "column_list": ["col1","col2","col3","col4","col5"],
                   "column_pk_list": ["col1"],
                   "data_type_list": ["int","varchar","varchar","varchar","varchar"],
                   "con_time_out_sec": 60,
                   "log_level_str": "debug"}


    lamda_return = ElGlueJobInvoker_lambda.glue_invoker_handler(event, context)


    print(f" Returned json {json.dumps(lamda_return)}")