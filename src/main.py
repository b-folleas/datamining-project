# -*- coding: utf-8 -*-

import database_driver as db_driver
import download
import seed

import visualization

import recommendation


if __name__ == "__main__":
    images_source = 'ikarus777/best-artworks-of-all-time'
    
    number_images = int(input("Nombre images à télécharger :\n"))
    number_history = int(
        input("Nombre de lignes à ajouter dans l'historique :\n"))

    # Choosing random images
    images_list = download.choose_rand_image(images_source, number_images)

    # Downloading these images
    download.download_images(images_source, images_list)

    # Launch connection to the database, used for seeding the database
    db_driver.connect_database()

    # Seeding database
    seed.seed_database(images_source, images_list, number_history)

    # Getting the user to study
    user_id = int(input("Rentrer l'id de l'utilisateur à étudier :\n"))

    # Recommendation
    print("Recommendation : painting_id ", recommendation.user_recommend(user_id))

    # Visualization
    visualization.plot_user_history(user_id)
    # visualization.plot_users_dashboard()
    visualization.plot_likes_by_artist()
    visualization.plot_paintings_through_time()

    # Launch connection to the database, used for seeding the database
    db_driver.close_connection()
