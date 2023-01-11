def topic_match(email_topics, url, keywords):
    email_list = []
    for email, topics in email_topics.items():
        if topics & keywords:
            email_list.append(email)
    return email_list, url