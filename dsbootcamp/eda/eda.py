import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def cat_summary(data, col_name):
    print(pd.DataFrame({col_name: data[col_name].value_counts(),
                        "Ratio": 100 * data[col_name].value_counts() / len(data)}), end="\n\n\n")
    sns.countplot(x=col_name, data=data)
    plt.show()


def cat_summary_adv(data, number_of_classes=10):
    """
        This function gives the summary of categorical variables for the given pandas dataframe

        Parameters
        ----------
        data: pandas dataframe 
            Dataframe that comprises categorical variables to be analysed
        number_of_classes: float
            Default argument is given as 10 as generally categorical variables have fewer than 10 classes.
            Also categorical variables that have more than 10 classes will not be summarized and they will
            be printed.

        Examples
        ----------
        cat_summary_adv(df)

        or

        cat_summary_adv(df, 15)
    """
    import pandas as pd
    categorical_cols = [col for col in data.columns if data[col].dtypes == 'O']
    var_count = 0  # Number of cat. variables will be printed.
    vars_more_classes = []  # Number of cat. variables that have more than given argument number_of_classes will be returned.
    
    for var in categorical_cols:
        if data[var].nunique() <= number_of_classes:  # select according to its number of classes
            print(pd.DataFrame({var: data[var].value_counts(),
                           "Ratio (%)": round(100 * data[var].value_counts()/ len(data), 2)}), end="\n\n\n")
            var_count += 1
        else:
            vars_more_classes.append(data[var].name)
    print(f"{var_count} categorical variables have been described.\n\n")
    if len(vars_more_classes) > 0:
        print(f"There are {len(vars_more_classes)} variables which have more than {number_of_classes} classes.\n\n")
        print(f"Variable names that have more than {number_of_classes} classes.\n\n")
        print(vars_more_classes)



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



def target_summary_with_cat(data, target):
    col_names = [col for col in data.columns 
                 if len(data[col].unique()) < 10 
                 and col not in target]
    
    for var in col_names:
        print(pd.DataFrame({"TARGET_MEAN": data.groupby(var)[target].mean()}), end="\n\n\n")
