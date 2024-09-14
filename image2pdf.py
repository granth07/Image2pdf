import tkinter as tk
from tkinter import filedialog
from PIL import Image
def select_images():
    file_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if file_paths:
        save_pdf(file_paths)


def save_pdf(image_paths):
    pdf_path = filedialog.asksaveasfilename(
        title="Save PDF as",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        initialfile="output.pdf"
    )

    if pdf_path:
        try:
            images = []
            for image_path in image_paths:
                with Image.open(image_path) as img:
                    # Convert image to RGB mode if it's not
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    images.append(img.copy())  # Use img.copy() to avoid potential issues with the context manager

            # Save all images as a single PDF
            if images:
                images[0].save(
                    pdf_path,
                    save_all=True,
                    append_images=images[1:],
                    resolution=100.0,
                    quality=95
                )
                print(f"PDF saved as: {pdf_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    root = tk.Tk()
    root.title("Image to PDF Converter")
    button = tk.Button(root, text="Select Images", command=select_images)
    button.pack(pady=20)

    # Run the application
    root.mainloop()
if __name__ == "__main__":
    main()
