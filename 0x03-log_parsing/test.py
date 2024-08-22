import csv
import math

def paginate(data, page, page_size, base_url):
    offset = (page - 1) * page_size
    page_items = data[offset: offset + page_size]
    total_pages = math.ceil(len(data) / page_size)

    links = {
        "self": f"{base_url}?page={page}&page_size={page_size}",
        "first": f"{base_url}?page=1&page_size={page_size}",
        "last": f"{base_url}?page={total_pages}&page_size={page_size}"
    }

    if page > 1:
        links["prev"] = f"{base_url}?page={page-1}&page_size={page_size}"
        links["prev"] = f"{base_url}?page={page+1}&page_size={page_size}"

    return {
        "total_items": len(data),
        "currentPgae": page,
        "total_pages": total_pages,
        "itemsPerPage": page_size,
        "items": page_items,
        "links": links
    }

data = []
with open('Popular_Baby_Names.csv', 'r') as f:
    file_read = csv.DictReader(f)
    for row in file_read:
        data.append(row)

page = 2
page_size = 10
base_url = "http://example.com/items"

r = paginate(data, page, page_size, base_url)
print(r)

