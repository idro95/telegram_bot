import telepot

token = '626034314:AAELt98p2dq6bvkknIRQ9ROgwl5zojVgPMM'

SegreSG = telepot.Bot(token)
print(SegreSG.getMe())

VISITORS = {}
PLACES = {'/1':['Spagna'], '/2':['Popolo'], '/3':['Augusto'], '/4':['Pantheon'], '/5':['Trevi']}


if SegreSG.getUpdates()==[]:
    last = 0
else:
    last = SegreSG.getUpdates()[-1]['update_id'] #in case of old messages

metroSpagna = """Prendi la metro A dalla stazione "Cornelia" fino a "Spagna" (direzione Anagnina)."""

metroBarberini = """Prendi la metro A dalla stazione "Cornelia" fino a "Barberini" (direzione Anagnina)."""

metroFlaminio = """Prendi la metro A dalla stazione "Cornelia" fino a "Flaminio" (direzione Anagnina)."""


####################################
def Spagna(provenience):
    """ it guides you to Piazza di Spagna and inside it
    """
    if provenience == 'Spagna':
        ##############################################################################################################
        # inizia percorso in Spagna
        SegreSG.sendMessage(Id, 'Ecco la guida breve a Piazza di Spagna.')
        SegreSG.sendMessage(Id, 'https://drive.google.com/file/d/1m2vL_1_19eMDtjLqJ3yr1TeVtw-kHDCi/view?usp=sharing')
        SegreSG.sendMessage(Id, """Quando vorrai proseguire il tour digita il numero corrispondente alla prossima destinazione:
/2 Piazza del Popolo
/3 Mausoleo di Augusto
/4 Pantheon
/5 Fontana di Trevi""")
    elif provenience == 'Popolo':
        # percorso Popolo - Spagna
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Piazza+del+Popolo,+00187+Roma+RM/Piazza+di+Spagna,+Piazza+di+Spagna,+Roma,+RM/@41.9080115,12.4749543,16z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f60f8e5e81687:0x43ee9ffffdce4350!2m2!1d12.4763579!2d41.9107038!1m5!1m1!1s0x132f60551bc4f4e3:0xe876d6d8db1d5938!2m2!1d12.482327!2d41.9056978!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DA P.ZA DEL POPOLO A SPAGNA: Procedi in direzione sud su Piazza del Popolo verso Via del Babuino. Quindi procedi dritto fino a Spagna.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/1".""")
    elif provenience == 'Augusto':
        # percorso Augusto - Spagna
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Mausoleo+di+Augusto,+Piazza+Augusto+Imperatore,+Roma,+RM/Piazza+di+Spagna,+Piazza+di+Spagna,+Roma,+RM/@41.905857,12.4766909,17z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f6056f1882ae5:0x4916bb1e62c0e72c!2m2!1d12.4764264!2d41.9060311!1m5!1m1!1s0x132f60551bc4f4e3:0xe876d6d8db1d5938!2m2!1d12.482327!2d41.9056978!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DAL MAUSOLEO DI AUGUSTO A SPAGNA: Con il Tevere alle spalle, vai di fronte (sulla sinistra in Piazza Augusto) e procedi su Via dei Pontefici (prima) e continua su Via Vittoria (poi). Quando arrivi a Via del Babuino gira a destra e continua fino a Piazza di Spagna.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/1".""")
    elif provenience == 'Pantheon':
        # percorso Pantheon - Spagna
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Pantheon,+Piazza+della+Rotonda,+Roma,+RM/Piazza+di+Spagna,+Piazza+di+Spagna,+Roma,+RM/@41.9024031,12.4752361,16z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f604f678640a9:0xcad165fa2036ce2c!2m2!1d12.4768729!2d41.8986108!1m5!1m1!1s0x132f60551bc4f4e3:0xe876d6d8db1d5938!2m2!1d12.482327!2d41.9056978!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DAL PANTHEON A SPAGNA: Con il Pantheon alle spalle, vai di fronte su Via del Pantheon (prima) e continua su Via della Maddalena (poi). Al termine della via gira a destra e subito a sinistra su Via di Campo Marzio. Svolta a destra su Piazza S.Lorenzo in Lucina. Continua sempre dritto fino a che non troverai Piazza di Spagna alla tua sinistra.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/1".""")
    elif provenience == 'Trevi':
        # percorso Trevi - Spagna
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Fontana+di+Trevi,+Piazza+di+Trevi,+Roma,+RM/Piazza+di+Spagna,+Piazza+di+Spagna,+Roma,+RM/@41.9034239,12.4798221,16z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f6053278340d5:0xf676f1e1cc02bbb6!2m2!1d12.483313!2d41.9009325!1m5!1m1!1s0x132f60551bc4f4e3:0xe876d6d8db1d5938!2m2!1d12.482327!2d41.9056978!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DALLA FONTANA DI TREVI A SPAGNA: Con la Fontana alle spalle, vai a sinistra su Via del Lavatore (prima) e continua su Via in Arcione (poi). Gira a sinistra su Via del Traforo e prosegui dritto fino ad arrivare a Piazza di Spagna.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/1".""")

####################################
def Popolo(provenience):
    """ it guides you to Piazza del Popolo and inside it
    """    
    if provenience == 'Popolo':
        ##############################################################################################################
        # inizia percorso in Popolo
        SegreSG.sendMessage(Id, 'Ecco la guida breve a Piazza del Popolo.')
        SegreSG.sendMessage(Id, 'https://drive.google.com/open?id=1FIlM7loDpHb04uQQkIBMc6mYZpUQerNO')
        SegreSG.sendMessage(Id, """Quando vorrai proseguire il tour, digita il numero corrispondente alla prossima destinazione:
/1 Piazza di Spagna
/3 Mausoleo di Augusto
/4 Pantheon
/5 Fontana di Trevi""")
    if provenience == 'Spagna':
        # percorso Spagna - Popolo
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Piazza+di+Spagna,+Piazza+di+Spagna,+Roma,+RM/Piazza+del+Popolo,+00187+Roma+RM/@41.9082087,12.4749543,16z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f60551bc4f4e3:0xe876d6d8db1d5938!2m2!1d12.482327!2d41.9056978!1m5!1m1!1s0x132f60f8e5e81687:0x43ee9ffffdce4350!2m2!1d12.4763579!2d41.9107038!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DA SPAGNA A P.ZA DEL POPOLO: Avendo la Scalinata alle spalle, imbocca Via del Babuino, a destra della piazza. Prosegui dritto fino a raggiungere Piazza del Popolo.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/2".""")
    if provenience == 'Augusto':
        # percorso Augusto - Popolo
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Mausoleo+di+Augusto,+Piazza+Augusto+Imperatore,+Roma,+RM/Piazza+del+Popolo,+00187+Roma+RM/@41.9083714,12.4738699,17z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f6056f1882ae5:0x4916bb1e62c0e72c!2m2!1d12.4764264!2d41.9060311!1m5!1m1!1s0x132f60f8e5e81687:0x43ee9ffffdce4350!2m2!1d12.4763579!2d41.9107038!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DAL MAUSOLEO DI AUGUSTO A P.ZA DEL POPOLO: Avendo alle spalle il fiume Tevere e il Museo dell'Ara Pacis, prosegui a sinistra su Via di Ripetta, sempre dritto fino a raggiungere Piazza del Popolo.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/2".""")
    if provenience == 'Pantheon':
        # percorso Pantheon - Popolo
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Pantheon,+Piazza+della+Rotonda,+Roma,+RM/Piazza+del+Popolo,+00187+Roma+RM/@41.9046729,12.4680054,15z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f604f678640a9:0xcad165fa2036ce2c!2m2!1d12.4768729!2d41.8986108!1m5!1m1!1s0x132f60f8e5e81687:0x43ee9ffffdce4350!2m2!1d12.4763579!2d41.9107038!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DAL PANTHEON A P.ZA DEL POPOLO: Avendo il Pantheon alle spalle, vai dritto e imbocca Via della Rosetta (delle due, quella a sinistra). Al termine della strada, gira a sinistra su Via del Pozzo delle Cornacchie. Dopo circa 100m, gira a destra su Via della Scrofa e prosegui dritto fino a raggiungere Piazza del Popolo.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/2".""")
    if provenience == 'Trevi':
        # percorso Trevi - Popolo
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Fontana+di+Trevi,+Piazza+di+Trevi,+Roma,+RM/Piazza+del+Popolo,+00187+Roma+RM/@41.905617,12.4725141,15z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f6053278340d5:0xf676f1e1cc02bbb6!2m2!1d12.483313!2d41.9009325!1m5!1m1!1s0x132f60f8e5e81687:0x43ee9ffffdce4350!2m2!1d12.4763579!2d41.9107038!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DALLA FONTANA DI TREVI A P.ZA DEL POPOLO: Da Piazza di Trevi, imbocca Via dei Crociferi (guardando la Fontana, sul lato sinistro). Prosegui dritto su Via dei Sabini, fino alla fine. Gira a destra su Via del Corso e prosegui dritto fino all'arrivo a Piazza del Popolo.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/2".""")
    
####################################
def Augusto(provenience):
    """ it guides you to Mausoleo di Augusto and inside it
    """    
    if provenience == 'Augusto':
        ##############################################################################################################
        # inizia percorso in Augusto
        SegreSG.sendMessage(Id, 'Ecco la guida breve al Mausoleo di Augusto.')
        SegreSG.sendMessage(Id, 'https://drive.google.com/open?id=1TEnD3UQlIfHH5SBjjr27rqX1Jn6Ojifs')
        SegreSG.sendMessage(Id, """Quando vorrai proseguire il tour, digita il numero corrispondente alla prossima destinazione:
/1 Piazza di Spagna
/2 Piazza del Popolo
/4 Pantheon
/5 Fontana di Trevi""")
    if provenience == 'Spagna':
        # percorso Spagna - Augusto
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Piazza+di+Spagna,+00187+Roma+RM/Mausoleo+di+Augusto,+Piazza+Augusto+Imperatore,+Roma,+RM/@41.9065544,12.4768202,17z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f60551bc4f4e3:0xe876d6d8db1d5938!2m2!1d12.482327!2d41.9056978!1m5!1m1!1s0x132f6056f1882ae5:0x4916bb1e62c0e72c!2m2!1d12.4764264!2d41.9060311!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DA SPAGNA AL MAUSOLEO DI AUGUSTO: Avendo alle spalle la Scalinata, vai a destra su Via del Babuino. Dopo poco, gira a sinistra su Via Vittoria. Prosegui dritto fino ad arrivare al Mausoleo di Augusto.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/3".""")
    if provenience == 'Popolo':
        # percorso Popolo - Augusto
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Piazza+del+Popolo,+00187+Roma+RM/Mausoleo+di+Augusto,+Piazza+Augusto+Imperatore,+Roma,+RM/@41.9083714,12.4734802,17z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f60f8e5e81687:0x43ee9ffffdce4350!2m2!1d12.4763579!2d41.9107038!1m5!1m1!1s0x132f6056f1882ae5:0x4916bb1e62c0e72c!2m2!1d12.4764264!2d41.9060311!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DA P.ZA DEL POPOLO AL MAUSOLEO DI AUGUSTO: Rivolto verso Via del Corso, imbocca Via di Ripetta (delle due, a destra). Prosegui dritto fino a raggiungere il Mausoleo di Augusto.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/3".""")
    if provenience == 'Pantheon':
        # percorso Pantheon - Augusto
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Pantheon,+Piazza+della+Rotonda,+Roma,+RM/Mausoleo+di+Augusto,+Piazza+Augusto+Imperatore,+Roma,+RM/@41.9023289,12.4718582,16z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f604f678640a9:0xcad165fa2036ce2c!2m2!1d12.4768729!2d41.8986108!1m5!1m1!1s0x132f6056f1882ae5:0x4916bb1e62c0e72c!2m2!1d12.4764264!2d41.9060311!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DAL PANTHEON AL MAUSOLEO DI AUGUSTO: Avendo il Pantheon alle spalle, vai dritto e imbocca Via della Rosetta (delle due, quella a sinistra). Al termine della strada, gira a sinistra su Via del Pozzo delle Cornacchie. Dopo circa 100m, gira a destra su Via della Scrofa e prosegui dritto fino a raggiungere il Mausoleo di Augusto.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/3".""")
    if provenience == 'Trevi':
        # percorso Trevi - Augusto
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Fontana+di+Trevi,+Piazza+di+Trevi,+Roma,+RM/Mausoleo+di+Augusto,+Piazza+Augusto+Imperatore,+Roma,+RM/@41.903273,12.475021,16z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f6053278340d5:0xf676f1e1cc02bbb6!2m2!1d12.483313!2d41.9009325!1m5!1m1!1s0x132f6056f1882ae5:0x4916bb1e62c0e72c!2m2!1d12.4764264!2d41.9060311!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DALLA FONTANA DI TREVI AL MAUSOLEO DI AUGUSTO: Da Piazza di Trevi, imbocca Via dei Crociferi (guardando la Fontana, sul lato sinistro). Prosegui dritto su Via dei Sabini, fino alla fine. Gira a destra su Via del Corso e prosegui dritto fino all'incrocio con Via dei Condotti. Gira a sinistra su Via Tomacelli e prosegui per 300m. Quindi gira a destra su Via di Ripetta e prosegui dritto fino al Mausoleo di Augusto.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/3".""")


    
####################################
def Pantheon(provenience):
    """ it guides you to the Pantheon and inside it
    """    
    if provenience == 'Pantheon':
        ##############################################################################################################
        # inizia percorso al Pantheon
        SegreSG.sendMessage(Id, 'Ecco la guida breve del Pantheon.')
        SegreSG.sendMessage(Id, 'https://drive.google.com/file/d/1gvocSfYcnseGT0KZXdNPJ3HB07IJODUQ/view?usp=sharing')
        SegreSG.sendMessage(Id, """Quando vorrai proseguire il tour, digita il numero corrispondente alla prossima destinazione:
/1 Piazza di Spagna
/2 Piazza del Popolo
/3 Mausoleo di Augusto
/5 Fontana di Trevi""")
    if provenience == 'Spagna':
        # percorso Spagna - Pantheon
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Piazza+di+Spagna,+Piazza+di+Spagna,+Roma,+RM/Pantheon,+Piazza+della+Rotonda,+Roma,+RM/@41.9024031,12.4752163,16z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f60551bc4f4e3:0xe876d6d8db1d5938!2m2!1d12.482327!2d41.9056978!1m5!1m1!1s0x132f604f678640a9:0xcad165fa2036ce2c!2m2!1d12.4768729!2d41.8986108!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DA SPAGNA AL PANTHEON: Avendo la Scalinata alle spalle, imbocca Via Borgognona (a sinistra nella piazza). Prosegui fino alla fine, quindi gira a sinistra su Via del Corso, quindi subito a destra su Via Frattina. Prosegui fino alla fine, poi gira a sinistra su Via di Campo Marzio. Al termine della strada, gira a destra, quindi subito a sinistra, imboccando Via della Maddalena. Alla fine della strada, gira a sinistra e subito a destra su Via del Pantheon. Prosegui dritto.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/4".""")
    if provenience == 'Popolo':
        # percorso Popolo - Pantheon
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Piazza+del+Popolo,+00187+Roma+RM/Pantheon,+Piazza+della+Rotonda,+Roma,+RM/@41.9046729,12.4679443,15z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f60f8e5e81687:0x43ee9ffffdce4350!2m2!1d12.4763579!2d41.9107038!1m5!1m1!1s0x132f604f678640a9:0xcad165fa2036ce2c!2m2!1d12.4768729!2d41.8986108!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DA P.ZZA DEL POPOLO AL PANTHEON: Rivolto verso Via del Corso, imbocca Via di Ripetta (delle due, a destra). Prosegui su Via della Scrofa, fino a Largo Giuseppe Toniolo, quindi gira a sinistra. Prosegui su Via del Pozzo delle Cornacchie fino a incrociare Via della Rosetta, quindi gira a destra. Prosegui dritto fino al Pantheon.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/4".""")
    if provenience == 'Augusto':
        # percorso Augusto - Pantheon
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Mausoleo+di+Augusto,+Piazza+Augusto+Imperatore,+Roma,+RM/Pantheon,+Piazza+della+Rotonda,+Roma,+RM/@41.9023289,12.4717657,16z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f6056f1882ae5:0x4916bb1e62c0e72c!2m2!1d12.4764264!2d41.9060311!1m5!1m1!1s0x132f604f678640a9:0xcad165fa2036ce2c!2m2!1d12.4768729!2d41.8986108!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DAL MAUSOLEO DI AUGUSTO AL PANTHEON: Avendo il Tevere (e il Museo dell'Ara Pacis) alle spalle, imbocca Via di Ripetta (sulla destra nella piazza). Prosegui su Via della Scrofa, fino a Largo Giuseppe Toniolo, quindi gira a sinistra. Prosegui su Via del Pozzo delle Cornacchie fino a incrociare Via della Rosetta, quindi gira a destra. Prosegui dritto fino al Pantheon.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/4".""")
    if provenience == 'Trevi':
        # percorso Trevi - Pantheon
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Fontana+di+Trevi,+Piazza+di+Trevi,+Roma,+RM/Pantheon,+Piazza+della+Rotonda,+Roma,+RM/@41.8997756,12.4778577,17z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f6053278340d5:0xf676f1e1cc02bbb6!2m2!1d12.483313!2d41.9009325!1m5!1m1!1s0x132f604f678640a9:0xcad165fa2036ce2c!2m2!1d12.4768729!2d41.8986108!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DALLA FONTANA DI TREVI AL PANTHEON: Avendo la Fontana alle spalle, vai a destra su Via delle Muratte. Prosegui dritto su Via di Pietra, quindi ancora dritto su Via dei Pastini. Al termine della strada sulla sinistra troverai il Pantheon.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/4".""")


####################################
def Trevi(provenience):
    """ it guides you to Fontana di Trevi and inside it
    """    
    if provenience == 'Trevi':
        ##############################################################################################################
        # inizia percorso in Trevi
        SegreSG.sendMessage(Id, 'Ecco la guida breve alla Fontana di Trevi.')
        SegreSG.sendMessage(Id, 'https://drive.google.com/open?id=1P3GXpKgxYNYahEH3NhQMNmNoTyPXdiW7')
        SegreSG.sendMessage(Id, """Quando vorrai proseguire il tour, digita il numero corrispondente alla prossima destinazione:
/1 Piazza di Spagna
/2 Piazza del Popolo
/3 Mausoleo di Augusto
/4 Pantheon""")
    if provenience == 'Spagna':
        # percorso Spagna - Trevi
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Piazza+di+Spagna,+00187+Roma+RM/Fontana+di+Trevi,+Piazza+di+Trevi,+Roma,+RM/@41.9033975,12.4791511,16z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f60551bc4f4e3:0xe876d6d8db1d5938!2m2!1d12.482327!2d41.9056978!1m5!1m1!1s0x132f6053278340d5:0xf676f1e1cc02bbb6!2m2!1d12.483313!2d41.9009325!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DA SPAGNA ALLA FONTANA DI TREVI: Avendo la Scalinata alle spalle, imbocca sulla sinistra Via di Propaganda. Prosegui dritto su Via di Sant'Andrea delle Fratte fino al Largo del Nazareno. Quindi gira a sinistra su Via del Nazareno. All'incrocio con Via del Tritone, imbocca Via della Stamperia (di fronte, delle due a destra). Prosegui dritto fino a raggiungere Piazza di Trevi.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/5".""")
    if provenience == 'Popolo':
        # percorso Popolo - Trevi
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Piazza+del+Popolo,+00187+Roma+RM/Fontana+di+Trevi,+Piazza+di+Trevi,+Roma,+RM/@41.9054117,12.4714541,15z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f60f8e5e81687:0x43ee9ffffdce4350!2m2!1d12.4763579!2d41.9107038!1m5!1m1!1s0x132f6053278340d5:0xf676f1e1cc02bbb6!2m2!1d12.483313!2d41.9009325!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DA P.ZZA DEL POPOLO ALLA FONTANA DI TREVI: Imbocca Via del Corso. Prosegui sulla via fino a superare Largo Chigi (1km circa). Svolta a sinistra su Via dei Sabini e prosegui su Via dei Crociferi fino a giungere a Piazza Trevi.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/5".""")
    if provenience == 'Pantheon':
        # percorso Pantheon - Trevi
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Pantheon,+Piazza+della+Rotonda,+Roma,+RM/Fontana+di+Trevi,+Piazza+di+Trevi,+Roma,+RM/@41.8997756,12.4779128,17z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f604f678640a9:0xcad165fa2036ce2c!2m2!1d12.4768729!2d41.8986108!1m5!1m1!1s0x132f6053278340d5:0xf676f1e1cc02bbb6!2m2!1d12.483313!2d41.9009325!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DAL PANTHEON ALLA FONTANA DI TREVI: Avendo il Pantheon alle spalle, imbocca a destra Via del Seminario. Prosegui dritto fino ad incrociare Via del Corso, quindi gira a sinistra. Alla seconda, svolta a destra su Via delle Muratte, quindi prosegui dritto fino a Piazza Trevi.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/5".""")
    if provenience == 'Augusto':
        # percorso Augusto - Trevi
        if VISITORS[Id][0] == 'MAPS':
            SegreSG.sendMessage(Id, 'Ecco la strada: https://www.google.it/maps/dir/Mausoleo+di+Augusto,+Piazza+Augusto+Imperatore,+Roma,+RM/Fontana+di+Trevi,+Piazza+di+Trevi,+Roma,+RM/@41.9030676,12.475021,16z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f6056f1882ae5:0x4916bb1e62c0e72c!2m2!1d12.4764264!2d41.9060311!1m5!1m1!1s0x132f6053278340d5:0xf676f1e1cc02bbb6!2m2!1d12.483313!2d41.9009325!3e2?hl=it')
        elif VISITORS[Id][0] == 'FEET':
            SegreSG.sendMessage(Id, "DAL MAUSOLEO DI AUGUSTO ALLA FONTANA DI TREVI: Avendo il Tevere alla sinistra, con Ponte Cavour di fianco a voi, imboccate sulla destra Via Tomacelli. Proseguite fino a incrociare Via del Corso, quindi imboccala svoltando a destra. Prosegui dritto fino a superare Largo Chigi. Gira sulla destra su Via dei Sabini e prosegui dritto fino ad arrivare a Piazza Trevi.")
        SegreSG.sendMessage(Id, """Una volta arrivato/a digita "/5".""")



while 0 == 0:

    # update until someone writes a new message
    while last == 0 or last == SegreSG.getUpdates()[-1]['update_id']:
        SegreSG.getUpdates()

    # someone has written a message
    resp = SegreSG.getUpdates()[-1] #gets the message

    name = resp['message']['chat']['first_name'] #name of writer
    Id = resp['message']['chat']['id'] #id of writer
    text = resp['message']['text'] #text of the message

    if list(VISITORS.keys()) == [] or Id not in VISITORS.keys():
        #add a new user to the keys of VISITORS and ask for using MAPS
        VISITORS[Id] = []
        SegreSG.sendMessage(Id, 'Benvenuto. Preferisci utilizzare Google Maps per spostarti? Digita "sì" se decidi di usarlo, altrimenti digita "no" (consigliato se hai un livello di batteria troppo basso).')
        SegreSG.sendMessage(Id, 'Nel caso tu scelga "no" ti verranno date indicazioni "manuali" passo dopo passo.')
        SegreSG.sendMessage(Id, 'La scelta non potrà essere modificata successivamente. Google Maps sarà comunque utilizzato nel primo spostamento fondamentale.')

    elif Id in VISITORS.keys() and len(VISITORS[Id]) == 0:
        #check the answer to the usage of MAPS and add it to VISITORS[Id]
        if text in ['Sì','sì','SI','Si','si','sI','Yes','yes']:
            VISITORS[Id] += ['MAPS']
        else:
            VISITORS[Id] += ['FEET']
        SegreSG.sendMessage(Id, 'La tua preferenza è stata registrata. Puoi iniziare il tour scegliendo la prima tappa.')

    elif text != '/start' and len(VISITORS[Id]) != 0:
        #someone has written a command
        if len(VISITORS[Id]) == 1:
            VISITORS[Id] += [text]
            if text == '/errore':
                SegreSG.sendMessage(Id, 'Cominciamo bene! Riprova inserendo un comando valido.')
                VISITORS[Id] = VISITORS[Id][:-1]
            elif text == '/3' or text == '/1':
                SegreSG.sendMessage(Id, metroSpagna)
                if text == '/3':
                    SegreSG.sendMessage(Id, 'Una volta arrivato/a a Spagna, clicca sul seguente link per raggiungere il Mausoleo di Augusto.')
                    SegreSG.sendMessage(Id, 'https://www.google.it/maps/dir/Spagna,+Roma,+RM/Mausoleo+di+Augusto,+Piazza+Augusto+Imperatore,+Roma,+RM/@41.9065836,12.4772315,17z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f605560efd5f7:0x758d03a3986995a6!2m2!1d12.4830554!2d41.9065475!1m5!1m1!1s0x132f6056f1882ae5:0x4916bb1e62c0e72c!2m2!1d12.4764264!2d41.9060311!3e2?hl=it')
                    SegreSG.sendMessage(Id, 'Una volta sul posto, digita nuovamente "/3" per iniziare la visita.')
                else:
                    SegreSG.sendMessage(Id, 'Una volta sul posto, digita nuovamente "/1" per iniziare la visita.')
            elif text == '/2':
                SegreSG.sendMessage(Id, metroFlaminio)
                SegreSG.sendMessage(Id, 'Una volta sul posto, digita nuovamente "/2" per iniziare la visita.')
            elif text == '/4' or text == '/5':
                SegreSG.sendMessage(Id, metroBarberini)
                if text == '/4':
                    SegreSG.sendMessage(Id, 'Una volta arrivato/a a Barberini, clicca sul seguente link per raggiungere il Pantheon.')
                    SegreSG.sendMessage(Id, 'https://www.google.it/maps/dir/Barberini,+Roma,+RM/Pantheon,+Piazza+della+Rotonda,+Roma,+RM/@41.9017131,12.4783751,16z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f61abc26b2031:0x5be5af9827b80d2f!2m2!1d12.488969!2d41.9036298!1m5!1m1!1s0x132f604f678640a9:0xcad165fa2036ce2c!2m2!1d12.4768729!2d41.8986108!3e2?hl=it')
                    SegreSG.sendMessage(Id, 'Una volta sul posto, digita nuovamente "/4" per iniziare la visita.')
                if text == '/5':
                    SegreSG.sendMessage(Id, 'Una volta arrivato/a a Barberini, clicca sul seguente link per raggiungere la Fontana di Trevi.')
                    SegreSG.sendMessage(Id, 'https://www.google.it/maps/dir/Barberini,+Roma,+RM/Fontana+di+Trevi,+Piazza+di+Trevi,+00187+Roma+RM/@41.9022481,12.4841398,17z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x132f61abc26b2031:0x5be5af9827b80d2f!2m2!1d12.488969!2d41.9036298!1m5!1m1!1s0x132f6053278340d5:0xf676f1e1cc02bbb6!2m2!1d12.483313!2d41.9009325!3e2?hl=it')
                    SegreSG.sendMessage(Id, 'Una volta sul posto, digita nuovamente "/5" per iniziare la visita.')
            else:
                VISITORS[Id] = VISITORS[Id][:-1]

        # in caso di errore nella scelta iniziale
        elif len(VISITORS[Id]) == 2 and text == '/errore':
            VISITORS[Id] = VISITORS[Id][:-1]
            SegreSG.sendMessage(Id, 'Tranquillo. Reinserisci un comando e ricominciamo.')
            SegreSG.sendMessage(Id, 'Scegli bene, stavolta!')
                                
        # Piazza di Spagna /1
        elif text == '/1':
            Spagna(PLACES[VISITORS[Id][-1]][0])
            VISITORS[Id] += ['/1']

        # Piazza del Popolo /2
        elif text == '/2':
            Popolo(PLACES[VISITORS[Id][-1]][0])
            VISITORS[Id] += ['/2']

        # Mausoleo di Augusto /3
        elif text == '/3':
            Augusto(PLACES[VISITORS[Id][-1]][0])
            VISITORS[Id] += ['/3']

        # Pantheon /4
        elif text == '/4':
            Pantheon(PLACES[VISITORS[Id][-1]][0])
            VISITORS[Id] += ['/4']

        # Fontana di Trevi /5
        elif text == '/5':
            Trevi(PLACES[VISITORS[Id][-1]][0])
            VISITORS[Id] += ['/5']

        # in caso di errore
        elif text == '/errore':
            SegreSG.sendMessage(Id, 'Se hai sbagliato scelta, digita due volte il comando corrispondente al luogo dove sei ora (un inserimento alla volta). Poi inserisci il comando corrispondente al luogo dove vuoi andare.')
            SegreSG.sendMessage(Id, """Dove sei ora? Inserisci due volte (sempre un inserimento alla volta) il comando relativo:
/1 Piazza di Spagna;
/2 Piazza del Popolo;
/3 Mausoleo di Augusto;
/4 Pantheon;
/5 Fontana di Trevi.""")

    last = SegreSG.getUpdates()[-1]['update_id']
