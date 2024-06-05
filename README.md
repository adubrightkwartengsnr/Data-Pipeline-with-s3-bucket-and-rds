![Getting Started](./Utils/sales_dashboard.png)
<a name="readme-top"></a>

<div align="center">
  <h1><b>ETL-Pipeline-S3-Amazon-Redshidt</b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- [Project Description ](#ETL-Pipeline)
  - [🛠 Built with ](#-built-with-)
    - [Tech Stack ](#tech-stack-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
  - [👥 Authors ](#-authors-)
  - [🤝 Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [🙏 Acknowledgments ](#-acknowledgments-)
  - [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

# Flight-Radar Pipeline <a name="about-project"></a>

**Flight-Radar Pipeline: ETL Pipeline Using S3 bucket,AWS Glue and Amazon Redshift** This project demonstrates a complete ETL (Extract, Transform, Load) data pipeline for processing flight data. The data is extracted from the FlightRadar API, synthetically expanded, stored in Amazon S3, and finally loaded into an Amazon Redshift data warehouse using AWS Glue. The pipeline serves as a robust and scalable solution for data integration, transformation, and analysis tasks.

1. **flight_id**: the unique identification of the flight

2. **flight**: flight number
3. **callsign**: The callsign used by the flight

4. **squawk**: The transponder code used by the flight.

5. **clicks**: The number of times the flight was clicked on the FlightRadar platform.

6. **from_iata**: The IATA code of the departure airport.

7. **from_city**: The city where the departure airport is located.

9. **to_iata**:  The IATA code of the arrival airport.

10. **to_city**: The city where the arrival airport is located.

11. **model**: The model of the aircraft used for the flight
12. **type**: The type of flight

## 🛠 Built With <a name="Technologies Used"></a>
To implement this project, the following technologies and services are used:

1. _Python_: Python is a versatile programming language that is widely used in data engineering for scripting, data manipulation, and automation. In this project, Python scripts are used for extracting data from the FlightRadar API and generating synthetic data to expand the dataset. Python's rich ecosystem of libraries, such as Pandas and NumPy, makes it suitable for these tasks.

2. _Pandas_ and NumPy: Pandas and NumPy libraries were essential for data manipulation and numerical computations.Pandas is a powerful data manipulation and analysis library for Python. In this project, Pandas is used for handling and transforming flight data. It provides data structures like DataFrames, which are essential for processing and analyzing large datasets.

3. _The Flight Radar API_:The FlightRadar API provides access to real-time flight tracking data. In this project, the API is used to extract flight data, which forms the basis of the dataset used in the ETL pipeline. The API provides detailed information about flights, including flight numbers, callsigns, and more.

4. _Visual Studio Code and Jupyter Notebooks_: Jupyter Notebooks within the Visual Studio IDE provided an interactive environment for running code, visualizing data, and documenting the analysis process.

5. _Pyspark_:PySpark is the Python API for Apache Spark, a fast and general-purpose cluster-computing system. In this project, PySpark is used within AWS Glue for large-scale data processing and transformations. PySpark enables efficient handling of big data and is well-suited for distributed computing environments.

6. _Json_: JSON (JavaScript Object Notation) is a lightweight data interchange format. In this project, JSON is used to store and exchange flight data extracted from the FlightRadar API. JSON's readability and ease of use make it a popular choice for API responses and data serialization. 

7. _AWS CLI_: AWS CLI is a unified tool to manage AWS services from the command line. In this project, the AWS CLI is used to upload data to S3, manage Glue jobs, and interact with various AWS services programmatically. It provides a convenient way to automate AWS operations and integrate them into the data pipeline.

8. _SQL_: SQL (Structured Query Language) is used for querying and manipulating relational databases. In this project, SQL is used to query and analyze the flight data stored in Amazon Redshift. SQL's powerful querying capabilities make it indispensable for data analysis and reporting tasks.

9. _Amazon S3_: AWS S3 is an object storage service that provides scalability, data availability, security, and performance. In this project, S3 is used for storing the raw and synthetic flight data before and after processing. It serves as a reliable and cost-effective storage solution for large datasets.

10. _AWS Glue_:AWS Glue is a fully managed ETL service that makes it easy to move data between your data stores. Glue provides both the serverless ETL service and the data catalog. In this project, AWS Glue is used to create ETL jobs that transform and load the flight data from S3 into Amazon Redshift. Glue crawlers are also used to automatically discover and catalog metadata about the datasets.

11. _AWS Redshift_:Amazon Redshift is a fully managed data warehouse service that allows you to run complex queries against petabytes of structured data using standard SQL. In this project, Redshift serves as the data warehouse where the transformed flight data is loaded for further analysis and reporting. Redshift's scalability and performance make it an ideal choice for handling large-scale data analytics.

12. _GitHub_: GitHub served as the version control system for the project, enabling collaboration and tracking changes in the codebase.
    These technologies played a crucial role in the successful implementation of the project, providing the necessary tools to analyze and derive insights from the time series data.


<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>


<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- Features -->

## Project Impact <a name="key-features"></a>
This ETL pipeline project has significant implications:
- Scalability: By leveraging AWS services such as S3, Glue, and Redshift, the pipeline can handle large volumes of data efficiently.

- Data Quality: Synthetic data generation ensures a rich dataset for testing and validation, allowing better insights and data quality checks.

- Automation: AWS Glue enables automated ETL jobs, reducing the need for manual intervention and increasing reliability.

- Real-Time Processing: With modifications, the pipeline can be extended to handle real-time data streaming and processing.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

![image](https://github.com/adubrightkwartengsnr/Data-Pipeline-with-s3-bucket-and-rds)



<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python


### Setup

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone https://github.com/adubrightkwartengsnr/Data-Pipeline-with-s3-bucket-and-rds
```

Change into the cloned repository

```sh
  cd Data-Pipeline-with-s3-bucket-and-rds
  
```

Create a virtual environment

```sh

python -m venv env

```

Activate the virtual environment

```sh
    env/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```


<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Bright Adu Kwarteng Snr**

- GitHub: [GitHub Profile](https://github.com/adubrightkwartengsnr)
- LinkedIn: [LinkedIn Profile](www.linkedin.com/in/bright-adu-kwarteng-snr)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>
- Access to More Data: Obtain access to a larger dataset from the FlightRadar API or other data sources to get more comprehensive insights.
- Data Validation: Implement more rigorous data validation and cleansing processes to ensure the accuracy and reliability of the data.
- Optimize ETL Processes: Fine-tune the ETL jobs for better performance. Use partitioning, indexing, and efficient data formats (like Parquet) to speed up data processing.
- Serverless Architectures: Consider using serverless technologies like AWS Lambda for lightweight ETL tasks to reduce costs and improve scalability.
- Distributed Processing: Use Apache Spark or AWS EMR for large-scale data processing to handle bigger datasets more efficiently.
- Automated Workflows: Use AWS Step Functions or Apache Airflow to automate and orchestrate the entire ETL workflow, ensuring seamless data flow and reducing manual intervention.
- Monitoring and Alerts: Implement comprehensive monitoring and alerting using AWS CloudWatch or other monitoring tools to detect issues and ensure the pipeline runs smoothly.
    
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

I would like to express my sincere gratitude to my instructors Derek Degbedzui, Emile and Theophilus Akugre for their exceptional guidance, unwavering support, and invaluable mentorship throughout the course of this project. Their expertise, dedication, and commitment to our learning journey have been instrumental in shaping our understanding and skills in data engineering.

I would also like to extend a special thank you to Trestle Academy Ghana,INNGEN Technology Solutions, GIZ-Ghana for this opportunity given to us in this 3-month training to equip us with knowledge in data engineering. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>









