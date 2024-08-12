<h1 align="center">PipeLogger Library</h1>

### What does the Pipelogger library do?
Pipelogger is a library created to establish a standard format for execution logs in pipelines mainly related to data ingestion. The standard form is this:

```json
 {
  "PipelineLogs": {
    "PipelineID": "Pipeline-Example",
    "Timestamp": "MM-DD-YY-THH:MM:SS",
    "Status": "Success",
    "Message": "Data uploaded successfully",
    "ExecutionTime": 20.5075738430023
  },
  "BigQueryLogs": [
    {
      "BigQueryID": "project.pipeline-example.table_1",
      "Size": 1555
    },
    {
      "BigQueryID": "project.pipeline-example.table_2",
      "Size": 3596
    }
  ],
  "Details": [
    {
      "additional_info": [
        "Data downloaded successfully",
        "Data processed successfully",
        "Data uploaded successfully"
      ]
    }
  ]
}
```

### What should you consider when implementing the PipeLogger in your pipeline?

* The pipeline must be deployed in GCP, either as Cloud Function or Cloud Run. 
* The pipeline must feed Big Query tables.
* The pipeline needs a bucket to store the logs.


### 

### How to implement it in any Pipeline?
> [Take a look at the Official PipeLogger Documentation](https://github.com/Romboost-Repo/PipeLogger/blob/main/docs/implementation.ipynb)

---