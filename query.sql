CREATE TABLE categorie(
    id INT PRIMARY KEY auto_increment NOT NULL,
    nom VARCHAR(255)
)

CREATE TABLE produit (
    id INT PRIMARY KEY auto_increment NOT NULL,
    nom VARCHAR(255),
    description VARCHAR(255),
    prix INT,
    quantité INT,
    id_categorie INT,
    CONSTRAINT FK_categ FOREIGN KEY (id_categorie) REFERENCES categorie(id)
)

INSERT INTO categorie (nom) VALUES ("Alimentaire"); #1
INSERT INTO categorie (nom) VALUES ("Santé"); #2
INSERT INTO categorie (nom) VALUES ("Sport"); #3
INSERT INTO categorie (nom) VALUES ("Electronique");#4

INSERT INTO produit (nom,description,prix,quantité,id_categorie) VALUES ("Haltères","Haltères Decathlon",35,2,3);
INSERT INTO produit (nom,description,prix,quantité,id_categorie) VALUES ("PC Portable","PC Portable Asos",540,1,4);
INSERT INTO produit (nom,description,prix,quantité,id_categorie) VALUES ("Steak Haché","Steak Haché 100grammes",10,1,1);
INSERT INTO produit (nom,description,prix,quantité,id_categorie) VALUES ("Ballon de foot","Ballon Adidas",40,1,3);

