import sys
from google.cloud import storage
from google.cloud import vision

def analyze_pdf(file_path):
    # Upload the PDF to Google Cloud Storage
    storage_client = storage.Client()
    bucket = storage_client.bucket('your-bucket-name')
    blob = bucket.blob('your-blob-name')
    blob.upload_from_filename(file_path)

    # Call the Vision API to analyze the PDF
    client = vision.ImageAnnotatorClient()
    gcs_source_uri = 'gs://your-bucket-name/your-blob-name'
    gcs_source = vision.GcsSource(uri=gcs_source_uri)
    input_config = vision.InputConfig(gcs_source=gcs_source, mime_type='application/pdf')
    features = [vision.Feature(type_=vision.Feature.Type.DOCUMENT_TEXT_DETECTION)]
    requests = [vision.AnnotateFileRequest(input_config=input_config, features=features)]
    response = client.batch_annotate_files(requests=requests)

    # Print the results
    for page_response in response.responses[0].responses:
        print(u'Page number: {}'.format(page_response.context.page_number))
        print(u'Full text: {}'.format(page_response.full_text_annotation.text))

if __name__ == "__main__":
    analyze_pdf(sys.argv[1])