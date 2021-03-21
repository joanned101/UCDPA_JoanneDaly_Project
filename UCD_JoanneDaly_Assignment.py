# Import csv file into a Pandas DataFrame
import pandas as pd
movie_data = 'IMDb movies.csv'
df = pd.read_csv(movie_data, low_memory=False)

# Dataframe with columns of interest only
data = pd.DataFrame(df, columns=['title', 'year', 'genre', 'production_company', 'budget', 'worldwide_gross_income'])

# Dataframe overview
print(data.head())
print(data.shape)
print(df.dtypes)

# Create a List from csv file
df.values.tolist()
print(df)

# Set index and sort and slice because dataset is very large
data_index = df.set_index("year").sort_index()
print(data_index)
data_20 = data_index.loc["2000":"2020"]
print(data_20)

# Counting missing values
print(data_20.isna().sum())
# Filling missing values not relevant to this dataset.
# Option to replace all NaN elements with 0s -> data_20.fillna(0)
# Option to propagate non-null values forward or backward -> data_20.fillna(method='ffill')

# Merge 2 dataframes not relevant to this dataset.
# Merge two dataframes on one column -> dfm = df1.merge(df2, on ='col')
# Merge on two columns with suffixes -> dfm2 = df1.merge(df2, on =['col2', 'col2'], suffixes=('_col1', '_col2'))

# Dataset too large to make use of so an alternative smaller file was found in order to perform analysis

# Make use of API and for loop
import requests
url = 'http://www.omdbapi.com/?t=avengers+endgame&apikey=71b7c9cf'
r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
    print(key + ':', value)

# Import new dataset
movie3_df = pd.read_csv("movies.csv")

# Take a look at general details of dataset
print(movie3_df.head())
print(movie3_df.shape)
print(movie3_df.isna().sum())

# Initial analysis of movie3_df dataset
# Find out the top scoring movie per genre using sort and groupby
top_genre = movie3_df.sort_values('score',ascending=False).groupby('genre')['name','score'].first()
print(top_genre)

# Find out the top grossing movie per genre
top_gross = movie3_df.sort_values('gross', ascending=False).groupby('genre')['name','gross'].first()
print(top_gross)

# Calculate the average runtime per movie: mean = 106.5513 minutes
time_movie = movie3_df['runtime'].mean()
print(time_movie)

# Count how many movies by title per genre
count_genre = movie3_df[['genre', 'name']].groupby('genre').count()
print(count_genre)

# Preparing visualisations
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['axes.facecolor']='lightgrey'
font1 = {'family':'serif', 'color':'blue', 'size':18, 'fontweight':'bold'}
font2 = {'family':'serif', 'size':10, 'style':'italic'}

# Visual 1: Average RUNTIME Histogram
movie3_df['runtime'].plot(kind='hist', bins=20)
plt.title("AVERAGE RUNTIME OF MOVIE", fontdict=font1)
plt.xlabel("Runtime (minutes)", fontdict=font2)
plt.ylabel("Movie Count", fontdict=font2)
plt.grid(axis='y', color='grey', linestyle='--', linewidth=0.5)
plt.show()

# Visual 2: Box plot of same data
movie3_df['runtime'].plot(kind='box')
plt.title("AVERAGE RUNTIME OF MOVIE", fontdict=font1)
plt.grid(axis='y', color='grey', linestyle='--', linewidth=0.5)
plt.show()

# Visual 3: Count plot of Movie Genres
sns.countplot(x="genre", data=movie3_df)
plt.title("MOVIE GENRES", fontdict=font1)
plt.xlabel("Movie Genres", fontdict=font2)
plt.xticks(rotation=90)
plt.ylabel("Count", fontdict=font2)
plt.show()

# Visual 4: Bar plot of Ratings
movie3_df[['rating', 'name']].groupby('rating').count().plot(kind='bar')
plt.title("MOVIE RATINGS", fontdict=font1)
plt.xticks(rotation=90)
plt.xlabel('Movie Rating', fontdict=font2)
plt.ylabel('Title Count', fontdict=font2)
plt.grid(axis='y', color='grey', linestyle='--', linewidth=0.5)
plt.show()


# Visual 5: Scatter plot of score and gross
sns.scatterplot(x="score", y="gross", data=movie3_df, hue="genre")
plt.title("IMDB RATING -vs- GROSS BOX-OFFICE INTAKE BY GENRE", fontdict=font1)
plt.xlabel('IMDB Rating', fontdict=font2)
plt.ylabel('Gross Box-Office intake', fontdict=font2)
plt.show()


























































