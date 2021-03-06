import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def cat_summary(dataframe, col_name):
    """
            Summarise categorical col in dataframe

            Parameters
            ----------
            dataframe: pandas dataframe
                Dataframe that comprises categorical variables to be analysed
            col_name: string
                Name of categorical col


            Examples
            ----------
            # for one variable
            import seaborn as sns
            from dsmlbc.eda.eda import cat_summary
            df = sns.load_dataset("titanic")
            cat_summary(df, "age")

            # for all categorical variable
            cat_cols = [col for col in df.columns if df[col].dtypes == 'O']
            for col in cat_cols:
                cat_summary(df, col)


        """

    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}), end="\n\n\n")
    sns.countplot(x=col_name, data=dataframe)
    plt.show()


def cat_summary_adv(dataframe, categorical_cols, number_of_classes=10):
    """
        Summarise categorical cols in dataframe

        Parameters
        ----------
        dataframe: pandas dataframe
            Dataframe that comprises categorical variables to be analysed

        categorical_cols: list
            List of categorical cols

        number_of_classes: int
            Default argument is given as 10 as generally categorical variables have fewer than 10 classes.
            Also categorical variables that have more than 10 classes will not be summarized and they will
            be printed.

        Examples
        ----------
        import seaborn as sns
        from dsmlbc.eda.eda import cat_summary_adv
        df = sns.load_dataset("titanic")
        cat_cols = [col for col in df.columns if df[col].dtypes == 'O']
        cat_summary_adv(df, cat_cols)

    """
    col_count = 0
    cols_more_classes = []
    for col in categorical_cols:
        if dataframe[col].nunique() <= number_of_classes:  # select according to its number of classes
            print(pd.DataFrame({col: dataframe[col].value_counts(),
                                "Ratio (%)": round(100 * dataframe[col].value_counts() / len(dataframe), 2)}),
                  end="\n\n\n")
            col_count += 1
        else:
            cols_more_classes.append(dataframe[col].name)

    print(f"{col_count} categorical variables have been described.\n")
    if len(cols_more_classes) > 0:
        print(f"There are {len(cols_more_classes)} variables which have more than {number_of_classes} classes:")
        print(cols_more_classes)



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
