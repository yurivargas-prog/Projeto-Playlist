import streamlit as st 

generos = {    
    'Eletronica' : {
        "Alok" : "https://www.youtube.com/watch?v=JVpTp8IHdEg&list=RDJVpTp8IHdEg&start_radio=1",
       
    },
    ' Hip Hop':{
        'Hungria' : "https://www.youtube.com/watch?v=OHgpwHgMUhY&list=RDOHgpwHgMUhY&start_radio=1",

    }, 
      'Rock' :{
      'Nirvana' : "https://www.youtube.com/watch?v=hTWKbfoikeg&list=RDhTWKbfoikeg&start_radio=1",
    
      },

    'Pop' : {
    'Calvin Harris' : "https://www.youtube.com/watch?v=ebXbLfLACGM&list=RDebXbLfLACGM&start_radio=1",
   
    },
}

st. sidebar.title("Playlists a journy to the beyond")
st. sidebar.image("CEO TESLA.png")
genero = st.sidebar.selectbox(" selecione um genero musical", generos. keys())
artista = st. sidebar.selectbox("selecione uma artista ",generos[genero].keys())
st.title(artista)


video, sobre = st.tabs(["video ","sobre o artista "])

with video: 
            st.video(generos[genero][artista])

with sobre : 
    if artista == "Alok" : 
        st.markdown("""  Peres Petrillo (Goiânia, 26 de agosto de 1991) é um DJ e produtor musical brasileiro,[5] mais conhecido por seu sucesso mundial
    de 2016 "Hear Me Now".[6] É atualmente o terceiro melhor DJ do mundo segundo a revista britânica DJ Mag.[7]""")



    elif artista == 'Hungria' :
        st.markdown("""Hungria ficou conhecido nacionalmente pelo seu primeiro single, Bens Materiais, mas 
só alcançou sucesso fora do território nacional
com as músicas Dubai, Lembranças, Coração de Aço, Beijo Com Trap, Temporal, Chovendo Inimigo,
O Playboy Rodou, Não Troco, Quebra-Cabeça, Um Pedido, Insônia e Amor e Fé,""")



    elif artista == 'Nirvana' :
        st.markdown(""" Nirvana foi uma banda estadunidense de rock formada pelo vocalista e guitarrista Kurt Cobain 
e pelo baixista Krist Novoselic em Aberdeen no ano de 1987,[1] que obteve grande sucesso no movi
mento grunge de Seattle no início dos anos 1990. Vários bateristas passaram pelo
Nirvana, sendo o que ficou mais tempo na banda foi Dave Grohl, que entrou em 1990.""")


    elif artista == "Calvin Harris" :
        st.markdown("""Adam Richard Wiles (Dumfries, 17 de janeiro de 1984), mais conhecido pelo nome artístico Calvin
    Harris, é um DJ, produtor musical, cantor e compositor escocês. De acordo com a Forbes, foi o DJ ma
is bem pago do mundo em 2013 e em 2014, valendo 66 milhões de dólares (60 milhões de euros) em 2015""")



