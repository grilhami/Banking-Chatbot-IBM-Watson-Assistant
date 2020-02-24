from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def multiple_line_answer(sentences):
    
    if len(sentences) > 1:
        return " ".join(sentences)
    else:
        return sentences[0]

def get_answer(iam_apikey, url, environment_id, collection_id, question):


    authenticator = IAMAuthenticator(iam_apikey)
    discovery = DiscoveryV1(
        version="2018-12-03",
        authenticator=authenticator
    )

    discovery.set_service_url(url)

    query_result = discovery.query(
                                environment_id, 
                                collection_id, 
                                natural_language_query=question,
                                passages=True, 
                                count=3, passages_count=3).get_result()['results'][0]

    answer = multiple_line_answer(query_result['answer'])

    #TODO: handler when question returns no asnwer
    return { 'message': answer}