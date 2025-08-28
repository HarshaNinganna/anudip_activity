import PyPDF2

def merge_pdfs(pdf_list, output_filename):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        try:
            merger.append(pdf)
            print(f"Added: {pdf}")
        except Exception as e:
            print(f"Error with {pdf}: {e}")
    merger.write(output_filename)
    merger.close()
    print(f"\n
          Merged PDF saved as: {output_filename}")


if __name__ == "__main__":
    # Example usage
    print("=== PDF Merger Tool ===")
    files = input("Enter PDF filenames separated by commas: ").split(",")
    files = [f.strip() for f in files]

    output = input("Enter output filename (e.g. merged.pdf): ").strip()
    if not output.endswith(".pdf"):
        output += ".pdf"

    merge_pdfs(files, output)
