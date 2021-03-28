/* Insertion script for first users */

/*** using pgcrypto to encrypt our password
/* using gen_salt function with blowfish algorithm 
/* which is the best algorithm supported by crypt() function 
***/
CREATE EXTENSION pgcrypto;

INSERT INTO users (
    username,
    email,
    password
)
VALUES
    (
        'superuser',
        'superuser@email.com',
        crypt('superuserpassword', gen_salt('bf'))
    ),
    (
        'toto',
        'toto@france.fr',
        crypt('totopassword', gen_salt('bf'))
    ),
    (
        'belette',
        'belette@live.live',
        crypt('belettepassword', gen_salt('bf'))
    );