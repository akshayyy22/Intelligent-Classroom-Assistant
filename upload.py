import requests

def upload_pdf(file_path):
    url = "https://file.io/"
    with open(file_path, "rb") as file:
        response = requests.post(url, files={"file": file})
        if response.status_code == 200:
            return response.json()["link"]
        return None

pdf_path = "output/lecture_notes.pdf"
download_link = upload_pdf(pdf_path)
if download_link:
    print("PDF uploaded successfully! Download link:", download_link)
else:
    print("Upload failed.")