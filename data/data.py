#########################################################################
#					        DATA FOR THE PROJECT						                      #
#########################################################################

## domain: artists, actors, films, directors, ect,
domain = ['Kheiron Tabib', 'Anglade Jean-Hughes', 'Annaud Jean-Jacques', 'Arestrup Niels', 'Arquette Rosanna', 'Audiard Jacques', 'Balasko Josiane', 'Baldwin Adam', 'Bale Christian', 'Bardem Javier', 'Barr Jean-Marc', 'Bart Emmanuelle', 'Bench Judi', 'Bening Anette', 'Berenson Marisa', 'Bergman Ingrid', 'Besson Luc', 'Blanc Michel', 'Bracco Lorraine', 'Brando Marlon', 'Broderick Matthew', 'Brolin Josh', 'Bullock Sandra', 'Bunker Edward', 'Burton Tim', 'Buscemi Steve', 'Caan Jamees', 'Caan James', 'Cage Nicolas', 'Caine Michael', 'Cameron James', 'Campbell Martin', 'Caroll Madeleine', 'Carradine David', 'Caruso David', 'Cassel Vincent', 'Chabrol Claude', 'Clavier Christian', 'Coen Ethan', 'Collette Tony', 'Connery Sean', 'Coppola Francis Ford', 'Coppola Sofia', 'Costner Kevin', 'Cotillard Marion', 'Craig Daniel', 'Crowe Russel', 'Crowe Russell', 'Cruise Tom', 'Damon Matt', 'Day Doris', 'De Funs Louis', 'De Niro Robert', 'De Palma Brian', 'Demme Jonathan', 'Deneuve Catherine', 'Departieu Gérard', 'Depp Johnny', 'Dern Laura', 'DiCaprio Leonardo', 'Diaz Cameron', 'Dillon Mat', 'Donat Robert', 'Douglas Kirk', 'Dreyfus Richard', 'Dullea Keir', 'Dunaway Fane', 'Dunst Kirsten', 'Dutronc Jacques', 'Duvall Robert', 'Eastwood Clint', 'Emmerich Roland', 'Farrelly Bobby', 'Fassbender Michael', 'Ferrara Abel', 'Fiennes Ralph', 'Fincher David', 'Fishburne Laurence', 'Fisher Carrie', 'Fleischer Richard ', 'Fonda Bridget', 'Fontaine Joan', 'Ford Harrison', 'Ford John', 'Foster Jodie', 'Foxx Jamie', 'Freeman Morgan', 'Furlong Edward', 'Galabru Michel', 'Gallo Vincent', 'Garcia Andy', 'Gilliam Terry', 'Girault Jean', 'Goldblum Jeff', 'Grant Cary', 'Gray James', 'Green Eva', 'Grier Pam', 'Gudmundsdottir Bjork', 'Gyllenhaal Maggie', 'Hackman Gene', 'Hamill Mark', 'Hanks Tom', 'Hannah Daryl', 'Harlin Renny', 'Harris Ed', 'Hathaway Anne', 'Hauer Rutger', 'Hayden Sterling', 'Hedren Tippi', 'Hestone Charlton ', 'Hitchcock Alfred', 'Hoffman Dustin', 'Holm Ian', 'Hopkins Anthony', 'Huppert Isabelle', 'Jackson Samuel', 'Jackson Samuel L.', 'Jones Tommy Lee', 'Jovovich Milla', 'Karyo Tchky', 'Kassowitz Matthieu', 'Keaton Diane', 'Keaton Michael', 'Keitel Harvey', 'Kelly Grace', 'Kidman Nicole', 'Kilmer Val', 'Kubrick Stanley', 'Kurozawa Akira', 'Lanvin Grard', 'Laurent Mélanie', 'Lavanant Dominique', 'Leconte Patrice', 'Ledger Heath', 'Leigh Janet', 'Leighton Eric', 'Leone Sergio', 'Levinson Barry', 'Lhermite Thierry', 'Linney Laura', 'Liotta Ray', 'Liu Lucy', 'Lockwood Gary', 'Léaud Jean-Pierre', 'Macy William', 'Madsen Michael', 'Maguire Tobey', 'Malkovitch John', 'Mann Michael', 'Marquand Richard', 'Mason James', 'McConaughey Mathew', 'McDowell Macolm', 'McGillis Kelly', 'McTierman John', 'Mendes Sam', 'Miles Vera', 'Milland Ray', 'Modine Matthew', 'Moss Carie-Anne', 'Moss Carrie-Anne', 'Mouglalis Anna', 'Neeson Liam', 'Nicholson Jack', 'Nolan Christopher', 'Novak Kim', 'O\'Hara Maureen', 'O\'Neal Ryan', 'Oldman Gary', 'Olivier Laurence', 'Osment Haley Joel', 'Pacino Al', 'Page Elen', 'Parillaud Anne', 'Pearce Guy', 'Penn Chris', 'Perkins Anthony', 'Pesci Joe', 'Pfeiffer Michelle', 'Phoenix Joaquin', 'Pialat Maurice', 'Pitt Brad', 'Plummer Christopher', 'Poiret Jean', 'Portman Natalie', 'Rahim Tahar', 'Raimi Sam', 'Rains Claude', 'Redgrave Vanessa', 'Reeves Keanu', 'Reno Jean', 'Ricci Christina', 'Rosselini Isabella', 'Roth Tim', 'Saint Eva Marie', 'Sanders George', 'Scheider Roy', 'Schwartzenegger Arnold', 'Sciora Annabella', 'Scorcese Martin', 'Scott George', 'Scott Ridley', 'Scott Tony', 'Sellers Peter', 'Shaw Robert', 'Shyamalan M. Night', 'Sizemore Tom', 'Slater Christian', 'Snipes Wesley', 'Spacey Kevin', 'Spielberg Steven', 'Stewart James', 'Stone Sharon', 'Swank Hillary', 'Tarantino Quentin', 'Tarkovski Andrei', 'Taylor Rod', 'Theron Charlize', 'Thurman Uma', 'Travolta John', 'Truffaut François', 'Van Cleef Lee', 'Villeret Jacques', 'Voight John', 'Volonte Gian Maria', 'Wachowski Andy', 'Wahlberg Mark', 'Walken Christopher', 'Waltz Christoph', 'Wayne John', 'Weaver Sigourney', 'Weaving Hugo', 'Willis Bruce', 'Winslet Kate', 'Woo John', 'von Trier Lars', 'Vertigo', 'Alien', 'Titanic', 'Sacrifice', 'Volte/Face', 'Sleepy Hollow', 'American Beauty', 'Impitoyable', 'Gladiator', 'Blade Runner', 'Piège de cristal', '58 minutes pour vivre', 'Van Gogh', 'Seven', 'L\'armée des douze singes', 'Le nom de la rose', 'Pulp fiction', 'Mary à tout prix', 'Terminator', 'Les dents de la mer', 'Le silence des agneaux', 'Godzilla', 'Matrix', 'Mission: Impossible', 'Kagemusha', 'Les pleins pouvoirs', 'Le gendarme et les extra-terrestres', 'Le monde perdu', 'Rain Man', 'Top Gun', 'Les bronzés font du ski', 'Le bon, la brute et le truand', 'Psychose', 'Le retour du Jedi', 'Les oiseaux', 'Reservoir dogs', 'Eyes Wide Shut', 'Shining', 'Pas de printemps pour Marnie', 'Fenêtre sur cour', 'La mort aux trousses', 'Jeanne d\'Arc', 'Le cinquième élément', 'Léon', 'Nikita', 'Le grand bleu', 'Spider-Man', 'King of New York', 'The Matrix reloaded', 'The Matrix Revolutions', 'De bruit et de fureur', 'Usual suspects', 'Bad Lieutenant', 'Le parrain', 'Le parrain II', 'Le parrain III', 'Jackie Brown', 'Une journée en enfer', 'Sixième sens', 'Lost in Translation', 'Kill Bill', 'Stalingrad', 'Million Dollar Baby', 'Pour quelques dollars de plus', 'Marie Antoinette', 'Soleil vert', 'Heat', 'Taxi driver', 'Les affranchis', 'Casino', 'Casino Royale', 'Skyfall', 'No country for old men', 'Fargo', 'Django unchained', 'Inglourious Basterds', 'Inglourious Basterds', 'Les quatre cents coups', 'Le dernier métro', 'Rio Grande', 'Interstellar', 'Inception', 'Memento', 'Batman begins', 'The Dark Knight', 'The Dark Knight Rises', 'Un prophète', 'Nous trois ou rien']

## set of actors
actors = ["Anglade Jean-Hughes", "Arestrup Niels", "Arquette Rosanna", "Balasko Josiane", "Baldwin Adam", "Bale Christian", "Bardem Javier", "Barr Jean-Marc", "Bart Emmanuelle", "Bench Judi", "Bening Anette", "Berenson Marisa", "Blanc Michel", "Bracco Lorraine", "Brando Marlon", "Broderick Matthew", "Brolin Josh", "Bunker Edward", "Buscemi Steve", "Caan James", "Cage Nicolas", "Caine Michael", "Carradine David", "Cassel Vincent", "Clavier Christian", "Collette Tony", "Connery Sean", "Coppola Sofia", "Costner Kevin", "Cotillard Marion", "Craig Daniel", "Crowe Russel", "Crowe Russell", "Cruise Tom", "Damon Matt", "De Funs Louis", "De Niro Robert", "Deneuve Catherine", "Departieu Gérard", "Depp Johnny", "DiCaprio Leonardo", "Diaz Cameron", "Dillon Mat", "Dreyfus Richard", "Dunaway Fane", "Dunst Kirsten", "Dutronc Jacques", "Duvall Robert", "Eastwood Clint", "Fassbender Michael", "Fishburne Laurence", "Fisher Carrie", "Fonda Bridget", "Ford Harrison", "Foster Jodie", "Foxx Jamie", "Freeman Morgan", "Galabru Michel", "Gallo Vincent", "Garcia Andy", "Goldblum Jeff", "Grant Cary", "Green Eva", "Grier Pam", "Gyllenhaal Maggie", "Hackman Gene", "Hamill Mark", "Hanks Tom", "Hannah Daryl", "Harris Ed", "Hathaway Anne", "Hauer Rutger", "Hayden Sterling", "Hedren Tippi", "Hestone Charlton ", "Hoffman Dustin", "Holm Ian", "Hopkins Anthony", "Huppert Isabelle", "Jackson Samuel", "Jackson Samuel L.", "Jones Tommy Lee", "Jovovich Milla", "Karyo Tchky", "Kassowitz Matthieu", "Keaton Diane", "Keaton Michael", "Keitel Harvey", "Kidman Nicole", "Kilmer Val", "Laurent Mélanie", "Lavanant Dominique", "Ledger Heath", "Leigh Janet", "Leighton Eric", "Lhermite Thierry", "Liotta Ray", "Liu Lucy", "Léaud Jean-Pierre", "Macy William", "Madsen Michael", "Malkovitch John", "Mann Michael", "Mason James", "McConaughey Mathew", "McGillis Kelly", "Miles Vera", "Modine Matthew", "Moss Carie-Anne", "Moss Carrie-Anne", "Mouglalis Anna", "Neeson Liam", "Nicholson Jack", "Novak Kim", "O'Hara Maureen", "O'Neal Ryan", "Oldman Gary", "Pacino Al", "Page Elen", "Parillaud Anne", "Pearce Guy", "Penn Chris", "Perkins Anthony", "Pesci Joe", "Pitt Brad", "Poiret Jean", "Portman Natalie", "Rahim Tahar", "Reeves Keanu", "Reno Jean", "Ricci Christina", "Rosselini Isabella", "Roth Tim", "Saint Eva Marie", "Scheider Roy", "Schwartzenegger Arnold", "Sciora Annabella", "Shaw Robert", "Shyamalan M. Night", "Sizemore Tom", "Slater Christian", "Snipes Wesley", "Spacey Kevin", "Stewart James", "Stone Sharon", "Swank Hillary", "Tarantino Quentin", "Taylor Rod", "Theron Charlize", "Thurman Uma", "Travolta John", "Voight John", "Wahlberg Mark", "Walken Christopher", "Waltz Christoph", "Wayne John", "Weaver Sigourney", "Weaving Hugo", "Willis Bruce", "Winslet Kate", "von Trier Lars"]

## set of artists
artists = ["Kheiron Tabib", "Anglade Jean-Hughes", "Annaud Jean-Jacques", "Arestrup Niels", "Arquette Rosanna", "Audiard Jacques", "Balasko Josiane", "Baldwin Adam", "Bale Christian", "Bardem Javier", "Barr Jean-Marc", "Bart Emmanuelle", "Bench Judi", "Bening Anette", "Berenson Marisa", "Bergman Ingrid", "Besson Luc", "Blanc Michel", "Bracco Lorraine", "Brando Marlon", "Broderick Matthew", "Brolin Josh", "Bullock Sandra", "Bunker Edward", "Burton Tim", "Buscemi Steve", "Caan Jamees", "Caan James", "Cage Nicolas", "Caine Michael", "Cameron James", "Campbell Martin", "Caroll Madeleine", "Carradine David", "Caruso David", "Cassel Vincent", "Chabrol Claude", "Clavier Christian", "Coen Ethan", "Collette Tony", "Connery Sean", "Coppola Francis Ford", "Coppola Sofia", "Costner Kevin", "Cotillard Marion", "Craig Daniel", "Crowe Russel", "Crowe Russell", "Cruise Tom", "Damon Matt", "Day Doris", "De Funs Louis", "De Niro Robert", "De Palma Brian", "Demme Jonathan", "Deneuve Catherine", "Departieu Gérard", "Depp Johnny", "Dern Laura", "DiCaprio Leonardo", "Diaz Cameron", "Dillon Mat", "Donat Robert", "Douglas Kirk", "Dreyfus Richard", "Dullea Keir", "Dunaway Fane", "Dunst Kirsten", "Dutronc Jacques", "Duvall Robert", "Eastwood Clint", "Emmerich Roland", "Farrelly Bobby", "Fassbender Michael", "Ferrara Abel", "Fiennes Ralph", "Fincher David", "Fishburne Laurence", "Fisher Carrie", "Fleischer Richard ", "Fonda Bridget", "Fontaine Joan", "Ford Harrison", "Ford John", "Foster Jodie", "Foxx Jamie", "Freeman Morgan", "Furlong Edward", "Galabru Michel", "Gallo Vincent", "Garcia Andy", "Gilliam Terry", "Girault Jean", "Goldblum Jeff", "Grant Cary", "Gray James", "Green Eva", "Grier Pam", "Gudmundsdottir Bjork", "Gyllenhaal Maggie", "Hackman Gene", "Hamill Mark", "Hanks Tom", "Hannah Daryl", "Harlin Renny", "Harris Ed", "Hathaway Anne", "Hauer Rutger", "Hayden Sterling", "Hedren Tippi", "Hestone Charlton ", "Hitchcock Alfred", "Hoffman Dustin", "Holm Ian", "Hopkins Anthony", "Huppert Isabelle", "Jackson Samuel", "Jackson Samuel L.", "Jones Tommy Lee", "Jovovich Milla", "Karyo Tchky", "Kassowitz Matthieu", "Keaton Diane", "Keaton Michael", "Keitel Harvey", "Kelly Grace", "Kidman Nicole", "Kilmer Val", "Kubrick Stanley", "Kurozawa Akira", "Lanvin Grard", "Laurent Mélanie", "Lavanant Dominique", "Leconte Patrice", "Ledger Heath", "Leigh Janet", "Leighton Eric", "Leone Sergio", "Levinson Barry", "Lhermite Thierry", "Linney Laura", "Liotta Ray", "Liu Lucy", "Lockwood Gary", "Léaud Jean-Pierre", "Macy William", "Madsen Michael", "Maguire Tobey", "Malkovitch John", "Mann Michael", "Marquand Richard", "Mason James", "McConaughey Mathew", "McDowell Macolm", "McGillis Kelly", "McTierman John", "Mendes Sam", "Miles Vera", "Milland Ray", "Modine Matthew", "Moss Carie-Anne", "Moss Carrie-Anne", "Mouglalis Anna", "Neeson Liam", "Nicholson Jack", "Nolan Christopher", "Novak Kim", "O'Hara Maureen", "O'Neal Ryan", "Oldman Gary", "Olivier Laurence", "Osment Haley Joel", "Pacino Al", "Page Elen", "Parillaud Anne", "Pearce Guy", "Penn Chris", "Perkins Anthony", "Pesci Joe", "Pfeiffer Michelle", "Phoenix Joaquin", "Pialat Maurice", "Pitt Brad", "Plummer Christopher", "Poiret Jean", "Portman Natalie", "Rahim Tahar", "Raimi Sam", "Rains Claude", "Redgrave Vanessa", "Reeves Keanu", "Reno Jean", "Ricci Christina", "Rosselini Isabella", "Roth Tim", "Saint Eva Marie", "Sanders George", "Scheider Roy", "Schwartzenegger Arnold", "Sciora Annabella", "Scorcese Martin", "Scott George", "Scott Ridley", "Scott Tony", "Sellers Peter", "Shaw Robert", "Shyamalan M. Night", "Sizemore Tom", "Slater Christian", "Snipes Wesley", "Spacey Kevin", "Spielberg Steven", "Stewart James", "Stone Sharon", "Swank Hillary", "Tarantino Quentin", "Tarkovski Andrei", "Taylor Rod", "Theron Charlize", "Thurman Uma", "Travolta John", "Truffaut François", "Van Cleef Lee", "Villeret Jacques", "Voight John", "Volonte Gian Maria", "Wachowski Andy", "Wahlberg Mark", "Walken Christopher", "Waltz Christoph", "Wayne John", "Weaver Sigourney", "Weaving Hugo", "Willis Bruce", "Winslet Kate", "Woo John", "von Trier Lars"]

## set of movies
films = ["Vertigo", "Alien", "Titanic", "Sacrifice", "Volte/Face", "Sleepy Hollow", "American Beauty", "Impitoyable", "Gladiator", "Blade Runner", "Piège de cristal", "58 minutes pour vivre", "Van Gogh", "Seven", "L'armée des douze singes", "Le nom de la rose", "Pulp fiction", "Mary à tout prix", "Terminator", "Les dents de la mer", "Le silence des agneaux", "Godzilla", "Matrix", "Mission: Impossible", "Kagemusha", "Les pleins pouvoirs", "Le gendarme et les extra-terrestres", "Le monde perdu", "Rain Man", "Top Gun", "Les bronzés font du ski", "Le bon, la brute et le truand", "Psychose", "Le retour du Jedi", "Les oiseaux", "Reservoir dogs", "Eyes Wide Shut", "Shining", "Pas de printemps pour Marnie", "Fenêtre sur cour", "La mort aux trousses", "Jeanne d'Arc", "Le cinquième élément", "Léon", "Nikita", "Le grand bleu", "Spider-Man", "King of New York", "The Matrix reloaded", "The Matrix Revolutions", "De bruit et de fureur", "Usual suspects", "Bad Lieutenant", "Le parrain", "Le parrain II", "Le parrain III", "Jackie Brown", "Une journée en enfer", "Sixième sens", "Lost in Translation", "Kill Bill", "Stalingrad", "Million Dollar Baby", "Pour quelques dollars de plus", "Marie Antoinette", "Soleil vert", "Heat", "Taxi driver", "Les affranchis", "Casino", "Casino Royale", "Skyfall", "No country for old men", "Fargo", "Django unchained", "Inglourious Basterds", "Inglourious Basterds", "Les quatre cents coups", "Le dernier métro", "Rio Grande", "Interstellar", "Inception", "Memento", "Batman begins", "The Dark Knight", "The Dark Knight Rises", "Un prophète", "Nous trois ou rien"]

## the fil directors
film_director = ["Kheiron Tabib", "Annaud Jean-Jacques", "Audiard Jacques", "Besson Luc", "Burton Tim", "Cameron James", "Campbell Martin", "Chabrol Claude", "Coen Ethan", "Coppola Francis Ford", "Coppola Sofia", "De Palma Brian", "Demme Jonathan", "Dern Laura", "Eastwood Clint", "Emmerich Roland", "Farrelly Bobby", "Ferrara Abel", "Fincher David", "Fleischer Richard ", "Ford John", "Gilliam Terry", "Girault Jean", "Grier Pam", "Harlin Renny", "Hitchcock Alfred", "Keaton Michael", "Kubrick Stanley", "Kurozawa Akira", "Leconte Patrice", "Leone Sergio", "Levinson Barry", "Mann Michael", "Marquand Richard", "McTierman John", "Mendes Sam", "Nolan Christopher", "Osment Haley Joel", "Phoenix Joaquin", "Pialat Maurice", "Raimi Sam", "Scorcese Martin", "Scott Ridley", "Scott Tony", "Spielberg Steven", "Tarantino Quentin", "Tarkovski Andrei", "Truffaut François", "Wachowski Andy", "Woo John"]

## acts: (actor, film)
acts = [("Novak Kim", "Vertigo"), ("Stewart James", "Vertigo"), ("Weaver Sigourney", "Alien"), ("DiCaprio Leonardo", "Titanic"), ("Winslet Kate", "Titanic"), ("Cage Nicolas", "Volte/Face"), ("Travolta John", "Volte/Face"), ("Depp Johnny", "Sleepy Hollow"), ("Ricci Christina", "Sleepy Hollow"), ("Walken Christopher", "Sleepy Hollow"), ("Bening Anette", "American Beauty"), ("Spacey Kevin", "American Beauty"), ("Eastwood Clint", "Impitoyable"), ("Freeman Morgan", "Impitoyable"), ("Hackman Gene", "Impitoyable"), ("Baldwin Adam", "Gladiator"), ("Berenson Marisa", "Gladiator"), ("Crowe Russell", "Gladiator"), ("O'Neal Ryan", "Gladiator"), ("Ford Harrison", "Blade Runner"), ("Hauer Rutger", "Blade Runner"), ("Willis Bruce", "Piège de cristal"), ("Willis Bruce", "58 minutes pour vivre"), ("Dutronc Jacques", "Van Gogh"), ("Freeman Morgan", "Seven"), ("Pitt Brad", "Seven"), ("Spacey Kevin", "Seven"), ("Willis Bruce", "L'armée des douze singes"), ("Connery Sean", "Le nom de la rose"), ("Slater Christian", "Le nom de la rose"), ("Arquette Rosanna", "Pulp fiction"), ("Jackson Samuel L.", "Pulp fiction"), ("Keitel Harvey", "Pulp fiction"), ("Roth Tim", "Pulp fiction"), ("Tarantino Quentin", "Pulp fiction"), ("Thurman Uma", "Pulp fiction"), ("Travolta John", "Pulp fiction"), ("Walken Christopher", "Pulp fiction"), ("Willis Bruce", "Pulp fiction"), ("Diaz Cameron", "Mary à tout prix"), ("Dillon Mat", "Mary à tout prix"), ("Schwartzenegger Arnold", "Terminator"), ("Dreyfus Richard", "Les dents de la mer"), ("Scheider Roy", "Les dents de la mer"), ("Shaw Robert", "Les dents de la mer"), ("Foster Jodie", "Le silence des agneaux"), ("Hopkins Anthony", "Le silence des agneaux"), ("Broderick Matthew", "Godzilla"), ("Reno Jean", "Godzilla"), ("Fishburne Laurence", "Matrix"), ("Reeves Keanu", "Matrix"), ("Bart Emmanuelle", "Mission: Impossible"), ("Cruise Tom", "Mission: Impossible"), ("Reno Jean", "Mission: Impossible"), ("Voight John", "Mission: Impossible"), ("Eastwood Clint", "Les pleins pouvoirs"), ("Hackman Gene", "Les pleins pouvoirs"), ("Harris Ed", "Les pleins pouvoirs"), ("De Funs Louis", "Le gendarme et les extra-terrestres"), ("Galabru Michel", "Le gendarme et les extra-terrestres"), ("Goldblum Jeff", "Le monde perdu"), ("Cruise Tom", "Rain Man"), ("Hoffman Dustin", "Rain Man"), ("Cruise Tom", "Top Gun"), ("Kilmer Val", "Top Gun"), ("McGillis Kelly", "Top Gun"), ("Balasko Josiane", "Les bronzés font du ski"), ("Blanc Michel", "Les bronzés font du ski"), ("Clavier Christian", "Les bronzés font du ski"), ("Lavanant Dominique", "Les bronzés font du ski"), ("Lhermite Thierry", "Les bronzés font du ski"), ("Eastwood Clint", "Le bon, la brute et le truand"), ("Leigh Janet", "Psychose"), ("Miles Vera", "Psychose"), ("Perkins Anthony", "Psychose"), ("Fisher Carrie", "Le retour du Jedi"), ("Ford Harrison", "Le retour du Jedi"), ("Hamill Mark", "Le retour du Jedi"), ("Hedren Tippi", "Les oiseaux"), ("Taylor Rod", "Les oiseaux"), ("Bunker Edward", "Reservoir dogs"), ("Buscemi Steve", "Reservoir dogs"), ("Keitel Harvey", "Reservoir dogs"), ("Madsen Michael", "Reservoir dogs"), ("Penn Chris", "Reservoir dogs"), ("Roth Tim", "Reservoir dogs"), ("Tarantino Quentin", "Reservoir dogs"), ("Cruise Tom", "Eyes Wide Shut"), ("Kidman Nicole", "Eyes Wide Shut"), ("Nicholson Jack", "Shining"), ("Connery Sean", "Pas de printemps pour Marnie"), ("Hedren Tippi", "Pas de printemps pour Marnie"), ("Grant Cary", "La mort aux trousses"), ("Mason James", "La mort aux trousses"), ("Saint Eva Marie", "La mort aux trousses"), ("Dunaway Fane", "Jeanne d'Arc"), ("Hoffman Dustin", "Jeanne d'Arc"), ("Jovovich Milla", "Jeanne d'Arc"), ("Karyo Tchky", "Jeanne d'Arc"), ("Malkovitch John", "Jeanne d'Arc"), ("Holm Ian", "Le cinquième élément"), ("Jovovich Milla", "Le cinquième élément"), ("Oldman Gary", "Le cinquième élément"), ("Willis Bruce", "Le cinquième élément"), ("Oldman Gary", "Léon"), ("Portman Natalie", "Léon"), ("Reno Jean", "Léon"), ("Anglade Jean-Hughes", "Nikita"), ("Karyo Tchky", "Nikita"), ("Parillaud Anne", "Nikita"), ("Arquette Rosanna", "Le grand bleu"), ("Barr Jean-Marc", "Le grand bleu"), ("Reno Jean", "Le grand bleu"), ("Gallo Vincent", "Spider-Man"), ("Rosselini Isabella", "Spider-Man"), ("Sciora Annabella", "Spider-Man"), ("Snipes Wesley", "Spider-Man"), ("von Trier Lars", "Spider-Man"), ("Buscemi Steve", "King of New York"), ("Cassel Vincent", "King of New York"), ("Fishburne Laurence", "King of New York"), ("Kassowitz Matthieu", "King of New York"), ("Snipes Wesley", "King of New York"), ("Walken Christopher", "King of New York"), ("Fishburne Laurence", "The Matrix reloaded"), ("Moss Carrie-Anne", "The Matrix reloaded"), ("Reeves Keanu", "The Matrix reloaded"), ("Weaving Hugo", "The Matrix reloaded"), ("Caan James", "The Matrix Revolutions"), ("Fishburne Laurence", "The Matrix Revolutions"), ("Reeves Keanu", "The Matrix Revolutions"), ("Theron Charlize", "The Matrix Revolutions"), ("Wahlberg Mark", "The Matrix Revolutions"), ("Costner Kevin", "De bruit et de fureur"), ("Huppert Isabelle", "De bruit et de fureur"), ("Mouglalis Anna", "De bruit et de fureur"), ("Damon Matt", "Usual suspects"), ("Hanks Tom", "Usual suspects"), ("Modine Matthew", "Usual suspects"), ("Sizemore Tom", "Usual suspects"), ("Spacey Kevin", "Usual suspects"), ("Keitel Harvey", "Bad Lieutenant"), ("Brando Marlon", "Le parrain"), ("Caan James", "Le parrain"), ("Duvall Robert", "Le parrain"), ("Hayden Sterling", "Le parrain"), ("Keaton Diane", "Le parrain"), ("Pacino Al", "Le parrain"), ("De Niro Robert", "Le parrain II"), ("Duvall Robert", "Le parrain II"), ("Keaton Diane", "Le parrain II"), ("Pacino Al", "Le parrain II"), ("Coppola Sofia", "Le parrain III"), ("Garcia Andy", "Le parrain III"), ("Keaton Diane", "Le parrain III"), ("Pacino Al", "Le parrain III"), ("De Niro Robert", "Jackie Brown"), ("Fonda Bridget", "Jackie Brown"), ("Grier Pam", "Jackie Brown"), ("Jackson Samuel", "Jackie Brown"), ("Keaton Michael", "Jackie Brown"), ("Fonda Bridget", "Une journée en enfer"), ("Jackson Samuel L.", "Une journée en enfer"), ("Willis Bruce", "Une journée en enfer"), ("Shyamalan M. Night", "Sixième sens"), ("Willis Bruce", "Sixième sens"), ("Collette Tony", "Lost in Translation"), ("Crowe Russel", "Lost in Translation"), ("Leighton Eric", "Lost in Translation"), ("Mann Michael", "Lost in Translation"), ("Pacino Al", "Lost in Translation"), ("Carradine David", "Kill Bill"), ("Hannah Daryl", "Kill Bill"), ("Liu Lucy", "Kill Bill"), ("Madsen Michael", "Kill Bill"), ("Thurman Uma", "Kill Bill"), ("Brando Marlon", "Stalingrad"), ("Keaton Diane", "Stalingrad"), ("Eastwood Clint", "Million Dollar Baby"), ("Freeman Morgan", "Million Dollar Baby"), ("Swank Hillary", "Million Dollar Baby"), ("Dunst Kirsten", "Marie Antoinette"), ("Hestone Charlton ", "Soleil vert"), ("De Niro Robert", "Heat"), ("De Niro Robert", "Taxi driver"), ("Foster Jodie", "Taxi driver"), ("Bracco Lorraine", "Les affranchis"), ("De Niro Robert", "Les affranchis"), ("Liotta Ray", "Les affranchis"), ("Pesci Joe", "Les affranchis"), ("De Niro Robert", "Casino"), ("Pesci Joe", "Casino"), ("Stone Sharon", "Casino"), ("Craig Daniel", "Casino Royale"), ("Green Eva", "Casino Royale"), ("Bardem Javier", "Skyfall"), ("Bench Judi", "Skyfall"), ("Craig Daniel", "Skyfall"), ("Bardem Javier", "No country for old men"), ("Brolin Josh", "No country for old men"), ("Jones Tommy Lee", "No country for old men"), ("Buscemi Steve", "Fargo"), ("Macy William", "Fargo"), ("DiCaprio Leonardo", "Django unchained"), ("Foxx Jamie", "Django unchained"), ("Jackson Samuel", "Django unchained"), ("Waltz Christoph", "Django unchained"), ("Fassbender Michael", "Inglourious Basterds"), ("Laurent Mélanie", "Inglourious Basterds"), ("Pitt Brad", "Inglourious Basterds"), ("Waltz Christoph", "Inglourious Basterds"), ("Léaud Jean-Pierre", "Les quatre cents coups"), ("Deneuve Catherine", "Le dernier métro"), ("Departieu Gérard", "Le dernier métro"), ("Poiret Jean", "Le dernier métro"), ("O'Hara Maureen", "Rio Grande"), ("Wayne John", "Rio Grande"), ("Caine Michael", "Interstellar"), ("Hathaway Anne", "Interstellar"), ("McConaughey Mathew", "Interstellar"), ("Caine Michael", "Inception"), ("Cotillard Marion", "Inception"), ("DiCaprio Leonardo", "Inception"), ("Page Elen", "Inception"), ("Moss Carie-Anne", "Memento"), ("Pearce Guy", "Memento"), ("Bale Christian", "Batman begins"), ("Caine Michael", "Batman begins"), ("Freeman Morgan", "Batman begins"), ("Neeson Liam", "Batman begins"), ("Oldman Gary", "Batman begins"), ("Bale Christian", "The Dark Knight"), ("Caine Michael", "The Dark Knight"), ("Freeman Morgan", "The Dark Knight"), ("Gyllenhaal Maggie", "The Dark Knight"), ("Ledger Heath", "The Dark Knight"), ("Oldman Gary", "The Dark Knight"), ("Bale Christian", "The Dark Knight Rises"), ("Caine Michael", "The Dark Knight Rises"), ("Cotillard Marion", "The Dark Knight Rises"), ("Freeman Morgan", "The Dark Knight Rises"), ("Hathaway Anne", "The Dark Knight Rises"), ("Oldman Gary", "The Dark Knight Rises"), ("Arestrup Niels", "Un prophète"), ("Rahim Tahar", "Un prophète")]

## directs: (director, film)
directs = [("Hitchcock Alfred", "Vertigo"), ("Scott Ridley", "Alien"), ("Cameron James", "Titanic"), ("Tarkovski Andrei", "Sacrifice"), ("Woo John", "Volte/Face"), ("Burton Tim", "Sleepy Hollow"), ("Mendes Sam", "American Beauty"), ("Eastwood Clint", "Impitoyable"), ("Scott Ridley", "Gladiator"), ("Scott Ridley", "Blade Runner"), ("McTierman John", "Piège de cristal"), ("Harlin Renny", "58 minutes pour vivre"), ("Pialat Maurice", "Van Gogh"), ("Fincher David", "Seven"), ("Gilliam Terry", "L'armée des douze singes"), ("Annaud Jean-Jacques", "Le nom de la rose"), ("Tarantino Quentin", "Pulp fiction"), ("Farrelly Bobby", "Mary à tout prix"), ("Cameron James", "Terminator"), ("Spielberg Steven", "Les dents de la mer"), ("Demme Jonathan", "Le silence des agneaux"), ("Emmerich Roland", "Godzilla"), ("Wachowski Andy", "Matrix"), ("De Palma Brian", "Mission: Impossible"), ("Kurozawa Akira", "Kagemusha"), ("Eastwood Clint", "Les pleins pouvoirs"), ("Girault Jean", "Le gendarme et les extra-terrestres"), ("Spielberg Steven", "Le monde perdu"), ("Levinson Barry", "Rain Man"), ("Scott Tony", "Top Gun"), ("Leconte Patrice", "Les bronzés font du ski"), ("Leone Sergio", "Le bon, la brute et le truand"), ("Hitchcock Alfred", "Psychose"), ("Marquand Richard", "Le retour du Jedi"), ("Hitchcock Alfred", "Les oiseaux"), ("Tarantino Quentin", "Reservoir dogs"), ("Kubrick Stanley", "Eyes Wide Shut"), ("Kubrick Stanley", "Shining"), ("Hitchcock Alfred", "Pas de printemps pour Marnie"), ("Hitchcock Alfred", "Fenêtre sur cour"), ("Hitchcock Alfred", "La mort aux trousses"), ("Besson Luc", "Jeanne d'Arc"), ("Besson Luc", "Le cinquième élément"), ("Besson Luc", "Léon"), ("Besson Luc", "Nikita"), ("Besson Luc", "Le grand bleu"), ("Raimi Sam", "Spider-Man"), ("Ferrara Abel", "King of New York"), ("Wachowski Andy", "The Matrix reloaded"), ("Phoenix Joaquin", "The Matrix Revolutions"), ("Chabrol Claude", "De bruit et de fureur"), ("Dern Laura", "Usual suspects"), ("Ferrara Abel", "Bad Lieutenant"), ("Coppola Francis Ford", "Le parrain"), ("Coppola Francis Ford", "Le parrain II"), ("Coppola Francis Ford", "Le parrain III"), ("Tarantino Quentin", "Jackie Brown"), ("Grier Pam", "Une journée en enfer"), ("Keaton Michael", "Sixième sens"), ("Osment Haley Joel", "Lost in Translation"), ("Tarantino Quentin", "Kill Bill"), ("Annaud Jean-Jacques", "Stalingrad"), ("Eastwood Clint", "Million Dollar Baby"), ("Leone Sergio", "Pour quelques dollars de plus"), ("Coppola Sofia", "Marie Antoinette"), ("Fleischer Richard ", "Soleil vert"), ("Mann Michael", "Heat"), ("Scorcese Martin", "Taxi driver"), ("Scorcese Martin", "Les affranchis"), ("Scorcese Martin", "Casino"), ("Campbell Martin", "Casino Royale"), ("Mendes Sam", "Skyfall"), ("Coen Ethan", "No country for old men"), ("Coen Ethan", "Fargo"), ("Tarantino Quentin", "Django unchained"), ("Tarantino Quentin", "Inglourious Basterds"), ("Truffaut François", "Les quatre cents coups"), ("Truffaut François", "Le dernier métro"), ("Ford John", "Rio Grande"), ("Nolan Christopher", "Interstellar"), ("Nolan Christopher", "Inception"), ("Nolan Christopher", "Memento"), ("Nolan Christopher", "Batman begins"), ("Nolan Christopher", "The Dark Knight"), ("Nolan Christopher", "The Dark Knight Rises"), ("Audiard Jacques", "Un prophète"), (" Kheiron Tabib", "Nous trois ou rien")]

