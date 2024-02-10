import subprocess
import glob
import os
import logging

def openPDF(digits, directory=None):
    directory = directory or r"C:\Users\ianza\OneDrive\Documents\CSV\CertificateStatements"
    logging.info(f"Searching for PDF file with digits: {digits}")
    logging.info(f"Searching in directory: {directory}")
    
    try:
        # Check if the directory exists
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory '{directory}' does not exist.")

        # Get a list of all PDF files in the directory
        pdfFiles = glob.glob(os.path.join(directory, "*.pdf"))

        # Iterate through each PDF file
        for pdfFile in pdfFiles:
            # Extract the last 4 digits of the filename (excluding the extension)
            filename = os.path.basename(pdfFile)  # Get the filename without the directory path
            filenameWithoutExtension = os.path.splitext(filename)[0]  # Remove the extension
            
            # Extract the last 4 digits from digits if necessary
            if len(digits) > 4:
                digits = digits[-4:]

            last4Digits = filenameWithoutExtension[-4:]  # Get the last 4 digits
            logging.info(f"Checking file: {pdfFile}, last 4 digits: {last4Digits}")

            # Check if the last 4 digits match the desired value (digits)
            if last4Digits == digits:
                # Found the matching PDF file
                # Open the PDF file using the default PDF viewer
                logging.info(f"Matching PDF file found: {pdfFile}")
                subprocess.Popen([pdfFile], shell=True)
                return pdfFile
        
        # If no matching PDF file is found
        logging.info("No matching PDF file found.")
        return None
    
    except Exception as e:
        # Handle any exceptions and log the error
        logging.error(f"Error occurred while opening PDF: {str(e)}")
