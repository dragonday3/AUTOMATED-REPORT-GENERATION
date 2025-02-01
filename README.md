# AUTOMATED-REPORT-GENERATION

**INTERN ID**: CT12GAN

**DOMAIN**: PYTHON PROGRAMMING

**BATCH DURATION**: December 25th, 2024 to February 25th, 2025

**MENTOR NAME**: NEELA SANTHOSH

# **Automated Report Generation: Student Scores Report Generator**

The **Student Scores Report Generator** is a Python-based application designed to streamline the process of analyzing and presenting student performance data. This tool is particularly useful for educators, school administrators, and anyone involved in academic assessment who needs to quickly summarize student scores in a professional format. By leveraging the simplicity of CSV files for data input and the versatility of PDF for output, this project provides an efficient solution for generating comprehensive reports.

**FILES INCLUDED IN THE REPO:**
- automated_report_generation.py (Main Python File)
- File.csv (Sample CSV File)

**KEY FEATURES:**
1. **CSV Data Input**: The application reads student data from a CSV file, which is a widely used format for data storage and exchange. The CSV file must contain at least two columns: `Name` and `Score`. This allows users to easily manage and update student information using spreadsheet software like Microsoft Excel or Google Sheets.

2. **Data Analysis**: Once the data is read, the application performs several key calculations:
  - **Total Score**: The sum of all student scores, providing a quick overview of overall performance.
  - **Average Score**: The mean score calculated from the total scores, offering insights into the general performance level of the class.
  - **Highest and Lowest Scores**: Identifying the best and worst performances helps educators recognize top achievers and those who may need additional support.

3. **PDF Report Generation**: The application generates a well-structured PDF report that includes:
  - A clear and professional title.
  - A table displaying each student's name alongside their score, making it easy to read and understand.
  - A summary section that highlights the total, average, highest, and lowest scores, providing a concise overview of the data.

4. **User-Friendly Interface**: The program prompts users to input the name of the CSV file, making it accessible even for those with limited technical skills. This feature ensures that users can operate the application without needing to modify the code.

**TOOLS/TECH. USED:**
- **Python**: The primary programming language used for developing the application.
- **fpdf**: A library for generating PDF documents in Python.
- **csv**: A built-in Python library for reading and writing CSV files.

**INSTALLATION AND USAGE:** 
To run this project, you need to have Python installed on your machine. You can install the required library using pip. Here are the steps to set up the project:

1. Clone the repo to your local machine:
   - git clone https://github.com/dragonday3/AUTOMATED-REPORT-GENERATION.git

2. Install the required library:
   - pip install fpdf

3. Prepare a CSV file with student data. The file should have format as mentioned in the sample csv file (File.csv)

4. Save the CSV file in the same directory as the script.

5. Run the script:
   - python automated_report_generation.py

6. When prompted, enter the name of the CSV file (including the .csv extension).

8. The program will read the data, analyze it, and generate a PDF report named 'report.pdf' in the same directory.

9. Check the directory for the generated PDF report.

# **OUTPUT**
![Screenshot 2025-01-11 104238](https://github.com/user-attachments/assets/aa2c167e-ab7a-4034-94aa-0ff3e3e30394)
![Screenshot 2025-01-11 104404](https://github.com/user-attachments/assets/f7e699a3-443e-4676-9078-8e603514ee24)
