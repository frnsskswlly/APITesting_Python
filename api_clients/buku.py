from assertpy import assert_that

from api_clients.base import APIClient

class BukuAPI(APIClient):
    def __init__(self, email, password):
        super().__init__()
        self.base_url = "https://secondhand-6-3-staging.herokuapp.com"
        self.seller_route = "/seller/buku"
        self.user_route = "/user/buku"
        self.search_route = "/cari?nama="
        self.token = ""
        self.email = email
        self.password = password


    def login(self):
        payload = {
			"email": self.email,
			"password": self.password
		}
        response = self.post('https://secondhand-6-3-staging.herokuapp.com/auth/login', json=payload)
        data = response.json()
        code = response.status_code
        assert_that(code).is_equal_to(200)
        assert_that(data["message"]).is_equal_to("User found!")
        token = data["data"]["token"]
        assert_that(token).is_not_empty()
        self.headers = {'Token': token}
        return token

    def get_all_seller(self):
        return self.get(self.base_url + self.seller_route)
    
    def create(self, payload):
        return self.post(self.base_url + self.seller_route, files=dict(payload))
    
    def destroy(self, id):
        return self.delete(self.base_url + self.seller_route + f"/{id}")

    def get_all(self):
        return self.get(self.base_url + self.user_route)

    def search(self, search_term):
        return self.get(self.base_url + self.search_route + f"{search_term}")

    def get_data_by_id(self, id):
        return self.get()