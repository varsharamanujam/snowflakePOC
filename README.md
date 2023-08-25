# Exploring_Snowflake
This Proof of Concept (POC) focuses on the intricacies of revenue forecasting, using a real-world scenario as our guiding light. We've chosen the domain of revenue prediction to showcase the power of Snowflake's data handling capabilities.

## Directory Structure

Ensure that the directory structure is as follows:

```
snowflakePOC/
|-- snowflakePOC/
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


Dataset Folder: Create a folder named ```Dataset``` and place items.csv inside it. The dataset can be downloaded from [this link](https://www.kaggle.com/datasets/oscarm524/revenue-forecast)

## Installation

**Clone the Repository:** Clone this repository to your local machine:
```git clone https://github.com/varsharamanujam/snowflakePOC.git ```

**Navigate to the Directory:** Move into the cloned directory:
```cd snowflakePOC```

**Install the Package:** Use pip to install the package:
```pip install .```

## Usage
After installation, you can run the following commands from the command line:

**Upload Data:** To upload data, use:
```upload_data path/to/config.json```

Replace path/to/config.json with the actual path to your config.json file.

**Perform Analysis:** To perform analysis, use:

```perform_analysis path/to/config.json```

## Conclusion
Follow the instructions above to explore the capabilities of Snowflake for revenue prediction. Ensure that you have provided the necessary config.json file and dataset as described in the prerequisites.




















