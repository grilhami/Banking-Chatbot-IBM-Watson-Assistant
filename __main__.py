import sys

# Remove this import when you have found the way to integrate more than 1 function!
from balance_enquiry import helper

"""
    Nawar: I do not know how to integrate Watson Assistant and Cloud Functions if the parameter is like this.
    So I commented the code, and the one used is the one after this comment.

from faq import get_answer
from balance_enquiry import get_balance

def main(args):
    Parameters
    ----------
    args : dict
        Should contain a key `intent` that has a key of either `faq`
        or `balance_enquiry`. If `intent` == `balance_enquiry`, 
        `args` should contain the key `username' and `password`,
        which both have string values. If `intent` == `faq`, then
        `args` should contain the keys `environment_id`, `collection_id`,
        and `questions`, which all have valeus of strings.

    if args['intent'] == "balance_enquiry":
        return get_balance(args['username'], args['password'])
    elif args['intent'] == "faq":
        return get_answer(
                        args['environment_id'], 
                        args['collection_id'], 
                        args['question']
                        )
    else:
        return {"message": "Great question! Unfortunately, I \
            currently don't know how to anser that. Please \
            contact customer support at customer_support@bank.com"}
"""


"""
    Real Function begins here.
"""
def main(args):
    return helper(args)