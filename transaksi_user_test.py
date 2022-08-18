import pytest
from assertpy import assert_that

from api_clients.transaksi_user import TransaksiUserAPI

@pytest.fixture(scope="session")
def transaksi_user_api():
	api = TransaksiUserAPI(email="efratawilmann@gmail.com", password="efrata123")
	api.login()
	return api