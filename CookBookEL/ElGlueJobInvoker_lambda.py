import boto3
client = boto3.client('glue')

try:
    import LambdaUtil as lh
except Exception as mnfe:
    import CookBookEL.LambdaUtil as lh




class ElGlueInvoker_Handler(lh.LambdaHandlerBase):
    """Echo handler."""

    def __init__(self):
        lh.LambdaHandlerBase.__init__(self,
                                   lambda_name='glue_invoker_handler')

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

        run_time = self.SimulateWorkDuration(p_min_seconds=1, p_max_seconds=5)
        self.Logger.info('## Seconds to start glue job:', run_time=run_time)

        response = {'JobRunId': 'AA987654321'}

        # # END DUMMY-RETURN


        self.Logger.info('## GLUE JOB RUN ID: ' + response['JobRunId'])


        self.EventReturn['response'] = response

        self.Logger.info("### ENDED LAMBDA...",
                         lambda_name='glue_invoker_handler')


glue_invoker_handler = ElGlueInvoker_Handler()