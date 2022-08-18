import requests


# kategoriResponse = requests.get('https://secondhand-6-3-staging.herokuapp.com/v1/kategori/')
# kategori = kategoriResponse.json()
# code = kategoriResponse.status_code
# print(kategori["data"])

# buku_id = 1
# bukuResponse = requests.get(f'https://secondhand-6-3-staging.herokuapp.com/user/buku/{buku_id}')

# print(bukuResponse.headers["Token"])

# buku = bukuResponse.json()

# code = bukuResponse.status_code
# assert code == 201, "Code doesn't match"

# print(bukuResponse.url)

# print(buku[0]["id"])
# assert buku[0]["id"] == 1

# print(buku[0]["nama"])
# assert buku[0]["nama"] == "Hujan"

# print(buku[0]["penjual_barang"]["nama"])
# assert buku[0]["penjual_barang"]["nama"] == "Anniel Miftasya"


# payload = {
# 	"email": "magdalisa@gmail.com",
#     "password": "magdalisa123"
# }

# login = requests.post('https://secondhand-6-3-staging.herokuapp.com/auth/login', json=payload)
# user = login.json()
# print(login.status_code)
# print(user["data"]["token"])



# print(login.json()["message"])

namaKategori = {
	"jenis_buku": "eBooks"
}

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1hZ2RhbGlzYUBnbWFpbC5jb20iLCJwYXNzd29yZCI6IiQyYiQxMCR4L2lqaERFQi4ySi9yaXpnWlJwQ3guVTIxTTQvZUFSQnl2TFZXclo2OUJUUnYvcnlEZXJBQyIsImlhdCI6MTY2MDcxNDUzMX0.MjGlhHJO9Qy8FAu8cERKuti3ybGN66kb-qUzEsBHtfQ"	
kategoriResponse = requests.post('https://secondhand-6-3-staging.herokuapp.com/v1/kategori/', json=namaKategori, headers={'Token': token })
code = kategoriResponse.status_code
# message = kategoriResponse.json()["message"]

print(code)
# print(message)