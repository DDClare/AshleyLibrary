import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    group = activities.groupby(by='sell_date')
    stats = group.agg(
        num_sold=('product', 'nunique'),
        products=('product', lambda x: ','.join(sorted(set(x))))
    ).reset_index()
    stats.sort_values(by='sell_date', inplace=True)
    return stats








