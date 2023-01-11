from topic_matcher import topic_match

email_topics = {'ctadler@ucsc.edu':{'cats', 'dogs', 'lego'},
                'kyosifov@ucsc.edu':{'computers', 'snacks', 'swimming'},
                'johndoe@email.com':{'politics', 'covid', 'candy'}}

url = 'https://www.cnn.com/travel/article/frontier-airlines-flights-cat-adoption-trnd/index.html'
keywords = {'cats', 'adopt', 'airplane'}

emails, returned_url = topic_match(email_topics, url, keywords)

for email in emails:   
    print(email, returned_url)