CREATE TABLE "users" (
  "id" id,
  "fk_preferences_id" int,
  "username" string,
  "password" string
);

CREATE TABLE "history" (
  "fk_user_id" int,
  "fk_image_id" int,
  "favorite" boolean
);

CREATE TABLE "preferences" (
  "id" id,
  "favorite_color" string,
  "favorite_orientation" string,
  "favorite_size" string
);

CREATE TABLE "images" (
  "id" id,
  "image_url" string,
  "color_primary" string,
  "color_secondary" string,
  "orientation" string,
  "size_x" int,
  "size_y" int,
  "creation_date" datetime,
  "camera" string,
  "geo_data" string
);

CREATE TABLE "tags_list" (
  "id" id,
  "fk_images_id" int,
  "fk_tags_id" int
);

CREATE TABLE "tags" (
  "id" id,
  "tag_name" string
);

ALTER TABLE "users" ADD FOREIGN KEY ("fk_preferences_id") REFERENCES "preferences" ("id");

ALTER TABLE "users" ADD FOREIGN KEY ("id") REFERENCES "history" ("fk_user_id");

ALTER TABLE "images" ADD FOREIGN KEY ("id") REFERENCES "history" ("fk_image_id");

ALTER TABLE "images" ADD FOREIGN KEY ("id") REFERENCES "tags_list" ("fk_images_id");

ALTER TABLE "tags" ADD FOREIGN KEY ("id") REFERENCES "tags_list" ("fk_tags_id");
