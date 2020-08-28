def column_stats(df, column):
    stats_dict = {'max': df[column].max(),
                  'min': df[column].min(),
                  'mean': round(df[column].mean()),
                  'range': df[column].max() - df[column].min()}
    return stats_dict
