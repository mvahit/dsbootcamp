def cat_summary(data):
    import pandas as pd
    import seaborn as sns
    from matplotlib import pyplot as plt
    cats_names = [col for col in data.columns if len(data[col].unique()) < 10 and data[col].dtypes == 'O']
    for var in cats_names:
        print(pd.DataFrame({var: data[var].value_counts(),
                            "Ratio": 100 * data[var].value_counts() / len(data)}), end="\n\n\n")
        sns.countplot(x=var, data=data)
        plt.show()


def hist_for_nums(data, numeric_cols):
    col_counter = 0
    data = data.copy()
    for col in numeric_cols:
        data[col].hist(bins=20)
        plt.xlabel(col)
        plt.title(col)
        plt.show()
        col_counter += 1
    print(col_counter, "variables have been plotted")