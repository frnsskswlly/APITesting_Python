import pytest
from assertpy import assert_that

from api_clients.kategori import KategoriAPI

@pytest.fixture(scope="session")
def kategori_api():
	api = KategoriAPI(email="efratawilmann@gmail.com", password="efrata123")
	api.login()
	return api

def test_get_all_kategori(kategori_api):
	response = kategori_api.get_all()

	data = response.json()
	code = response.status_code

	assert_that(code).is_equal_to(201)
	assert_that(data["data"]).is_not_empty()


def test_create_kategori(kategori_api):
	payload = {
		"jenis_buku": "Teenlit"
	}
	
	response = kategori_api.create(payload)
	code = response.status_code
	data = response.json()


	assert_that(code).is_equal_to(201)
	jenis_buku = data["jenis_buku"]
	assert_that(data["jenis_buku"]).is_equal_to(jenis_buku)


def test_delete_kategori(kategori_api):
	id = 15
	response = kategori_api.destroy(id)
	code = response.status_code
	data = response.json()

	assert_that(code).is_equal_to(201)
	assert_that(data["msg"]).is_equal_to("Data buku berhasil dihapus")

	# need to create another case to make assure the data is completely deleted


