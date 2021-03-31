# -*- coding: utf-8 -*-

import database_driver
from sklearn import tree
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


def user_recommend(user_id):
    history = database_manager.get_user_history(user_id)
    result = []
    data = []

    for item in history:
        data.append(database_manager.get_painting_metadata(item[0]))
        result.append(item[1])

    dataframe = pd.DataFrame(data,
                             columns=['artist_id', 'orientation', 'flash', 'width',
                                      'height', 'date', 'camera_make', 'camera_model'])

    dataframe['date'] = pd.to_datetime(dataframe['date'], format='%Y-%m-%d')

    dataframe = dataframe.astype(dtype={"artist_id": "int64", "orientation": "int64",
                                        "flash": "int64", "width": "int64", "height": "int64",
                                        "camera_model": "<U200"})

    resultframe = pd.DataFrame(result, columns=['favorite'])

    print(dataframe)
    print(resultframe)

    le1 = LabelEncoder()
    dataframe['camera_make'] = le1.fit_transform(dataframe['camera_make'])

    le2 = LabelEncoder()
    dataframe['camera_model'] = le2.fit_transform(dataframe['camera_model'])

    le3 = LabelEncoder()
    dataframe['date'] = le3.fit_transform(dataframe['date'])

    le4 = LabelEncoder()
    dataframe['orientation'] = le4.fit_transform(dataframe['orientation'])

    le5 = LabelEncoder()
    dataframe['flash'] = le5.fit_transform(dataframe['flash'])

    le6 = LabelEncoder()
    dataframe['width'] = le6.fit_transform(dataframe['width'])

    le7 = LabelEncoder()
    dataframe['height'] = le7.fit_transform(dataframe['height'])

    # Use of random forest classifier
    rfc = RandomForestClassifier(n_estimators=10, max_depth=2,
                                 random_state=0)
    rfc = rfc.fit(dataframe, resultframe.values.ravel())

    print(rfc.feature_importances_)


'''
    #prediction
    prediction = rfc.predict([
    [le1.transform(['red'])[0], le2.transform(['nature'])[0],
     le3.transform(['thumbnail'])[0], le4.transform(['portrait'])[0]]])

    df_  = pd.DataFrame(user_history,
                                             columns=['date', 'painting_number', 'all_painting'])

    df_paintings_through_time['date'] = pd.to_datetime(df_paintings_through_time['date'], format='%Y-%m-%d')
    df_paintings_through_time = df_paintings_through_time.astype(dtype={"painting_number": "int64",
                                                                    "all_painting": "int64"})



    #generating numerical labels
    le1 = LabelEncoder()
    dataframe['color'] = le1.fit_transform(dataframe['color'])

    le2 = LabelEncoder()
    dataframe['tag'] = le2.fit_transform(dataframe['tag'])

    le3 = LabelEncoder()
    dataframe['size'] = le3.fit_transform(dataframe['size'])

    le4 = LabelEncoder()
    dataframe['mode'] = le4.fit_transform(dataframe['mode'])

    le5 = LabelEncoder()
    resultframe['favorite'] = le5.fit_transform(resultframe['favorite'])

    #Use of random forest classifier
    rfc = RandomForestClassifier(n_estimators=10, max_depth=2,
                                 random_state=0)
    rfc = rfc.fit(dataframe, resultframe.values.ravel())

    #prediction
    prediction = rfc.predict([
        [le1.transform(['red'])[0], le2.transform(['nature'])[0],
         le3.transform(['thumbnail'])[0], le4.transform(['portrait'])[0]]])

    print(le5.inverse_transform(prediction))

    print(rfc.feature_importances_)
'''

if __name__ == "__main__":
    database_driver.connect_database()

    user_recommend(2)
