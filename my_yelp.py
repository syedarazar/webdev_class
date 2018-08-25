import requests

def search_businesses(search_term, search_location):

    api_key = "1v3wLTvtgy5cx2BIveW8Yqtx8kNXksFF9OiEpo9AvTXn_jbADvI9zjPO2iPCPT7QwF3KUg_N-6b6sc6-oAbuDEg6DyaFzA1vz-GJVB2hUuMLubYyNMYXRoLtfm5_W3Yx"

    url = "https://api.yelp.com/v3/businesses/search"

    my_headers = {
        "Authorization": "Bearer %s" % api_key
    }

    my_params = {
        "term": search_term,
        "location": search_location,
        "limit": 4,
    }

    businesses_object = requests.get(url, headers=my_headers, params=my_params)

    businesses_dict = businesses_object.text

    print(businesses_dict)

search_businesses("restaurants", "chicago")
