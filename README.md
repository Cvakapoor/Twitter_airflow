# 🐦 Twitter ETL with Airflow on AWS

This project demonstrates a Twitter ETL pipeline built with **Tweepy**, orchestrated by **Apache Airflow** running on an **AWS EC2 instance**, with the output CSV file stored in an **S3 bucket**.

---

## 📌 Project Overview

- **Extract**: Connects to the Twitter API v2 to search for public tweets containing the keyword `"football"`.
- **Transform**: Filters and extracts metadata like tweet text, creation time, like and retweet counts.
- **Load**: Saves the cleaned tweet data as a CSV to **Amazon S3**.
- **Orchestration**: Managed using **Apache Airflow**, deployed on an EC2 instance.

---

## 🛠️ Project Structure

├── dags/
│ └── twitter_dag.py # Airflow DAG definition
├── etl/
│ └── twitter_etl.py # Tweepy-based ETL script
├── README.md # This file



---

## 🚀 Getting Started

### 1. Twitter API Setup

- Sign up at [Twitter Developer Portal](https://developer.x.com/en/portal/dashboard).
- Create a project and app.
- Generate a **Bearer Token** for API v2.
- Store the token securely via Airflow Variables or environment variables.

```bash
airflow variables set TWITTER_BEARER_TOKEN "your_bearer_token_here"

### 2. AWS Setup

✅ EC2 Instance
Launch an EC2 instance (Ubuntu, Amazon Linux, etc.)

Install Airflow and dependencies

Ensure the instance has access to S3 either via:

An attached IAM Role with S3 permissions, or

AWS credentials in ~/.aws/credentials

✅ S3 Bucket
Create an S3 bucket (or use an existing one)

### 3. Airflow Configuration

Start Airflow on your EC2 instance:

airflow db init
airflow webserver --port 8080
airflow scheduler

Visit http://<EC2-public-IP>:8080 in your browser.

Enable and run the twitter_etl_dag.

🧾 Sample Output

CSV file: football_tweets.csv

Stored in: s3://your-bucket-name/twitter/football_tweets.csv

🐍 Python Requirements

Install dependencies:

pip install tweepy pandas apache-airflow
