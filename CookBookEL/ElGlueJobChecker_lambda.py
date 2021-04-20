import boto3

client = boto3.client('glue')

try:
    import LambdaUtil as lh
except Exception as mnfe:
    import CookBookEL.LambdaUtil as lh


class ElGlueChecker_Handler(lh.LambdaHandlerBase):
    """Echo handler."""

    def __init__(self):
        lh.LambdaHandlerBase.__init__(self,
                                   lambda_name='ElGlueJobChecker_lambda')

    def DoWork(self, request, **kwargs):
        self.Logger.info("### STARTED_LAMBDA...",
                         row_count=self.request.event['row_count'])

        self.Logger.info("## STARTED GLUE JOB:",
                         glue_job_name=self.request.event['glue_job_name'])

        """
        ## STUB LAUNCH GLUE JOB !

        response = client.start_job_run(JobName = glueJobName)
        logger.info('## GLUE JOB RUN ID: ' + response['JobRunId'])

        """

        # # START DUMMY-RETURN

        run_time = self.SimulateWorkDuration(p_min_seconds=5, p_max_seconds=15)
        self.Logger.info('## Seconds to start glue job:', run_time=run_time)

        response = {'JobRunId': 'AA987654321'}

        self.Logger.info('## GLUE JOB RUN ID: ' + response['JobRunId'])

        glue_job_name = self.request.event['glue_job_name']
        glue_job_run_id = response['JobRunId']
        job_run_state = 'SUCCEEDED'

        self.EventReturn['glue_status'] = \
            {
                    "GlueJobName": glue_job_name,
                    "GlueJobRunId": glue_job_run_id,
                    "GlueJobRunState": job_run_state,
                    # #"GlueJobStartedOn": glue_resp['JobRun'].get('StartedOn', '').strftime('%x, %-I:%M %p %Z'),
                    # #"GlueJobCompletedOn": glue_resp['JobRun'].get('CompletedOn', '').strftime('%x, %-I:%M %p %Z'),
                    # #"GlueJobLastModifiedOn": glue_resp['JobRun'].get('LastModifiedOn', '').strftime('%x, %-I:%M %p %Z')
            }

        # # END DUMMY-RETURN

        self.Logger.info("### ENDED LAMBDA...",
                         lambda_name='glue_invoker_handler')


glue_checker_handler = ElGlueChecker_Handler()