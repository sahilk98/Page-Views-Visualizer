import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df =  pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &\
        (df['value'] <= df['value'].quantile(0.975)) ]


def draw_line_plot():
    fig = df.plot(figsize = (10,5), color = 'red').figure
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
      # Copy and modify data for monthly bar plot
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(["year","month"])["value"].mean()
    df_bar1 = df_bar.unstack()

    # Draw bar plot

    monthname = ["January", "February", "March", "April", 'May', "June", "July","August", "September", "October", "November", "December"]
    bp = df_bar1.plot(figsize=(5,5), kind='bar', label = monthname)
    bp.set_xlabel('Years'); bp.set_ylabel('Average Page Views')
    bp.legend(labels = monthname, title='Months')
    fig = bp.figure

    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]

    df_box1 = df_box.copy()
    df_box1['month_nums'] = [d.month for d in df_box.date]
    df_box1 = df_box1.sort_values(by=['month_nums'])

    # Draw box plots (using Seaborn)

    fig, axs = plt.subplots(figsize=(8,5),nrows=1, ncols=2)
    axs[0] = sns.boxplot(x= df_box['Year'], y="value", data=df_box, ax=axs[0])
    axs[0].set_ylabel('Page Views')
    axs[0].set_title('Year-wise Box Plot (Trend)')

    axs[1] = sns.boxplot(x= df_box1['Month'], y="value", data=df_box1, ax= axs[1])
    axs[1].set_ylabel('Page Views')
    axs[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
