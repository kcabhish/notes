# Computer Vision

Computer vision is the area of artificil intelligence that deals with the analysis of visual input. such as photographs, vidoes and live camera feeds.

One of the most common machine learningmodel architectures for computer vision is convolutional neural network (CNN), a type of deep learning architecture. CNNs use filters to extract numerical feature maps from imges, and then feed the feture values into a deep learning model to geenrate a label prediction. 

## Multiple types for computer vision model.

- Image Classification is a for of computer vision in which a modal is trained with images that are labeled with the main subject of the image so that it can analyze unlabeld images and predict te most appropriate label - identifying the subject of the image.

- Object Detection: Form of computer vision in which the model is trained to identify the location of specific objects in an image.

- Sematic Segmentation: Is an advanced form of object detection where, rather than indicate an object's location by drawing a box around it, the model can indetify the individual pixels in the image that belog to a particular object.

- Multi-modal models: This combine visual features and associated text descriptions, enabling them to generat ecomprehensive descriptions of images.

## Common use of Computer vision Scenarios

- AI agents that can interpret visual input.
- Auto-captioning or tag-generation for photographs.
- Visual search.
- Monitoring stock levels or identifying items for checkout in retail scenarios.
- Security video monitoring.
- Authentication through facial recognition.
- Robotics and self-driving vehices.


# Responsible AI

It is a term used to describe considerations for building AI systems that includes guardrails to mitigte the risk of harmful, illegal, or offensive content generation or automated actions.

## Principles of Responsible AI

- **Fairness**: AI developers need to take care to minimize bias in training data and test AI systems for fairness.
- **Reliability and safety**: AI is based onprobabilistic models, it is not infallible. AI-powered applications need to take this into account and mitigate risks accordingly.
- **Privacy and Security**: Models are trained using data, which may include personal information. AI developers have responsibilites to ensure that the training data is kept secure, andthat the trained models themseleves can't be used to reveal private personal or organizational details.
- **Inclusiveness**: The potential of AI to improve lives and drive success should be open to everyone. AI developpers should strive to ensure that their solutions don't exclude some users.
- **Transparency**: AI can sometime seem like "magic", but its important to make users aware of how the system works and any potential limitations it may have.
- **Accountability**: Ultimately, the people and organizations that develop and distribute AI solutions are accountable for theif actions. It's important for organizationsn developing AI models and applications to define and apply a framework of governance to help ensure that they apply responsible AI priciples to their work.

# Explore AI Workloads

1. Open the [Computing History agent](https://aka.ms/computing-history-browser).
    The app downloads and initializes the required MobileNet computer vision model and `Phi 3.5 mini` models.
2. [Chat Playground](https://aka.ms/chat-playground)
    In the panel left change the default instructions to "you are an AI assistant that analuzes and summarizes text"

3. [Information Extractor](https://aka.ms/info-extractor)
    Use this sample to upload images of the [receipts](https://aka.ms/receipts).

# Transformers

Transformers work by processing huge volumes ofdata, and encoding language tokens (representing individual words or phrases) as vector-based embeddings (arrays of numeric values). A technique called attention is used to assign embedding values that reflect different aspects of how each token i used in the context of other tokens.

# AI-Powered information extraction concepts

Information extraction is a workload that combines multiple AI techniques to extract data from content - often digital documents. A comprehensive information extraction solution involves elements of computer vision to detect text in image-based data; and machine learning, or increasingly generative AI, to semantically map the extracted text to specific data fields.

- Text detection and extraction from images using optical character recognition (OCR).
- Value identification and mapping from the OCR results to data fields.

## OCR (Optical Character Recognition)

Optical Character Recognition (OCR) is a technology that automatically converts visual text in images - whether from scanned documents, photographs, or digital files—into editable, searchable text data. Rather than manually transcribing information, OCR enables automated data extraction from:

- Scanned invoices and receipts
- Digital photographs of documents
- PDF files containing images of text
- Screenshots and captured content
- Forms and handwritten notes

### The OCR pipeline: A step-by-step process

The stages in the OCR process are:

- Image acquisition and input.
- Preprocessing and image enhancement.
- Text region detection.
- Character recognition and classification.
- Output generation and post-processing.