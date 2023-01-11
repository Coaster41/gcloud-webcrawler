from google.cloud import language_v1

def classify(text, min_confidence=0.7):
    """Classify the input text into categories."""

    language_client = language_v1.LanguageServiceClient()

    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )
    response = language_client.classify_text(request={"document": document})
    categories = response.categories

    result = []

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        if category.confidence > min_confidence:
            result.append(category.name)
    
    


    return result

def filterKeywords(classification_result, min_size = 2):
    keywords = set()
    for words in classification_result:
        words = words.replace(' & ', '/')
        for word in words.split('/'):
            if len(word) >= min_size:
                keywords.add(word.lower())
    return keywords
