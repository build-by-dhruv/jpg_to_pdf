import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as pdfcanvas


# Function to convert an image (PNG or JPG) to PDF
def convert_to_pdf(input_image_path, output_pdf_path):
    img = Image.open(input_image_path)
    width, height = img.size
    aspect_ratio = width / height

    pdf = pdfcanvas.Canvas(output_pdf_path, pagesize=(letter[1], letter[0]))

    pdf_width, pdf_height = pdf._pagesize
    if aspect_ratio > 1:
        pdf.drawImage(input_image_path, 0, 0, pdf_width, pdf_height)
    else:
        pdf.drawImage(input_image_path, 0, 0, pdf_height * aspect_ratio, pdf_height)

    pdf.showPage()
    pdf.save()


# Function to handle the "Select Images" button click
def select_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.png;*.jpg")])
    if file_paths:
        for input_image_path in file_paths:
            folder_path, file_name = os.path.split(input_image_path)
            output_pdf_path = os.path.join(
                folder_path, f"{os.path.splitext(file_name)[0]}.pdf"
            )
            convert_to_pdf(input_image_path, output_pdf_path)


# Create the tkinter window
root = tk.Tk()
root.title("Image to PDF Converter")
root.geometry("256x256")

# Create and configure the main canvas with red background
canvas = tk.Canvas(root, bg="red", width=256, height=256)
canvas.pack(pady=0, padx=0)
# canvas.pack()

# Create a label for "PDF" in big, bold, white font
pdf_label = tk.Label(
    root, text="PDF", font=("Helvetica", 60, "bold"), bg="red", fg="white"
)
pdf_label.place(relx=0.5, rely=0.45, anchor="center")

# Create and configure the "Select Images" button
select_button = tk.Button(
    root,
    text="Convert",
    font=("Helvetica", 12, "bold"),
    bg="white",
    fg="red",
    command=select_images,
    width=256,
    # borderwidth=0,
)
select_button.place(relx=0.5, rely=0.95, anchor="s")
# Start the tkinter main loop
root.mainloop()