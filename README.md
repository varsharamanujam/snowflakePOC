# Exploring_Snowflake
This Proof of Concept (POC) focuses on the intricacies of revenue forecasting, using a real-world scenario as our guiding light. We've chosen the domain of revenue prediction to showcase the power of Snowflake's data handling capabilities.

## Directory Structure

Ensure that the directory structure is as follows:

```
your_package/
|-- your_package/
|   |-- __init__.py
|   |-- performAnalysis.py
|   |-- uploadData.py
|--Dataset/
|   |--items.csv
|-- setup.py
|-- config.json
|-- README.md
```


## Prerequisites

- **config.json**: Users must provide this file containing the following data:

  ```json
  {
      "user": "",
      "password": "",
      "account": "",
      "warehouse": "",
      "database": "",
      "schema": "",
      "testtable":""
    }


Dataset Folder: Create a folder named Dataset and place items.csv inside it. The dataset can be downloaded from [this link](https://www.kaggle.com/datasets/oscarm524/revenue-forecast)

Installation
Clone the Repository: Clone this repository to your local machine:
