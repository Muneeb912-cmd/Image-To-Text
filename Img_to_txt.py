from PIL import Image
import pytesseract
import os

def extract_text_from_images(folder_path, output_file_path):
    # Set the path to the Tesseract executable (modify this based on your Tesseract installation path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Open the output file for writing
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Iterate through all files in the specified folder
        for filename in os.listdir(folder_path):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                # Construct the full path to the image file
                image_path = os.path.join(folder_path, filename)

                # Open the image using Pillow
                img = Image.open(image_path)

                # Perform OCR on the image
                text = pytesseract.image_to_string(img)
                print('Completed :' ,filename)
                # Write the extracted text to the output file
                output_file.write(f"{text}\n")
                

if __name__ == "__main__":
    # Specify the folder path containing images
    folder_path = r"G:/free lancing/New folder (2)"

    # Specify the output file path
    output_file_path = "output.txt"

    # Call the function to extract text from images and write to the output file
    extract_text_from_images(folder_path, output_file_path)

    print(f"Text extraction completed. Results written to {output_file_path}")
