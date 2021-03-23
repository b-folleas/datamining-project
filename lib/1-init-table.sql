CREATE TABLE "users" (
  "user_id" SERIAL PRIMARY KEY,
  "fk_preferences_id" int,
  "username" varchar UNIQUE NOT NULL,
  "password" varchar NOT NULL
);

CREATE TABLE "history" (
  "history_id" SERIAL PRIMARY KEY,
  "fk_user_id" int,
  "fk_painting_id" int,
  "favorite" boolean
);

CREATE TABLE "preferences" (
  "preference_id" SERIAL PRIMARY KEY,
  "favorite_color" varchar,
  "favorite_orientation" varchar,
  "favorite_size" varchar
);

CREATE TABLE "paintings" (
  "painting_id" SERIAL PRIMARY KEY,
  "painting_path" varchar UNIQUE NOT NULL,
  "fk_artist_id" int,
  "color_primary" varchar NOT NULL,
  "color_secondary" varchar,
  "orientation" varchar,
  "flash" int,
  "width" int NOT NULL,
  "height" int NOT NULL,
  "date" date NOT NULL,
  "camera_make" varchar,
  "camera_model" varchar,
  "geo_data" varchar
);

CREATE TABLE "tags_list" (
  "fk_paintings_id" int,
  "fk_tags_id" int
);

CREATE TABLE "tags" (
  "tag_id" SERIAL PRIMARY KEY,
  "tag_name" varchar UNIQUE NOT NULL
);

CREATE TABLE "artists" (
  "artist_id" SERIAL PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL,
  "century" int,
  "genre" varchar,
  "nationality" varchar,
  "number_paintings" int
);

ALTER TABLE "users" ADD FOREIGN KEY ("fk_preferences_id") REFERENCES "preferences" ("preference_id");

ALTER TABLE "history" ADD FOREIGN KEY ("fk_user_id") REFERENCES "users" ("user_id");

ALTER TABLE "history" ADD FOREIGN KEY ("fk_painting_id") REFERENCES "paintings" ("painting_id");

ALTER TABLE "paintings" ADD FOREIGN KEY ("fk_artist_id") REFERENCES "artists" ("artist_id");

ALTER TABLE "tags_list" ADD FOREIGN KEY ("fk_paintings_id") REFERENCES "paintings" ("painting_id");

ALTER TABLE "tags_list" ADD FOREIGN KEY ("fk_tags_id") REFERENCES "tags" ("tag_id");
