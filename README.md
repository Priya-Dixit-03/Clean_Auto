# Clean_Auto
***Data Cleaning Automation Tool***
🧹 Overview
The Data Cleaning Automation Tool is designed to automate the data cleaning process for datasets in various formats. This tool leverages Python, Pandas, and Streamlit to provide a simple yet powerful interface that allows users to clean, preprocess, and export data efficiently.

The main goal of this project is to streamline the data cleaning process and make it accessible for non-technical users as well as data professionals.

**🚀 Features **
Automatic Data Cleaning: Automatically clean your data by handling common issues like missing values, duplicates, and incorrect data types.

Custom Cleaning Options: Allow users to define custom cleaning rules, such as filtering out rows based on certain conditions.

Streamlit Interface: Interactive web-based interface for users to upload datasets, view results, and download cleaned data.

Export Options: Export cleaned data to CSV or other formats.

Data Insights: View basic data statistics and visualizations for better understanding of the dataset.

**🛠️ Requirements**
Python 3.x

Pandas

Streamlit

You can install the necessary dependencies using pip:

bash
 
 
pip install -r requirements.txt
🚀 Getting Started
1. Clone the Repository
First, clone the repository to your local machine:

bash
 
 
git clone https://github.com/Priya-Dixit-03/Clean_Auto.git
cd Clean_Auto
2. Install Dependencies
Once inside the project folder, install the required Python dependencies:

bash
 
 
pip install -r requirements.txt
3. Run the Application
To launch the Data Cleaning Tool, run the following command:

bash
 
 
streamlit run app.py
This will start a local server and open the tool in your web browser.

🧑‍💻 How to Use
Upload Dataset: Click on the "Upload" button to upload your dataset in CSV or other supported formats.

Choose Cleaning Options: Select the cleaning operations you want to apply (e.g., remove missing values, drop duplicates, etc.).

View Cleaned Data: The tool will automatically clean the data based on your selections and display it in a table.

Download Cleaned Data: Once you're satisfied with the cleaned data, you can download it as a CSV or in other formats.

⚙️ Features of the App
Missing Values Handling: Automatically handle missing values by filling, dropping, or applying custom rules.

Data Type Conversion: Ensure columns have the correct data type (e.g., dates as datetime, integers as integers).

Outlier Detection: Identify and handle outliers in the dataset.

Custom Filtering: Allow users to apply custom filters to clean the data based on specific conditions.

