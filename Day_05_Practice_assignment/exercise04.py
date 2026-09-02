import re
def process_dataset(dataset):
    parsed_data = []
    for item in dataset:
        name = item[0]
        price = float(re.search(r"\d+",item[1]).group(0))
        score = float(re.search(r"\d.+",item[2]).group(0))
        parsed_data.append([name,price,score])
        
    filtered_data = list(filter(lambda x:x[1]<=1000,parsed_data))
    mapped_data = list(map(lambda x:dict(product = x[0],price = x[1],score = x[2]),filtered_data))
    sorted_data = list(sorted(mapped_data,key=lambda x:x['score'],reverse=True))
    for item in sorted_data:
        print(item)
 
data_input = [
    ("Laptop", "Price: 1200", "Rating: 4.8"),
    ("Phone", "Price: 800", "Rating: 4.5"),
    ("Mouse", "Price: 25", "Rating: 4.7"),
    ("Charger", "Price: 15", "Rating: 4.2")
]
process_dataset(data_input)


















