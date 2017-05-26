# Reproducible Data Analysis: real world products database

Goals:

- [ ] map similar sizes into the general size (XXL -> 2XL etc.)
- [ ] map colors into the groups (LIGHT GREEN -> GREEN)
- [ ] clean brands
- [ ] map categories
- [ ] extract features from title
- [ ] map codes
- [ ] find similar products
- [ ] group similar products with equal properties across the distibutors.

Working with dataset of `1'561'159` products.

Drop me a message if you want to get raw dataset (**all sensitive data removed**).

List of all keys:

```json
{ "_id" : "_id", "value" : null }
{ "_id" : "brand", "value" : null }
{ "_id" : "category", "value" : null }
{ "_id" : "code", "value" : null }
{ "_id" : "color", "value" : null }
{ "_id" : "size", "value" : null }
{ "_id" : "source", "value" : null }
{ "_id" : "title", "value" : null }
```

Example of the record:

```javascript
{
        "_id" : ObjectId("55fedbc4c702283c66877c14"),
        "code" : "A4N3234",
        "title" : "MARATHON T",
        "color" : "FOREST",
        "source" : "shemeka",
        "size" : "L",
        "category" : "performance",
        "brand" : "a4"
}
```

Import dataset into the database (mongodb):

```bash
mongoimport -d <database_name> -c data --file=products.json
```

Create indexes (in mongodb console ```mongo <database_name>```):

```javascript
db.data.createIndex({code: 1})
db.data.createIndex({color: 1});
db.data.createIndex({size: 1});
db.data.createIndex({source: 1});
db.data.createIndex({brand: 1});
db.data.createIndex({category: 1});
```

NOTE: `source` original distributor name replaced with alias.


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
