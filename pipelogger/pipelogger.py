import json
import logging
import time

from datetime import datetime
from google.cloud import bigquery
from google.cloud import storage


logging.basicConfig(level=logging.INFO)


class logsformatter:

    def __init__(self, pipeline_id, table_ids, project_id, bucket_name, folder_bucket):
        """
        Initialize the log formatter with the required information.

        Args:
            pipeline_id (str): Unique pipeline ID.
            table_ids (list): List of IDs of BigQuery tables.
            project_id (str): Google Cloud Project ID.
            bucket_name (str): Google Cloud Storage bucket where the logs will be stored.
            folder_bucket (str): Folder inside the bucket where the logs will be stored.
        """
        self.pipeline_id = pipeline_id
        self.table_ids = table_ids
        self.project_id = project_id
        self.bucket_name = bucket_name
        self.folder_bucket = folder_bucket

    def add_metadata_to_log(self, status, message, execution_time, detailsinfo=""):
        """
        Create a JSON log containing information about the pipeline execution.

        Args:
            status (str): Pipeline status, can be "Success" or "Failed".
            message (str): Message indicating the result or reason for failure.
            execution_time (float): Pipeline execution time in seconds.
            detailsinfo (str, optional): Additional information for the log. Default is "".

        Returns:
            str: JSON string containing the log information.
        """

        timestamp = datetime.now().strftime("%m-%d-%y-T%H:%M:%S")

        pipeline_logs = {
            "PipelineLogs": {
                "PipelineID": self.pipeline_id,
                "Timestamp": timestamp,
                "Status": status,
                "Message": message,
                "ExecutionTime": execution_time,
            },
            "BigQueryLogs": self.get_bigquery_logs(self.table_ids),
            "Details": self.create_details(detailsinfo)
        }

        return json.dumps(pipeline_logs, indent=4)

    def get_bigquery_logs(self, table_ids):
        """
        Get logs for BigQuery tables (Table Sizes).

        Args:
            table_ids (list): List of IDs of BigQuery tables.

        Returns:
            list: List of dictionaries containing the current size of each table.
        """

        bigquery_logs = [] 
        client = bigquery.Client(project=self.project_id)

        for table_id in table_ids:
            query = f"SELECT COUNT(*) AS size FROM `{table_id}`"
            results = client.query(query).to_dataframe()
            size = results['size'].iloc[0]
            size = int(size)

            bigquery_logs.append({
                "BigQueryID": table_id,
                "Size": size
            })

        return bigquery_logs

    def create_details(self, detailsinfo=""):
        """
        Create details section for the log.

        Args:
            detailsinfo (str, optional): Additional information for the log. Default is "".

        Returns:
            list: List containing detailed information.
        """

        details = []
        details.append({"additional_info": detailsinfo})
        return details

    def upload_logs_to_bucket(self, logs):
        """
        Upload JSON logs to a Google Cloud Storage bucket.

        Args:
            logs (str): JSON string to load.

        Returns:
            bool: True if the load is successful, False otherwise.
        """

        try:
            storage_client = storage.Client()
            bucket = storage_client.bucket(self.bucket_name)

            timestamp = datetime.now().strftime("%m-%d-%Y_T%H:%M:%S")
            filename = f"{self.folder_bucket}/{timestamp}_logs.json"

            blob = bucket.blob(filename)
            blob.upload_from_string(logs, content_type='application/json')
            logging.info(f'✔ Uploaded log file {
                         filename} to bucket {self.bucket_name}')
            return True
        except Exception as e:
            logging.error(f'017:Error uploading JSON file {
                          filename} to bucket {self.bucket_name}: {e}')
            return False

    def generate_the_logs(self, execution_status, msg, start_timer, logs_details):
        """
        Generate and upload logs for the pipeline execution.

        This function generates JSON logs containing information about the pipeline execution and uploads them to a Google Cloud Storage bucket.

        Args:
            execution_status (str): Status of the pipeline execution, it can be "Success" or "Failed".
            msg (str): Message indicating the result or reason for failure.
            start_timer (float): Timestamp indicating the start of pipeline execution.
            logs_details (str): Additional details to include in the logs.

        Returns:
            None
        """

        final_msg = msg
        end_timer = time.time()  # End timer to calculate pipeline execution time
        execution_time = end_timer - start_timer
        logs = self.add_metadata_to_log(
            execution_status, final_msg, execution_time, logs_details)
        self.upload_logs_to_bucket(logs)
