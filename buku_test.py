from urllib import response
import pytest
from assertpy import assert_that

from api_clients.buku import BukuAPI


@pytest.fixture(scope="session")
def buku_api():
	api = BukuAPI(email="efratawilmann@gmail.com", password="efrata123")
	api.login()
	return api


def test_get_all_data_buku_seller(buku_api):
	response = buku_api.get_all_seller()
	data = response.json()
	code = response.status_code

	# checking the json result
	assert_that(code).is_equal_to(201)
	assert_that(data["data"]).is_not_empty()



def test_tambah_buku(buku_api):
	# from-data input, need to set the filename:none to avoid content-disposition error
	payload = {
		"nama": (None, "Bola: Edisi Chelsea"),
		"deskripsi": (None, "Edisi khusus tentang tim bola Chelsea"),
		"gambar": (None, ""),
		"harga": (None, 325000),
		"pengarang": (None, "Bola"),
		"lokasi": (None, "Jakarta"),
		"tahun_terbit": (None, "2022"),
		"kategori_id": (None, 17)
	}
	
	response = buku_api.create(payload)
	code = response.status_code
	data = response.json()

	assert_that(code).is_equal_to(201)
	assert_that(data["nama"]).is_equal_to("Bola: Edisi Chelsea")

def test_delete_buku(buku_api):
	id = 12

	response = buku_api.destroy(id)
	data = response.json()
	code = response.status_code

	assert_that(code).is_equal_to(201)
	assert_that(data["msg"]).is_equal_to("")

def test_get_all_buku(buku_api):
	response = buku_api.get_all()
	data = response.json()
	code = response.status_code

	# checking the json result
	assert_that(code).is_equal_to(201)
	assert_that(data["data"]).is_not_empty()


def test_search_data_buku(buku_api):
	keyword = "surat"
	response = buku_api.search(keyword)
	data = response.json()
	code = response.status_code

	#checking the json result
	assert_that(code).is_equal_to(201)
	
	assert_that(data["data"]).is_not_empty()



def test_get_buku_by_id(buku_api):
	# buku_id = 1
	# bukuResponse = requests.get(self.URL + f'/user/buku/{buku_id}')
	# buku = bukuResponse.json()["buku"][0]
	# code = bukuResponse.status_code

	# assert_that(code).is_equal_to(201)
	# assert_that(["id"]).is_equal_to(1)
	# assert_that(["nama"]).is_equal_to("Hujan")
	# assert_that(["pengarang"]).is_equal_to("Tere Liye")
	# assert_that(["penjual_barang"]["nama"]).is_equal_to("Anniel Miftasya")
	pass


def test_edit_detail_buku_by_id(buku_api):
	pass


def test_filter_terjual(buku_api):
	pass


def test_filter_diminati(buku_api):
	pass