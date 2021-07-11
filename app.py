# importing pandas for reading the dataset
import pandas as pd

# Getting our Data
df = pd.read_csv('../Komic King/heroes_information.csv')

# Dropping unnecessary columns
df = df.drop(['Unnamed: 0', 'Alignment'], axis=1)

# importing Flask and other modules
from flask import Flask, request, render_template 
import os
  
# Flask constructor
app = Flask(__name__)   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods = ["GET", "POST"])
def comic():
    if request.method == "POST":
        
       # Fetching Details
       l = []
       comic_char = request.form.get("comic_char")
       name_index = (df[df['name'] == comic_char].index.values)
       df1 = df.iloc[name_index, :]
       for i in df.columns.tolist():
           a = df1[i]
           for j in a:
               l.append(i.upper()+": "+str(j))
       return render_template('comic_template.html', output = l)
        
    return render_template('comic_template.html')
  
if __name__=='__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host='0.0.0.0', port=port)