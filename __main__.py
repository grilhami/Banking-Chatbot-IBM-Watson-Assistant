import sys
from faq import get_answer
from balance_enquiry import get_balance


def main(args):
    if args['intent'] == "faq":
        return get_answer(args['iam_apikey'], args['url'], 
                        args['environment_id'], args['collection_id'], 
                        args['question'])
    elif args['intent'] == "balance_enquiry":
        return get_balance(args['username'], args['password'])
    else:
        message = "Good Question! Sadly, I can't answer that right now."
        return {"message": message}