import csv
from fpdf import FPDF

# Function to read data from a CSV file
def read_data(file_name):
    """
    Reads data from a specified CSV file and returns it as a list of dictionaries.

    Parameters:
    file_name (str): The name of the CSV file to read.

    Returns:
    list: A list of dictionaries where each dictionary represents a row in the CSV file.
    """
    data = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)  # Read the CSV file as a dictionary
        for row in reader:
            data.append(row)  # Append each row to the data list
    return data

# Function to analyze the data
def analyze_data(data):
    """
    Analyzes the student scores data to calculate total, average, highest, and lowest scores.

    Parameters:
    data (list): A list of dictionaries containing student scores.

    Returns:
    tuple: A tuple containing:
        - total (int): The total of all scores.
        - average (float): The average score.
        - highest (int): The highest score.
        - lowest (int): The lowest score.
    """
    scores = [int(row['Score']) for row in data]  # Extract scores and convert to integers
    total = sum(scores)  # Calculate total score
    average = total / len(scores)  # Calculate average score
    highest = max(scores)  # Find the highest score
    lowest = min(scores)  # Find the lowest score
    return total, average, highest, lowest

# Function to generate a PDF report
def generate_pdf_report(data, total, average, highest, lowest):
    """
    Generates a PDF report of student scores and summary statistics.

    Parameters:
    data (list): A list of dictionaries containing student scores.
    total (int): The total of all scores.
    average (float): The average score.
    highest (int): The highest score.
    lowest (int): The lowest score.
    """
    pdf = FPDF()  # Create a PDF object
    pdf.add_page()  # Add a new page to the PDF
    
    # Title
    pdf.set_font("Arial", 'B', 16)  # Set font for the title
    pdf.cell(0, 10, 'Student Scores Report', ln=True, align='C')  # Add title centered
    
    # Add a line break
    pdf.ln(10)
    
    # Table header
    pdf.set_font("Arial", 'B', 12)  # Set font for the header
    pdf.cell(40, 10, 'Name', 1)  # Column for student names
    pdf.cell(40, 10, 'Score', 1)  # Column for student scores
    pdf.ln()  # Move to the next line
    
    # Table content
    pdf.set_font("Arial", '', 12)  # Set font for the table content
    for row in data:
        pdf.cell(40, 10, row['Name'], 1)  # Add student name
        pdf.cell(40, 10, row['Score'], 1)  # Add student score
        pdf.ln()  # Move to the next line
    
    # Summary
    pdf.ln(10)  # Add a line break before the summary
    pdf.set_font("Arial", 'B', 12)  # Set font for the summary header
    pdf.cell(0, 10, 'Summary', ln=True)  # Add summary title
    pdf.set_font("Arial", '', 12)  # Set font for the summary content
    pdf.cell(0, 10, f'Total Scores: {total}', ln=True)  # Add total score
    pdf.cell(0, 10, f'Average Score: {average:.2f}', ln=True)  # Add average score
    pdf.cell(0, 10, f'Highest Score: {highest}', ln=True)  # Add highest score
    pdf.cell(0, 10, f'Lowest Score: {lowest}', ln=True)  # Add lowest score
    
    # Save the PDF
    pdf.output('report.pdf')  # Save the PDF file as 'report.pdf'

# Main function
def main():
    """
    Main function to execute the program. Reads data from a CSV file, analyzes it,
    and generates a PDF report.
    """
    file_name = input("Please enter the CSV file name (including .csv extension): ")  # Get filename from user
    data = read_data(file_name)  # Read data from the CSV file
    total, average, highest, lowest = analyze_data(data)  # Analyze the data to get statistics
    generate_pdf_report(data, total, average, highest, lowest)  # Generate the PDF report
    print("PDF report generated successfully!")  # Confirmation message

# Execute the main function
if __name__ == "__main__":
    main()  # Run the main function when the script is executed