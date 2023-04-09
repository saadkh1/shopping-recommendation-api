# Recommendation API for Shopping Products

This is a Flask-based API for providing personalized fashion recommendations for shopping products. The API uses cosine similarity to find the most similar items to a given item.

## Installation

To use this API, follow the steps below:

1. Clone the repository or download the code.

```bash
git clone https://github.com/saadkh1/shopping-recommendation-api.git
```

2. Install the required Python packages using pip.

```bash
! pip install -r requirements.txt
```

3. Download the dataset from Kaggle [here](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data). Alternatively, The dataset used in this project is available in the dataset.xlsx file, and product images are available in the shopping.zip file provided in this repository.

4. Start the Flask server.

```bash
python product_recommender_api.py
```

## Usage

After starting the server, you can access the API at http://localhost:5000.

To get the most similar items to a given item, make a GET request to http://localhost:5000/get_similar_items/<item_id>, where <item_id> is the ID of the item you want to find similar items for.

For example, to get the most similar items to item 219075028, make a GET request to 'http://localhost:5000/get_similar_items/219075028'.

The API will return a JSON object containing the IDs of the most similar items.

```bash
{
  "similar_items": ["219075014", "219075021", "219075017", "567"]
}
```

To test the recommendation system, use the test.ipynb notebook file. This file demonstrates how to load the dataset, run the recommendation system, and retrieve the list of similar items for a specific item.


Note that the API uses cosine similarity to find the most similar items, so the results may not be perfect. Additionally, the dataset used by the API is from H&M's Personalized Fashion Recommendations competition on [Kaggle](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data), so the results may be biased towards H&M products.
