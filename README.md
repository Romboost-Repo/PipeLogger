<h1 align="center">🚀 PipeLogger Library 🚀</h1>

<p align="center">
  <strong>Simplify the generation and management of logs in your data pipelines.</strong>
</p>

<p align="center">
  <a href="https://github.com/Romboost-Repo/PipeLogger"><img src="https://img.shields.io/github/stars/Romboost-Repo/PipeLogger?style=social" alt="GitHub stars"></a>
  <a href="https://pypi.org/project/pipelogger/"><img src="https://img.shields.io/pypi/v/pipelogger" alt="PyPI version"></a>
  <a href="https://github.com/Romboost-Repo/PipeLogger/issues"><img src="https://img.shields.io/github/issues/Romboost-Repo/PipeLogger" alt="GitHub issues"></a>
  <a href="https://github.com/Romboost-Repo/PipeLogger/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Romboost-Repo/PipeLogger" alt="License"></a>
</p>

---

## 📖 What is PipeLogger?

**PipeLogger** is a library designed to standardize the creation of logs in data pipelines, providing a consistent format that facilitates problem identification and troubleshooting. With **PipeLogger**, you can manage detailed and structured logs, enabling more effective tracking of operations and deeper analysis of data ingestion processes.

### 🚀 Main features

- **Log standardization:** PipeLogger creates detailed logs that follow a consistent format, making them easy to read and analyze.
- **Integration with Google Cloud Platform (GCP):** Designed for pipelines deployed on GCP, supporting Cloud Functions and Cloud Run.
- **BigQuery Table Monitoring:** Logs and monitors the size of BigQuery tables over time.
- **Storage in Google Cloud Storage:** Automatically stores logs in a GCP bucket for centralized access and management.
---

## 🌟 Example of Log Generated

PipeLogger creates logs in a clear and structured JSON format as follows:

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

---

## 💻 Implementation

### 📋 Prerequisites

Before implementing PipeLogger, make sure you meet the following requirements:

- The pipeline must be deployed on **Google Cloud Platform (GCP)**, using **Cloud Functions** or **Cloud Run**.
- The pipeline must interact with **BigQuery tables**.
- A **bucket on Google Cloud Storage** is required to store the generated logs.

### 🛠️ How to Implement PipeLogger in your Pipeline

Follow the steps detailed in our [**Official Documentation**](https://github.com/Romboost-Repo/PipeLogger/blob/main/docs/implementation.ipynb) to integrate PipeLogger into your pipeline projects.

### 🧑‍💻 Example of Basic Use

```python
from pipelogger import logsformatter
import time

# Initialize the log formatter
logger = logsformatter(
    pipeline_id="Pipeline-Example",
    table_ids=["project.pipeline-example.table_1", "project.pipeline-example.table_2"],
    project_id="your-gcp-project-id",
    bucket_name="your-gcs-bucket",
    folder_bucket="logs_folder"
)

# Simulate pipeline execution
start_time = time.time()

# Simulation of pipeline operations....

# Generate and upload logs
logger.generate_the_logs(
    execution_status="Success",
    msg="Data uploaded successfully",
    start_timer=start_time,
    logs_details=["Process completed without errors."]
)
```

---

## 📦 Installation

You can easily install PipeLogger from PyPI using pip:

```bash
pip install pipelogger
```

---

## 📚 Complete Documentation

For complete details on implementation, advanced configuration and more usage examples, visit the [**Official Documentation**](https://github.com/Romboost-Repo/PipeLogger).

---

## 🤝 Contribute

Contributions are welcome! If you have ideas, improvements or have found a bug, please open an issue or submit a pull request in our [**GitHub repository**](https://github.com/Romboost-Repo/PipeLogger).

---

## 📄 License

This project is licensed under the terms of the [**MIT License**](https://github.com/Romboost-Repo/PipeLogger/blob/main/LICENSE).

---

## 📧 Contact

If you have any questions, feel free to contact us through [**our GitHub page**](https://github.com/Romboost-Repo/PipeLogger) or send us an email.
