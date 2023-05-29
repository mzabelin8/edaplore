# EDAPLORE (Explore EDA)
Edaplore is a Python-based project for Exploratory Data Analysis (EDA). The project aims to automate various aspects of EDA, saving time and effort while providing essential insights into the data.

## Features
The main feature of this project is the generation of a comprehensive HTML report of the data. This report includes data separation, overview, comparison, and the generation of a correlation map.

## Getting Started
Prerequisites
Python 3.6 or later
Required Python packages: pandas, Jinja2
To install the required packages, use the following command:

pip install edaplore

git clone https://github.com/mzabelin8/edaplore.git

##Here's an example of how to run the code:
import pandas as pd
from edaplore imoprt Report
data = pd.read_csv('path_to_data')
path = 'path_to_save'
R = Report(data,
           path,
           fill_mis=False,
           drop_outliers=False,
           ohe=False)
data: This is a pandas DataFrame that you want to analyze.
path: This is the path where the generated HTML report will be saved.
fill_mis: This is a boolean that indicates whether missing values should be filled. The default is False.
drop_outliers: This is a boolean that indicates whether outliers should be dropped. The default is False.
ohe: This is a boolean that indicates whether one-hot encoding should be performed. The default is False.
After running the above script, an HTML report will be generated and saved to the specified path​1​.

## License
This project is licensed under the terms of the MIT license.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contact
You can get in touch with me at my email: mzabelin8@gmail.com
