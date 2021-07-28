import requests
import json

query = """
{
  characters(filter: {name: "sasuke"}) {
    info {
      count
      pages
      next
      prev
    }    
    results {
     _id
      name
      avatarSrc
      description
      rank
      village
    }
  }
}
"""
url = 'http://narutoql.com/graphql?query='+ query
# print(query)
r = requests.get(url)
print(r.status_code)
print(r.text)