""" Used to transform the dataframe from wide formate to long formate. """

from typing import Literal

from pandas import DataFrame


def wide_to_long(df: DataFrame, df_name: Literal['State', 'District']):
    """ Converts:
            Wide formate --> Long formate 

    Returns:
        list[DataFrame]: [religion, household_number, caste, education, household_size, age_groups]
    """

    id_vars = ['State', 'District'] if df_name == 'District' else ['State']

    religion = df.melt(id_vars,
                       ['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists',
                        'Jains', 'Others_Religions', 'Religion_Not_Stated'],
                       var_name='Variable', value_name='Value')

    household_number = df.melt(id_vars,
                               ['Rural_Households', 'Urban_Households'],
                               var_name='Variable', value_name='Value')

    caste = df.melt(id_vars,
                    ['SC', 'ST'],
                    var_name='Variable', value_name='Value')

    education = df.melt(id_vars,
                        ['Primary_Education', 'Middle_Education', 'Secondary_Education',
                            'Higher_Education', 'Graduate_Education'],
                        var_name='Variable', value_name='Value')

    household_size = df.melt(id_vars,
                             ['Household_size_1_person_Households',
                                 'Household_size_2_persons_Households',
                                 'Household_size_1_to_2_persons',
                                 'Household_size_3_persons_Households',
                                 'Household_size_3_to_5_persons_Households',
                                 'Household_size_4_persons_Households'],
                             var_name='Variable', value_name='Value')

    age_groups = df.melt(id_vars,
                         ['Age_Group_0_29', 'Age_Group_30_49',
                             'Age_Group_50', 'Age not stated'],
                         var_name='Variable', value_name='Value')

    return [religion, household_number, caste, education, household_size, age_groups]
