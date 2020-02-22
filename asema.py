import numpy as np

def kulkusuunta(n):
    if np.mod(n, 22) < 11:
        suunta = 'P'
    else:
        suunta = 'E'

    return suunta


def asema(n):
    asemat = ['Helsinki', 'Pasila', 'Tikkurila', 'Tampere', 'Parkano', 'Seinäjoki', 'Kokkola', 'Ylivieska', 'Oulainen', 'Oulu', 'Kemi', 'Rovaniemi']
    return asemat[n]

n_alkiot = 22

#
# OPASTUS: alla oleva silmukka käy läpi kaikki parit (asema,kulkusuunta), joita on
#          n_alkiot verran. Muuttuja n käy silmukassa läpi kaikki nämä parit.
#
#          Kun juna liikku lähtötilasta n delta_n asemaväliä, pääteasemaa vastaava
#          uusi n:n arvo on
#
#                       uusi_n = np.mod(n + delta_n, n_alkiot)
#
#          Tämän jälkeen tätä uutta n:n arvo vastaava kulkusuunta on
#          kulkusuunta(uusi_n).
#
#          Viimeinen vaihe on hakea arvoa uusi_n vastaava aseman nimi. Koska useimpiin asemiin
#          liitty kaksi mahdollista kulkusuuntaaun, asemien nimiä on vähemmän kuin
#          (asema,kulkusuunta)-pareja. Tästä syystä ohjelmaa kirjoittaessa pitää
#          miettiä, miten n kuvataan aseman nimeä vastaavaksi indeksiksi (jonka avulla
#          saadaan aseman nimi).
#

for n in range(0,n_alkiot):

    # Muttuja lahto_suunta tarkoittaa lähtötilanteen kulkusuuntaa

    lahto_suunta = kulkusuunta(n)

    # Täydennä rivit, jotka määrittävät lähtöaseman
    # Tarvinnet tähän if-lauseen

    if  np.mod(n, 22) < 11:
        lahto_asema = asema(np.mod(n, 11))
    else:
        lahto_asema = asema(11-np.mod(n, 11))

    #
    #  KOPIOI tähän saakka edellisen tehtävän 2 ohjelma ilman print-komentoa.
    #
    #  Muokkaa sen jälkeen ohjelmaasi niin, että se laskee kutakin lähtöasemaa
    #  ja kulkusuuntaa vastaavan seuraavan yhden asemavälin päässä olevan aseman
    #  ja kulkusuunnan. Laske tämä numeroilla, ja käytä funktioita hakeaksesi
    #  kutakin numeroa vastaavan asemanimen ja kulkusuunnan.
    #

    # lahto_a on lähtöseman numero

    lahto_a = n

    # delta_a on asemavälien muutos

    delta_a = 187

    # Täydennä loppu siten, että pääteaseman nimi sijoitetaan muuttujaan
    # paate_suunta, ja kulkusuunta sijoitetaan muuttujaan paate_suunta.
    # Huomaa, että tarvitset if-lauseita paate_aseman määrittämiseen argumentista n.

    uusi_n =  np.mod(lahto_a + delta_a, n_alkiot)
    paate_suunta = kulkusuunta(uusi_n)
    #paate_asema = asema(np.mod(uusi_n, 11))

    if np.mod(uusi_n, 22) <= 11:
        paate_asema = asema(np.mod(uusi_n, 12))
    else:
        paate_asema = asema(11-np.mod(uusi_n, 11))
    # Älä muuta seuraavaa print-komentoa, jotta kone osaa tarkastaa vastauksesi

    print('Lähtöasema: {}, suunta: {}'.format(lahto_asema, lahto_suunta))
    print('Pääteasema: {}, suunta: {}'.format(paate_asema, paate_suunta))
    print('---')