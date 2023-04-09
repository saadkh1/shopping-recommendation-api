import pandas as pd
import numpy as np
from tqdm.notebook import tqdm
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, jsonify

app = Flask(__name__)

articles = pd.read_excel("dataset.xlsx").set_index('article_id')

prod_name_enc = LabelEncoder()
group_name_enc = LabelEncoder()
index_enc = LabelEncoder()

articles['prod_name'] = prod_name_enc.fit_transform(articles['prod_name'])
articles['product_group_name'] = group_name_enc.fit_transform(articles['product_group_name'])
articles['index_name'] = index_enc.fit_transform(articles['index_name'])

dims = [
    'prod_name',
    'product_type_no',
    'product_group_name',
    'graphical_appearance_no',
    'colour_group_code',
    'perceived_colour_value_id',
    'perceived_colour_master_id',
    'department_no',
    'index_name',
    'index_group_no',
    'section_no',
    'garment_group_no'
]

article_vectors = articles[dims].values
article_ids = articles.index.values
article_data = {"id": article_ids, "vector": article_vectors}

class CosineSimilarityIndex():
    def __init__(self, article_vectors, labels):
        self.article_vectors = article_vectors.astype('float32')
        self.labels = labels
        
    def query(self, vector, k=5):
        similarities = cosine_similarity([vector], self.article_vectors).flatten()
        indices = similarities.argsort()[::-1][:k]
        return [self.labels[i] for i in indices]

index = CosineSimilarityIndex(article_data['vector'], article_data['id'])

similar_items_dict = {"item": [], "similar_items": []}
for x in range(len(article_data['vector'])):
    similar_items = index.query(article_data['vector'][x])
    similar_items_dict['item'].append(article_data['id'][x])
    similar_items_dict['similar_items'].append([item for item in similar_items if item != article_data['id'][x]])
similarities_df = pd.DataFrame(similar_items_dict)

def get_similar_items(item):
    similar_items = similarities_df.loc[similarities_df['item'] == item, 'similar_items'].iloc[0]
    return list(map(str, similar_items))

@app.route('/get_similar_items/<int:item>', methods=['GET'])
def get_similar_items_api(item):
    if item is None:
        return "Error: No item provided. Please specify an item."
    else:
        similar_items = get_similar_items(item)
        return jsonify({'similar_items': similar_items})

if __name__ == '__main__':
    app.run(debug=True)