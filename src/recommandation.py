# -*- coding: utf-8 -*-

import database_driver as db_driver
import database_manager as db_manager
from sklearn import tree
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


def user_recommend(user_id):
    history = db_manager.get_user_history(user_id)

    dataframe = pd.DataFrame(history,
                             columns=['favorite', 'orientation', 'flash', 'width',
                                      'height', 'artist_name', 'century', 'genre', 'artist_nationality'])

    resultframe = dataframe['favorite']

    resultframe = resultframe.astype(dtype={'favorite': "bool"})


    metadataframe = dataframe[['orientation', 'flash', 'width',
                               'height', 'artist_name', 'century', 'genre', 'artist_nationality']]

    metadataframe = metadataframe.astype(dtype={'orientation': "int64", 'flash': "int64", 'width': "int64",
                                        'height': "int64", 'artist_name': "<U200", 'century': "int64", 'genre': "<U200",
                                        'artist_nationality': "<U200"})

    #generating numerical labels
    le1 = LabelEncoder()
    dataframe['artist_name'] = le1.fit_transform(dataframe['artist_name'])

    le2 = LabelEncoder()
    dataframe['genre'] = le2.fit_transform(dataframe['genre'])

    le3 = LabelEncoder()
    dataframe['artist_nationality'] = le3.fit_transform(dataframe['artist_nationality'])


    # Use of random forest classifier
    rfc = RandomForestClassifier(n_estimators=10, max_depth=2,
                                 random_state=0)

    rfc = rfc.fit(metadataframe, resultframe)

    print(rfc.feature_importances_)


if __name__ == "__main__":
    db_driver.connect_database()

    user_recommend(2)

    db_driver.close_connection()
