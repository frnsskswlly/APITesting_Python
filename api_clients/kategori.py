from assertpy import assert_that

from api_clients.base import APIClient

class KategoriAPI(APIClient):
	def __init__(self, email, password):
		super().__init__()
		self.base_url = "https://secondhand-6-3-staging.herokuapp.com/v1/kategori"
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


	def get_all(self):
		return self.get(self.base_url)



	def create(self, payload):
		return self.post(self.base_url, json=payload)



	def destroy(self, id):
		return self.delete(self.base_url + f"/{id}")