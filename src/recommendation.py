# -*- coding: utf-8 -*-
from datetime import datetime

import database_driver as db_driver
import database_manager as db_manager
from sklearn import tree
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


def user_recommend(user_id):
    '''___.\n
    :param user_id: (int) The id of the user to chom we are recommending paintings to like.\n
    :display: Printing to the terminal ...
    :return: None
    '''
    history = db_manager.get_user_history(user_id)
    print(history)
    dataframe = pd.DataFrame(history,
                             columns=['favorite', 'painting_id', 'artist_id', 'artist_name', 'century', 'genre', 'artist_nationality', 'date', 'width',
                                      'height', 'orientation', 'flash'])

    resultframe = dataframe['favorite']

    # resultframe = resultframe.astype(dtype={'favorite': "bool"})

    metadataframe = dataframe[['orientation', 'flash', 'width',
                               'height']]

    # Use of random forest classifier
    rfc = RandomForestClassifier(n_estimators=10, max_depth=2,
                                 random_state=0)

    print("resultframe", metadataframe)

    rfc = rfc.fit(metadataframe, resultframe)

    paintings = db_manager.get_paintings()

    print(rfc.feature_importances_)

    for item in paintings:
        # item[6] = str(item[6])
        #print(item)
        test_item = [ item[2], item[3], item[4], item[5] ]
        #print(test_item)
        prediction = rfc.predict(
            [test_item]
        )
        if ( prediction == True ):
            return item




if __name__ == "__main__":
    db_driver.connect_database()

    user_recommend(2)

    db_driver.close_connection()

