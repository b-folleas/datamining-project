import download
import enrichment
import insertion

if __name__ == "__main__" :

    images_source = 'ikarus777/best-artworks-of-all-time'
    insert_table = 'paintings'

    # Getting all the downloaded images in a list from download.py
    
    # Choosing random images
    images_list = download.choose_rand_image(images_source, 30)
    # Downloading these images
    download.download_images(images_list)

    # Go through each images_list item to get it's meta-data
    for image in images_list :
        print(image["path"])
        img_meta_data = enrichment.set_img_data(image["path"])  

        print(img_meta_data)
        # Inserting these metadata of each image into the table paintings of the database
        meta_data_keys = list(img_meta_data.keys())
        meta_data_values = list(img_meta_data.values())

        insertion.insert(insert_table, meta_data_keys, meta_data_values)
    