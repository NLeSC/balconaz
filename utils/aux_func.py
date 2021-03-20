import pandas as pd

# code from https://towardsdatascience.com/from-dataframe-to-network-graph-bbb35c8ab675
# function creating leaderboard
def create_leaderboard(df,col_name, tab_header):
    leaderboard = df[col_name].value_counts(ascending=True)
    s = pd.Series(leaderboard, name=tab_header)
    df2 = s.to_frame().sort_values(tab_header, ascending=False)
    return df2

# trim the long url string for readibility
def trim_url(df, df_idx, str_lst):
    df_simple = df.copy()
    for s in str_lst:
        df_simple[df_idx] = df_simple[df_idx].str.replace(s, '')
    return df_simple

#def highlight_rows(df,v):
#    if df.col > v:
#        return ['background-color: yellow']*df.shape[1]
#    else:
#        return ['background-color: white']*df.shape[1]
#df_guess_simple.style.apply(highlight_rows(0), axis=1)


def sumBy(col_by,df1,df1_m,col_rm,col_m_on,col_sum):
    result = df1.groupby(by=[col_by])[col_sum].count()
    result = pd.merge(df1_m, result, on=col_m_on,how='left').fillna(0)
    del result[col_rm]
    return result


def subtract(df1,df2,col_idx,col_minuend,col_subth):
    result_df = pd.merge(df1,df2, on=[col_idx])
    result_df["delta"] = (result_df[col_minuend]) - result_df[col_subth]
    result_df = result_df.drop([col_minuend, col_subth], axis = 1)
    result_df.rename(columns = {'delta':col_minuend}, inplace = True)
    return result_df