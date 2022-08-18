import requests
from assertpy import assert_that
import pytest


class TestUser:

	URL = "https://secondhand-6-3-staging.herokuapp.com"


	def test_tambah_user(self):
		payload = {
			"nama": "Efrata",
    		"email": "efrata@gmail.com",
    		"password": "efrata123"
		}

		response = requests.post(self.URL + '/auth/register/user', json=payload)
		data = response.json()
		code = response.status_code

		assert_that(code).is_equal_to(200)
		assert_that(data["message"]).is_equal_to("Data User Ditambahkan!")
		assert_that(data["data"]["nama"]).is_equal_to("Efrata")
		assert_that(data["data"]["email"]).is_equal_to("efrata@gmail.com")
		assert_that(data["data"]["level"]).is_equal_to("user")


	def test_tambah_admin(self):
		payload = {
			"nama": "Efrata Wilmann",
    		"email": "efratawilmann@gmail.com",
    		"password": "efrata123"
		}

		response = requests.post(self.URL + '/auth/register/admin', json=payload)
		data = response.json()
		code = response.status_code

		assert_that(code).is_equal_to(200)
		assert_that(data["message"]).is_equal_to("Data Admin Ditambahkan!")
		assert_that(data["data"]["nama"]).is_equal_to("Efrata Wilmann")
		assert_that(data["data"]["email"]).is_equal_to("efratawilmann@gmail.com")
		assert_that(data["data"]["level"]).is_equal_to("admin")

	@pytest.fixture
	def test_login(self):
		payload = {
			"email": "efratawilmann@gmail.com",
    		"password": "efrata123"
		}

		response = requests.post(self.URL + '/auth/login', json=payload)
		data = response.json()
		code = response.status_code

		assert_that(code).is_equal_to(200)
		assert_that(data["message"]).is_equal_to("User found!")
		assert_that(data["data"]["user"]["email"]).is_equal_to("efratawilmann@gmail.com")
		assert_that(data["data"]["user"]["nama"]).is_equal_to("Efrata Wilmann")
		assert_that(data["data"]["user"]["level"]).is_equal_to("admin")

		token = data["data"]["token"]
		

		return token


	def test_edit_admin(self, test_login):

		token = test_login

		payload = {
		    "foto": "https://res.cloudinary.com/aurellieandra/image/upload/v1657692476/second_hand/sh_seeds/girl-profilepic_cik3wi.webp",
		    "nama": "Efrata Wilmann Snichdjer",
		    "kota": "Malang",
		    "alamat": "Jl. Looping No. 18",
		    "nohp": "08123456789"
		}

		response = requests.put(self.URL + '/v1/admin', json=payload, headers={'Token': token})
		data = response.json()
		code = response.status_code

		assert_that(code).is_equal_to(201)
		assert_that(data["email"]).is_equal_to("efratawilmann@gmail.com")
		assert_that(data["nama"]).is_equal_to("Efrata Wilmann Snichdjer")
		assert_that(data["kota"]).is_equal_to("Malang")
		assert_that(data["alamat"]).is_equal_to("Jl. Looping No. 18")
		assert_that(data["nohp"]).is_equal_to("08123456789")


	def	test_edit_user(self):
		token = test_login

		payload = {
		    "foto": "https://res.cloudinary.com/aurellieandra/image/upload/v1657692476/second_hand/sh_seeds/girl-profilepic_cik3wi.webp",
		    "nama": "Efrata",
		    "kota": "Malang",
		    "alamat": "Jl. Looping No. 18",
		    "nohp": "08123456789"
		}

		response = requests.put(self.URL + '/v1/user', json=payload, headers={'Token': token})
		data = response.json()
		code = response.status_code

		assert_that(code).is_equal_to(201)
		assert_that(data["email"]).is_equal_to("efrata@gmail.com")
		assert_that(data["nama"]).is_equal_to("Efrata")
		assert_that(data["kota"]).is_equal_to("Malang")
		assert_that(data["alamat"]).is_equal_to("Jl. Looping No. 18")
		assert_that(data["nohp"]).is_equal_to("08123456789")


	def test_get_user_by_login_id(self):
		token = test_login

		response = requests.get(self.URL + '/v1/user', headers={'Token': token})
		data = response.json()
		code = response.status_code

		assert_that(code).is_equal_to(201)
		assert_that(data["email"]).is_equal_to("efrata@gmail.com")
		assert_that(data["nama"]).is_equal_to("Efrata")
		assert_that(data["level"]).is_equal_to("user")


	def test_get_admin_by_login_id(self, test_login):
		token = test_login

		response = requests.get(self.URL + '/v1/admin', headers={'Token': token})
		data = response.json()
		code = response.status_code

		assert_that(code).is_equal_to(201)
		assert_that(data["email"]).is_equal_to("efratawilmann@gmail.com")
		assert_that(data["nama"]).is_equal_to("Efrata Wilmann Snichdjer")
		assert_that(data["level"]).is_equal_to("admin")


	def test_delete_user(self):
		user_id = 8
		response = requests.get(self.URL + '/v1/user' + f'/{user_id}', headers={'Token': token})
		data = response.json()
		code = response.status_code

		assert_that(code).is_equal_to(201)
		assert_that(data["msg"]).is_equal_to("Data user berhasil dihapus!")

	def test_delete_admin(self):
		admin_id = 8
		response = requests.get(self.URL + '/v1/admin' + f'/{admin_id}', headers={'Token': token})
		data = response.json()
		code = response.status_code

		assert_that(code).is_equal_to(201)
		assert_that(data["msg"]).is_equal_to("Data admin berhasil dihapus!")
