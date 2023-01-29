# India Census 2011 Dashboard

After taking the session of **CampusX DSMP Program**. I decided that this would be a good project to improve my **Data Wrangling and Data Interpretation** ability.

## Data Gathering

### 1. Census data get from kaggle.

- [Dataset 1](https://www.kaggle.com/datasets/sirpunch/indian-census-data-with-geospatial-indexing)
- [Dataset 2](https://www.kaggle.com/datasets/danofer/india-census?select=india-districts-census-2011.csv)

### Disclaimer

- Data is not **appropriate or absolute** to belive. I just used it for practicing purpose.

## Inspired from [CampusX](https://youtube.com/@campusx-official) a Data Science YouTube channel.

## Process of Thinking | Notetaking

### 1. For Populations data :

- Plot a `scatter_mapbox` for each _States and Districts_.
- Plot a `pie chart` for `male-female` distributions in _States_. _Do this only for States._

### 2. For Literacy Data :

- Plot a `scatter_mapbox` for each _States and Districts_.
- Plot a `pie chart` for `male-female` distribution in _States_.

### 3. For Castes Group Data :

- This data contains two caste groups `SC & ST`. So we can plot the only the `pie charts` for each _States_.
- For Districts we can plot the `nested pie plot` for each **States's Districts**.\*

### 4. For Religions Data :

- This contains _maybe_ five religions overall. So we have again plot the `nested pie plot` for each _States and Districts_.

### Common Thoughts :

1. Plot some default `scatter plot` with plotly to display many feature analysis in one graph.
2. After analysing the `Rough Analysis.py` graphs I found that `Litracy` columns does not depict the way it has to. That's why we have to calculate the `litracy rate` of the particulars.

## Feature Engineering

1. In the dataset _Male, Female and Literate_ columns are present instead of _Literacy Rate and Sex Ratio_.
2. The dataset is in _wide formate_ so I turn it into _long formate_ for analysis.

## Created by [arv-anshul](https://github.com/arv-anshul)

Used dataset is not appropiate for real life analysis. I just used it to improve my skills. Find the used datasets [here](#1-census-data-get-from-kaggle).
