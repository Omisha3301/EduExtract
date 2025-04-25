# EduMapr – AI-Powered Syllabus Summarizer & Book Finder

**EduMapr** is a web application that assists students and educators in extracting meaningful structure from syllabus PDFs. It focuses on converting academic course syllabus documents into a clear and concise summary, highlighting key topics, prerequisites, and listing recommended books. The app combines OCR, a language model API, and basic web scraping into a single workflow. Designed for usability, EduMapr offers a simple interface where users can upload a syllabus and receive a compact breakdown of its contents. 

---

## Text Recognition from Syllabus PDFs

The app begins by handling uploaded syllabus PDFs, which may include scanned or digitally generated documents. To ensure accessibility across different file formats, OCR is applied using a hosted model. This allows for text extraction even from image-based syllabi. The extracted content is processed and checked for relevance before further steps are taken. This prevents unnecessary model calls and helps maintain consistent results. The OCR process outputs a markdown-formatted version of the syllabus content, which is used as the input for further summarization. The current setup is able to handle multi-page documents and works well with most common syllabus formats.

---

## Summarization Using Language Model API

After the text is extracted, it is passed to a language model endpoint that has been instructed to return structured information. The model provides a short summary of the course, a list of topics in an estimated learning sequence, prerequisite knowledge (if any), and a list of recommended book titles found in the document. This step is handled through an API call using a chat-based interface with a fixed output structure in JSON format. No fine-tuning has been done — the model is used as-is with prompt design focused on consistency. This part of the app helps organize syllabus content into a digestible format and reduces the need to manually scan through lengthy PDFs.

---

## Book Search and Integration

If the syllabus contains recommended books, their titles are used to perform a basic web search through automation. The app queries Amazon India for each book and retrieves the first available match. It extracts details like the book title, author, price, and thumbnail, and provides a link to view the book online. This process uses standard HTML parsing techniques and returns only what is publicly visible. It's intended to help users quickly identify which books are being referenced and find them in one place. While not a perfect match every time, the method offers a reasonable level of accuracy and works well for commonly listed academic titles.

---

## Interface and Workflow Integration

The app is built using Streamlit to provide a simple and interactive frontend. Users can upload a PDF, wait for the processing, and view the structured results on the same page. The application is modular, with each task (OCR, summarization, book lookup) handled separately and stitched together in a clean pipeline. It is currently deployed to the cloud and publicly accessible. There is room for future enhancements, but the current version is functional and focused on core use cases.

---

## Deployment

The application is deployed on Render and can be accessed at the following link: [EduMapr](https://edumapr.onrender.com/).

---
