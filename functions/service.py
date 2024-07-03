
import requests #making an api with the pip install request

database = {
    1: "Khanyi",
    2: "Ifa",
    3: "Billy"

}

def get_user_from_db(user_id):
    return database.get(user_id)

#define API function 
def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    
    raise requests.HTTPError

