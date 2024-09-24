def word_count_handler(event, context):
    """
    A simple function that counts
    the number of words in a string
    """

    if ((not event) or (event.get('body') == None)):
        return {"error": "no body"}

    try:
        msg = event["body"]
        n_words = len(msg.split())

        return {
            "len": len(msg),
            "words": n_words,
        }
    except Exception as e:
        return {"error": e}
    